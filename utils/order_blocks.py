def identify_order_blocks(df):
    df['order_block'] = (df['high'].shift(1) > df['high']) & (df['low'].shift(1) < df['low'])
    return df
