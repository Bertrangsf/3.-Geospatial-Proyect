import pandas 

def df_final(df1,df2,df3):
    df = pandas.concat([df1, df2, df3])
    df = df.drop(["alt", "elevation"], axis = 1) 
    df.reset_index(inplace = True)
    df.rename(columns={"standard": "city"}, inplace=True)

    df = df.drop(df[df["index"] == "addresst"].index)
    df = df.drop(df[df["index"] == "prov"].index)
    df = df.drop(df[df["index"] == "countryname"].index)
    df = df.drop(df[df["index"] == "postal"].index)
    df = df.drop(df[df["index"] == "loc"].index)
    df = df.drop(df[df["index"] == "confidence"].index)
    df = df.set_index('city')
    df = df.drop(["index"], axis = 1) 

    return df