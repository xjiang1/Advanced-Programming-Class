import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb # optional to set plot theme
sb.set_theme() # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = None
        
        self.get_data()


    def get_data(self):
        #method that downloads data and stores in a DataFrame uncomment the code below wich should be the final two lines of your method#
        import yfinance as yf
        
        data = yf.download(self.symbol,start = self.start, end = self.end)
        
        data.reset_index(inplace=True)
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        
        self.data = data
        
        self.calc_returns(data)
        return data 

    
    def calc_returns(self, df):
        #method that adds change and return columns to data#
        #change column – the difference between the close to close price relative to the previous day’s close
        self.data['change_column'] = self.data['Close'] - self.data['Close'].shift(1)
        #instant_return – the daily instantaneous rate of return (np.log([closing_price]).diff().round(4))
        self.data['instant_return'] = np.log(self.data['Close']).diff().round(4)
          

    
    def plot_return_dist(self):
        #method that plots instantaneous returns as histogram
        plt.hist(self.data.instant_return, bins=50, density = True, color='skyblue', edgecolor='darkblue')
        plt.xlabel('Instantaneous returns')
        plt.ylabel('rate')
        plt.title('Daily Instantaneous Rate of Return')
        plt.show()


    def plot_performance(self):
        #method that plots stock object performance as percent
        self.data['Percent_Change'] = ((self.data['Close'] - self.data['Close'].iloc[0]) / self.data['Close'].iloc[0]) * 100
        plt.plot(self.data.index, self.data['Percent_Change'], color='skyblue', linestyle='-')
   
        plt.xlabel('Date')
        plt.ylabel('Percent Change (%)')
        plt.title('Stock Performance')
        
        plt.show()
                  

def main():
    # uncomment (remove pass) code below to test
    test = Stock(symbol=["AAPL"]) # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()

if __name__ == '__main__':
    main() 