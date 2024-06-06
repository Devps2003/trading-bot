# strategy.py

import pandas as pd
import numpy as np

def moving_average_crossover(data, short_window=50, long_window=200):
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    
    data['Signal'] = 0
    data['Signal'][short_window:] = \
        np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    
    data['Position'] = data['Signal'].diff()
    
    return data

if __name__ == "__main__":
    data = pd.read_csv("data.csv", index_col='Date', parse_dates=True)
    result = moving_average_crossover(data)
    result.to_csv("strategy_output.csv")
