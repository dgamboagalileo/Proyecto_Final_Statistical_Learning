import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler

##Imputación de variables numericas
class NumericalImputerOperator(BaseEstimator, TransformerMixin):
    def __init__(self, imputerType='mean', varNames=None):
        self.varNames = varNames
        if(imputerType == 'mean'):
            self.imputerType = 'mean'
        elif(imputerType == 'median'):
            self.imputerType = 'median'
        else:
            print("Mecanismo de imptación invalido.\n")
            
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y=None):
        X = X.copy()
        for col in self.varNames:
            if(self.imputerType == 'mean'):
                imputerValue = np.round(X[col].mean(), 0)
            else:
                imputerValue = np.round(X[col].median(), 0)
            X[col].fillna(imputerValue, inplace=True)
        return X
    

##Codificación de variables Categoricas  
class CategoricalEncoderOperator(BaseEstimator, TransformerMixin):
    def __init__(self, varNames=None):
        self.encoder_dict={}
        self.varNames=varNames

    def fit(self, X, y = None):
        for col in self.varNames:
            self.encoder_dict[col]=(X[col].value_counts().sort_values(ascending=False)).to_dict()
        return self

    def transform(self, X, y=None):     
        X = X.copy()
        for col in self.varNames:
            X[col]=X[col].map(self.encoder_dict[col])
        return X

##Tratamiento de Outliers y Capping
class OutliersTreatmentOperator(BaseEstimator, TransformerMixin):
    def __init__(self, factor=1.75, varNames=None):
        self.varNames=varNames
        self.factor=factor

    def fit(self, X, y = None):
        return self

    def transform(self, X, y=None):     
        X = X.copy()
        for col in self.varNames:
            q3=X[col].quantile(0.75)
            q1=X[col].quantile(0.25)
            self.IQR=q3-q1
            self.upper=q3 + self.factor*self.IQR
            self.lower=q1 - self.factor*self.IQR
            X[col]=np.where(X[col]>self.upper, self.upper,
                np.where(X[col]<self.lower, self.lower, X[col]))
        return X

##Transformación de variables numericas  
class NumericalTreatmentTransformation(BaseEstimator, TransformerMixin):
    def __init__(self, varNames=None):
        self.varNames=varNames

    def fit(self, X, y = None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        Xtemp=X.copy()
        for col in self.varNames:
            Xtemp[col], lambdaX=stats.yeojohnson(X[col])
            X[col]=Xtemp[col]
        return X

##Feature Scaling
class FeatureScaling(BaseEstimator, TransformerMixin):
    def __init__(self, varNames=None):
        self.varNames=varNames

    def fit(self, X, y = None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        Xtemp=X.loc[:,self.varNames]
        scaler=StandardScaler()
        scaler.fit(Xtemp) 
        dataset_temp_scaled=pd.DataFrame(scaler.transform(Xtemp),columns=Xtemp.columns)
        X.loc[:,self.varNames]=dataset_temp_scaled
        return X