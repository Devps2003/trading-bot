# backtester.py

import pandas as pd

def backtest(data, initial_balance=10000, share_size=10):
    balance = initial_balance
    positions = 0
    balance_history = []

    for i in range(len(data)):
        if data['Position'][i] == 1 and balance >= data['Close'][i] * share_size:
            positions += share_size
            balance -= data['Close'][i] * share_size
        elif data['Position'][i] == -1 and positions > 0:
            balance += data['Close'][i] * positions
            positions = 0
        balance_history.append(balance + positions * data['Close'][i])

    data['Balance'] = balance_history
    return data

if __name__ == "__main__":
    data = pd.read_csv("strategy_output.csv", index_col='Date', parse_dates=True)
    result = backtest(data)
    result.to_csv("backtest_output.csv")
