import io
import pandas as pd
import yfinance as yf
import seaborn as sns
import os


class StockScraper:
    """
    Creates a StockScraper object with methods that allow you to scrape data and write it to a CSV file.
    Scraped data can be curated in various ways.

    Class variables:
    :cvar stock_list: list[str] of stock symbols to track. default = None
    :cvar df: pd.DataFrame containing stock data
    :cvar file_path: path to csv file where stock data is written. default = None
    """
    stock_list: list[str]
    df: pd.DataFrame = pd.DataFrame()
    file_path: str

    def __init__(self, stock_list: list[str] | str | None = None, file_path: str = None):
        """

        :param stock_list: list[str] or str of stock symbols to track. default = None. if str: delimit tickers with
        comma.
        :param file_path: path to csv file where stock data is written. default = None.
        format as 'Directory\\...\\filename.csv'
        """

        if stock_list is list:
            self.stock_list = stock_list
        elif stock_list is str:
            self.stock_list = stock_list.split(',')
        elif stock_list is None:
            self.stock_list = ['GOOG', 'AAPL', 'MSFT', 'NVDA', 'TSLA', 'INTC']  # Default stocks if none are provided.

        if file_path is not None:
            self.file_path = file_path
        elif os.path.exists('stock_data.csv'):
            self.file_path = 'stock_data.csv'
        else:
            self.file_path = 'stock_data.csv'
            os.makedirs('stock_data.csv', exist_ok=True)

        with open('stock_data.csv', 'a') as f:
            try:
                f.readlines()
                self.df = pd.read_csv(f)
            except io.UnsupportedOperation:
                self.df = self.pull_data()
            finally:
                f.close()

    def pull_data(self):
        """
        Pulls yfinance stock data for a period of one day at 1 min intervals,
        cleans returned dataframe and then returns the cleaned dataframe.
        :return: Dataframe containing stock data.
        """

        df = yf.download(tickers=self.stock_list, period='1d', interval='1m', group_by='ticker')

        return df

    def calculate_values(self):
        pass
