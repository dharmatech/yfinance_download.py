
import os
import pathlib
import pandas as pd
import yfinance as yf

# symbol = '^GSPC'

def update_records(symbol, interval='1d'):

    symbol = symbol.replace('/', '_')

    path = f'pkl/{symbol}-{interval}.pkl'

    if os.path.isfile(path):

        print(f'Found {path}. Importing.')

        df = pd.read_pickle(path)

        # if df.empty:
        #     print(f'No records found for {symbol}.')
        #     return None        

        if len(df) == 1:
            print(f'Only one record found for {symbol}. Removing pkl.')
            os.remove(path)
            return None 
                   
        recent_record_date = df.index.unique()[-2]

        print(f'Recent record date: {recent_record_date}')

        new_records = yf.download(tickers=symbol, interval=interval, start=recent_record_date, progress=False)



        # yf.download(tickers='^GSPC', interval='1d', start='2024-09-16', progress=False)



        df = df[df.index < recent_record_date]

        df = pd.concat([df, new_records])

        df.to_pickle(path)

        return df

    else:

        pathlib.Path('pkl').mkdir(parents=True, exist_ok=True)

        df = yf.download(tickers=symbol, interval=interval, progress=False)
        
        if df.empty:
            print(f'No records found for {symbol}.')
            return None
        
        if len(df) == 1:
            print(f'Only one record found for {symbol}.')
            return None
        
        df.to_pickle(path)

        return df
    

def load_records(symbol, interval='1d', update=False):

    symbol = symbol.replace('/', '_')

    path = f'pkl/{symbol}-{interval}.pkl'

    if os.path.isfile(path):

        print(f'Found {path}. Importing.')

        df = pd.read_pickle(path)

        if len(df) == 1:
            print(f'Only one record found for {symbol}. Removing pkl.')
            os.remove(path)
            return None 
        
        if update == False:
            return df
                   
        recent_record_date = df.index.unique()[-2]

        print(f'Recent record date: {recent_record_date}')

        new_records = yf.download(tickers=symbol, interval=interval, start=recent_record_date, progress=False)

        df = df[df.index < recent_record_date]

        df = pd.concat([df, new_records])

        df.to_pickle(path)

        return df

    else:

        pathlib.Path('pkl').mkdir(parents=True, exist_ok=True)

        df = yf.download(tickers=symbol, interval=interval, progress=False)
        
        if df.empty:
            print(f'No records found for {symbol}.')
            return None
        
        if len(df) == 1:
            print(f'Only one record found for {symbol}.')
            return None
        
        df.to_pickle(path)

        return df
    
    