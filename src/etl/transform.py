def transform(dataframe):
    df = dataframe.iloc[9:19]
    df = df[['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6', 'Unnamed: 8']]
    df.rename(columns={
    'Unnamed: 0': 'year',
    'Unnamed: 2': 'less_than_one_point_four',
    'Unnamed: 4': 'one_point_four_less_than_two_point_seven',
    'Unnamed: 6': 'greater_than_two_point_seven',
    'Unnamed: 8': 'total'
    }, inplace=True)
    return df