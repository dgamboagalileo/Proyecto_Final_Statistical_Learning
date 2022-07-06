import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class NumericalImputerOperator(BaseEstimator, TransformerMixin):
    def __init__(self, imputerType='mean', varNames=None):
        if(imputerType=='mean'):
            self.imputerType='mean'
        elif(imputerType=='median'):
            self.imputerType='median'
        else:
            print("Mecanismo de imputación invalido.")
            
    def fit(self):
        return self
    
    def transform(self, X, y=None):
        X=X.copy()
        for col in self.varNames:
            if(self.imputerType=='mean'):
                imputerValue=np.round(X[col].mean(),0)
            else:
                imputerValue=np.round(X[col].median(),0)
            X[col].fillna(imputerValue)
        return X
            