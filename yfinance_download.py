
import os
import pathlib
import pandas as pd
import yfinance as yf
    
def update_records(symbol):

    path = f'pkl/{symbol}.pkl'

    if os.path.isfile(path):

        print(f'Found {path}. Importing.')

        df = pd.read_pickle(path)

        recent_record_date = df.index.unique()[-2]

        print(f'Recent record date: {recent_record_date}')

        new_records = yf.download(tickers=symbol, start=recent_record_date, progress=False)        

        df = df[df.index < recent_record_date]

        df = pd.concat([df, new_records])

        df.to_pickle(path)

        return df

    else:

        pathlib.Path('pkl').mkdir(parents=True, exist_ok=True)
    
        df = yf.download(tickers=symbol, progress=False)
        
        df.to_pickle(path)

        return df