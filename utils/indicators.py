import pandas_ta as ta # type: ignore

def calculate_indicators(df):
    df['5ema'] = ta.ema(df['close'], length=5)
    df['10ema'] = ta.ema(df['close'], length=10)
    df['stoch_k'], df['stoch_d'] = ta.stoch(df['high'], df['low'], df['close'], k=10, d=3, smooth_k=3)
    df['rsi'] = ta.rsi(df['close'], length=14)
    return df
