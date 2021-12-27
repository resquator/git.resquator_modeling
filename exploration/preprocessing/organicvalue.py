from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import random


class OrganicValue(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_ = X.copy()
        modified_column=[]
        for i in range(0,len(X_)):
            modified_column.append([random.random()*(i**2)+4])

        X_ = np.append(X_, modified_column, axis=1)
        return X_

