import csv
import requests
from bs4 import BeautifulSoup
from typing import Optional, Tuple, List

def fetch_station_lat_lon(station_name: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Fetch latitude and longitude for a given station name from the Current DBHYDRO website.
    Returns (lat, lon) as strings, or (None, None) if not found.
    """
    url = "https://my.sfwmd.gov/dbhydroplsql/show_dbkey_info.show_station_info"
    data = {"v_station": station_name}
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None, None
    soup = BeautifulSoup(response.text, "html.parser")
    lat, lon = None, None
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 2:
            if "Latitude" in cells[0].text:
                lat = cells[1].text.strip()
            if "Longitude" in cells[0].text:
                lon = cells[1].text.strip()
    return lat, lon

def process_stations(
    input_path: str = "data/input/station_list.csv",
    output_path: str = "data/output/List_of_Salinity.csv"
) -> None:
    """
    Read station names from a comma-separated file (no header), fetch lat/lon, and write to output CSV.
    Output format: Station_ID,Has available data ?,LAT (ddmmss.sss),LON (ddmmss.sss)
    The 'Has available data ?' column is always empty.
    """
    with open(input_path, newline="") as infile:
        line = infile.readline()
        station_names = [name.strip() for name in line.split(",") if name.strip()]
    fieldnames = [
        "Station_ID",
        "Has available data ? (Testing with get_wq())",
        "LAT (ddmmss.sss)",
        "LON (ddmmss.sss)"
    ]
    with open(output_path, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for station_id in station_names:
            lat, lon = fetch_station_lat_lon(station_id)
            writer.writerow({
                "Station_ID": station_id,
                "Has available data ? (Testing with get_wq())": "",
                "LAT (ddmmss.sss)": lat or "",
                "LON (ddmmss.sss)": lon or ""
            })
