#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:51:37 2019

@author: christopherdevairakkam
"""

# importing libararies 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

# Read the dataset
dataset = pd.read_csv('Data.csv');

# slice the independant part of the matrix
X=dataset.iloc[:,:-1].values;
X = pd.DataFrame(X)

# Slice the dependant part 

y = dataset.iloc[:,3].values;
y=pd.DataFrame(y);


# imputing missing values 
from sklearn.preprocessing import Imputer 

imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)

imputer = imputer.fit(X.iloc[:,1:3].values)
X.iloc[:,1:3]=imputer.transform(X.iloc[:,1:3].values)

#encoding catergorical data 

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder()
X.iloc[:,0]=labelencoder_x.fit_transform(X.iloc[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y=labelencoder_y.fit_transform(y)

