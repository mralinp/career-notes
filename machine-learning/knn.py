import numpy as np


class KNN:
    
    def __init__(self, k):
        self.k = k
        
    def fit(self, x,y):
        self.X = x
        self.Y = y
    
    def predict(self, x):
        pass