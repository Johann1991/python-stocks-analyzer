def identify_liquidity_zones(df):
    df['support'] = df['low'].rolling(window=10).min()
    df['resistance'] = df['high'].rolling(window=10).max()
    return df
