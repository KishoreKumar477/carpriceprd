def encode_features(df):
    df = df.copy()

    df.replace({
        'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2},
        'Seller_Type': {'Dealer': 0, 'Individual': 1},
        'Transmission': {'Manual': 0, 'Automatic': 1}
    }, inplace=True)

    df = df.infer_objects(copy=False)  

    return df
