import argparse
from .scraper import process_stations

def main():
    parser = argparse.ArgumentParser(description="DBHYDRO Station Lat/Lon Scraper")
    parser.add_argument(
        "--input",
        type=str,
        default="data/input/station_list.csv",
        help="Input CSV file with comma-separated station names (default: data/input/station_list.csv)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/output/List_of_Salinity.csv",
        help="Output CSV file to write results (default: data/output/List_of_Salinity.csv)",
    )
    args = parser.parse_args()
    process_stations(args.input, args.output)

if __name__ == "__main__":
    main()
