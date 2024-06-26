def identify_market_structure(df):
    df['HH'] = (df['high'] > df['high'].shift(1)) & (df['high'] > df['high'].shift(-1))
    df['LL'] = (df['low'] < df['low'].shift(1)) & (df['low'] < df['low'].shift(-1))
    df['HL'] = (df['low'] > df['low'].shift(1)) & (df['low'] < df['low'].shift(-1))
    df['LH'] = (df['high'] < df['high'].shift(1)) & (df['high'] > df['high'].shift(-1))
    return df
