import yfinance as yf
import pandas as pd

def download_history(
    ticker:str,
    multi_level_index:bool = False
)-> pd.DataFrame:  
    '''
    Download historical data from yahoofinance;
    
    Args:
        ticker (str): Ticker Name.
        multi_level_index (bool): Remove/include multi index.       
    '''
    

    df = yf.download(
        tickers=ticker, 
        multi_level_index = multi_level_index
    ).reset_index()
    
    return df
