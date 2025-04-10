import StockScraper


def main():
    scraper = StockScraper.StockScraper(file_path='stock_data.csv')
    print(scraper.df.columns)


if __name__ == '__main__':
    main()
