# Bloomberg Harvester - Data Extraction Suite

## 🎯 Objective
This repository contains a unified Python script designed to extract targeted, highly valuable historical financial data from a Bloomberg Terminal. The goal is to build a massive, pristine "Data Lake" for quantitative modeling.

## 📦 What This Script Does
Instead of running multiple different scripts, everything is unified into a single command to minimize moving parts. The script will sequentially extract the following datasets:

1. **Historical Options Surface & GEX (GameStop focus):** Pulls historical Implied Volatility (IV), Gamma, and Open Interest to map market maker hedging profiles over time.
2. **Historical Sentiment & News Flow:** Pulls aggregated headlines and proprietary Bloomberg sentiment scores for specific macro cycles. *(Note: We are pulling metadata and sentiment scores, not the raw article text, to keep the data clean and structured).*
3. **Supply Chain Data (`SPLC`):** Extracts quantitative revenue dependencies between major S&P 500 companies to map upstream/downstream ripples.
4. **Institutional Ownership (`HDS`):** Pulls historical 13F flows to identify stealth accumulation by smart money.

## 🚀 Execution Instructions for Windows (PC)

### Prerequisites
1. Ensure you are logged into the Bloomberg Terminal on this machine.
2. Ensure Python is installed (3.8+ recommended).
3. Open a Command Prompt or PowerShell terminal.

### Setup
1. Clone or download this repository.
2. Navigate to the folder in your terminal:
   ```cmd
   cd path\to\Bloomberg_Harvester
   ```
3. Install the required Bloomberg API libraries:
   ```cmd
   pip install -r requirements.txt
   ```

### Running the Harvester
Run the master script:
```cmd
python bloomberg_harvester.py
```

### The Output
The script will create an `output/` directory and populate it with `.parquet` and `.csv` files. 
Once the script finishes, simply zip the `output/` folder and upload it to Google Drive or Dropbox.

## 🧠 Data Architecture Notes
- **Why Parquet?** We use Apache Parquet formats for the massive datasets. Parquet compresses massive data much better than CSV and preserves data types across different operating systems (Windows to Mac).
- **Limits:** The script is designed with standard Bloomberg API data limits in mind, utilizing batching where necessary.
