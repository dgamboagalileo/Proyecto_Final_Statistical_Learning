def getNanColNames(df):
    colnames = df.columns
    nums_cols_na = []
    for col in colnames:
        if((df[col].isnull().sum() > 0) and ((df[col].dtypes == 'int64') or (df[col].dtypes == 'float64'))):
            nums_cols_na.append(col)
    return nums_cols_na

def getDtypes(dataset):
    """
    función para determinar el tipo de dato de cada columna dentro del Datasaet.
    """
    numeric_cols = []
    categoric_cols = []
    date_cols = []
    for col in dataset.columns:
        if(dataset[col].dtype == "object"):
            categoric_cols.append(col)
        elif((dataset[col].dtype == "int64") or (dataset[col].dtype == "float64")):
            numeric_cols.append(col)
        else:
            date_cols.append(col)
    return numeric_cols, categoric_cols, date_cols

def getContinuesCols(df):
    colnames=df.columns
    numeric_continues_vars=[]
    for col in colnames:
        unique_values=len(df[col].unique())
        if((df[col].dtype!="object")and(unique_values>30)):
            numeric_continues_vars.append(col)
    return numeric_continues_vars