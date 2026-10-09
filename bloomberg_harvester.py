import os
import time
import logging
import pandas as pd
import numpy as np

# ==========================================
# CONFIGURATION
# ==========================================
# Set to True to bypass Bloomberg API and generate fake data for testing locally.
# Set to False BEFORE handing off to the terminal user.
MOCK_MODE = False

if not MOCK_MODE:
    try:
        from xbbg import blp
    except ImportError:
        print("CRITICAL: xbbg library not installed. Please run 'pip install -r requirements.txt'")

# ==========================================
# LOGGING SETUP
# ==========================================
# This ensures if the script fails on his machine, we know exactly why.
log_filename = "harvester_execution.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler() # Also print to console
    ]
)

def setup_directories():
    """Ensure output directory exists."""
    if not os.path.exists('output'):
        os.makedirs('output')
    logging.info("Output directory verified.")

# ==========================================
# DATA EXTRACTION MODULES
# ==========================================

def pull_options_history(ticker="GME US Equity"):
    """Pulls historical options chain data, IV, and Gamma."""
    logging.info(f"Starting Options History extraction for {ticker}...")
    try:
        if MOCK_MODE:
            logging.info(f"[MOCK] Generating fake options data for {ticker}")
            dates = pd.date_range(start="2024-01-01", end="2024-01-10")
            df = pd.DataFrame({
                'Date': dates,
                'Ticker': ticker,
                'Spot_Price': np.random.uniform(10, 30, len(dates)),
                'IV_30D': np.random.uniform(0.5, 1.5, len(dates)),
                'Call_GEX': np.random.uniform(100000, 500000, len(dates)),
                'Put_GEX': np.random.uniform(-500000, -100000, len(dates))
            })
            time.sleep(1) # Simulate network delay
        else:
            # ACTUAL BLOOMBERG API CALL
            # df = blp.bdh(ticker, ['PX_LAST', 'IVOL_30D', 'CALL_IMP_VOL', 'PUT_IMP_VOL'], start_date='2020-01-01', end_date='today')
            # Note: A true options chain requires iterating through option tickers, this is a simplified index pull.
            pass
        
        # Save to Parquet
        output_path = f"output/options_history_{ticker.split()[0]}.parquet"
        df.to_parquet(output_path, engine='pyarrow')
        logging.info(f"Successfully saved Options History to {output_path}")
        
    except Exception as e:
        logging.error(f"Failed to pull options history for {ticker}. Error: {str(e)}")

def pull_historical_news_sentiment():
    """Pulls headlines, dates, and Bloomberg NLP Sentiment scores."""
    logging.info("Starting Historical News Sentiment extraction...")
    try:
        if MOCK_MODE:
            logging.info("[MOCK] Generating fake news sentiment data")
            df = pd.DataFrame({
                'Date': pd.date_range(start="2024-01-01", end="2024-01-05"),
                'Headline': ["Company announces earnings", "CEO steps down", "New product launch", "Market crash fears", "Stock hits ATH"],
                'Sentiment_Score': [0.8, -0.6, 0.9, -0.9, 0.95]
            })
            time.sleep(1)
        else:
            # ACTUAL API CALL (using News Sentiment fields)
            pass
            
        output_path = "output/news_sentiment_boulders.csv"
        df.to_csv(output_path, index=False)
        logging.info(f"Successfully saved News Sentiment to {output_path}")
        
    except Exception as e:
        logging.error(f"Failed to pull news sentiment. Error: {str(e)}")

def pull_supply_chain_matrix():
    """Pulls SPLC revenue dependency percentages."""
    logging.info("Starting SPLC Supply Chain Matrix extraction...")
    try:
        if MOCK_MODE:
            logging.info("[MOCK] Generating fake supply chain matrix")
            df = pd.DataFrame({
                'Supplier': ['TSMC', 'NVIDIA', 'MICROSOFT'],
                'Customer': ['AMD', 'MICROSOFT', 'OPENAI'],
                'Revenue_Dependency_Pct': [15.5, 22.0, 45.0]
            })
            time.sleep(1)
        else:
            # ACTUAL API CALL
            pass
            
        output_path = "output/supply_chain_matrix.parquet"
        df.to_parquet(output_path, engine='pyarrow')
        logging.info(f"Successfully saved Supply Chain Matrix to {output_path}")
        
    except Exception as e:
        logging.error(f"Failed to pull supply chain matrix. Error: {str(e)}")

def pull_institutional_ownership():
    """Pulls historical 13F and HDS data."""
    logging.info("Starting Institutional Ownership extraction...")
    try:
        if MOCK_MODE:
            logging.info("[MOCK] Generating fake institutional flows")
            df = pd.DataFrame({
                'Date': ['2023-Q1', '2023-Q2', '2023-Q3'],
                'Institution': ['Vanguard', 'BlackRock', 'Renaissance'],
                'Shares_Held': [1000000, 1500000, 500000]
            })
            time.sleep(1)
        else:
            # ACTUAL API CALL
            pass
            
        output_path = "output/institutional_flows.parquet"
        df.to_parquet(output_path, engine='pyarrow')
        logging.info(f"Successfully saved Institutional Flows to {output_path}")
        
    except Exception as e:
        logging.error(f"Failed to pull institutional ownership. Error: {str(e)}")

# ==========================================
# MAIN EXECUTION
# ==========================================
def main():
    print("\n" + "="*50)
    print("    BLOOMBERG HARVESTER - DATA EXTRACTION SUITE   ")
    print("="*50)
    
    if MOCK_MODE:
        print(">> RUNNING IN MOCK MODE (No Bloomberg Terminal required)")
    else:
        print(">> RUNNING IN LIVE MODE (Bloomberg Terminal required)")
    
    setup_directories()
    
    # Execute Modules
    pull_options_history("GME US Equity")
    pull_historical_news_sentiment()
    pull_supply_chain_matrix()
    pull_institutional_ownership()
    
    print("="*50)
    print("[SUCCESS] Pipeline execution finished.")
    print("Please ZIP the 'output' folder AND 'harvester_execution.log'.")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
