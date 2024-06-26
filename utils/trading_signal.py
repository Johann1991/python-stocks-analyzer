def trading_signal(df):
    signals = []
    for i in range(1, len(df)):
        if (df['5ema'].iloc[i] > df['10ema'].iloc[i] and 
            df['stoch_k'].iloc[i] > df['stoch_d'].iloc[i] and 
            df['stoch_k'].iloc[i] < 80 and 
            df['rsi'].iloc[i] > 50 and
            df['HH'].iloc[i] and
            df['order_block'].iloc[i]):
            signals.append('buy')
        elif (df['5ema'].iloc[i] < df['10ema'].iloc[i] and 
              df['stoch_k'].iloc[i] < df['stoch_d'].iloc[i] and 
              df['stoch_k'].iloc[i] > 20 and 
              df['rsi'].iloc[i] < 50 and
              df['LL'].iloc[i] and
              df['order_block'].iloc[i]):
            signals.append('sell')
        else:
            signals.append('hold')
    df['signal'] = signals
    return df
