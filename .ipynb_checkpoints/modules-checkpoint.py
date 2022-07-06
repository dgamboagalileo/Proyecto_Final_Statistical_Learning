def getNanColNames(dataset):
    colnames=dataset.columns
    cols_con_na=[]
    for col in colnames:
        if((dataset[col].isnull().sum()>0) and ((dataset[col].dtypes == 'int64') or (dataset[col].dtypes == 'float64'))):
            cols_con_na.append(col)
    return cols_con_na