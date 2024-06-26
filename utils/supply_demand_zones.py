def identify_supply_demand_zones(df):
    df['demand_zone'] = df['low'].rolling(window=10).min()
    df['supply_zone'] = df['high'].rolling(window=10).max()
    return df
