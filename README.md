# DBHYDRO Station Lat/Lon Scraper

A CLI tool to fetch latitude and longitude for a list of DBHYDRO station names and output them in a standardized CSV format.

---

## 🚀 Setup Instructions

1. **Clone or Download the Project**
   - Place the `dbhydro-scraper` folder in your desired directory.

2. **Install Python Dependencies**
   - Ensure you have Python 3.7+ installed.
   - Install required packages:
     ```sh
     pip3 install -r dbhydro-scraper/requirements.txt
     ```

---

## 📥 Preparing Input Data

- Place your station names in:
  ```
  dbhydro-scraper/data/input/station_list.csv
  ```
- The file should contain a single line with station names separated by commas (no header), for example:
  ```
  P37,FLAB10,C111AC
  ```

---

## ▶️ Running the Script

> **Important:**  
> Always run the script from the parent directory of `dbhydro-scraper` (e.g., `/Users/yourname/code/github/DBHYDRO`).

Run:
Specify custom input/output paths:
```sh
python3 -m dbhydro-scraper --input dbhydro-scraper/data/input/station_list.csv --output dbhydro-scraper/data/output/List_of_Salinity.csv
```

---

## 📤 Output

- Results are saved to:
  ```
  dbhydro-scraper/data/output/List_of_Salinity.csv
  ```
- The output CSV columns:
  ```
  Station_ID,Has available data ? (Testing with get_wq()),LAT (ddmmss.sss),LON (ddmmss.sss)
  ```
  - The `Has available data ? ` column will always be empty.

---

## 🛠️ Troubleshooting

- Ensure your input file is formatted correctly (no header, one line, comma-separated).
- Always run the script from the parent directory of `dbhydro-scraper`.
- SSL/LibreSSL warnings can usually be ignored unless you encounter connection errors.

---

**For any issues, check your input file and ensure you are running the script from the correct directory.** 