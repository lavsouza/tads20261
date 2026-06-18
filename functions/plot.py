import plotly.express as px

from functions.data import download_history
from plotly.graph_objects import Figure

def plot_history(
    ticker:str
)-> Figure: 
    '''
    Plot historical data from Yahoo Finance (yfinance) specified ticker;
    
    Args:
        ticker (str): Ticker Name.
    '''
    df = download_history(ticker)

    fig = px.line(
        df,
        x = 'Date',
        y = 'Close',
        title= f'{ticker} Stock Price.'
    )
    
    return fig



