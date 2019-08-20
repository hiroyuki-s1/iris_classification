import sys
import pandas as pd
import matplotlib
import numpy as np
import scipy as sp
import IPython
import sklearn
from sklearn.datasets import load_iris

iris_dataset = load_iris()

print("key of iris dataset \n{} ".format(iris_dataset.keys()))

dict_keys(['target_names', 'feature_names', 'DESCR', 'data', 'target'])

print(iris_dataset['DESCR'][:193])

print("target names: {}".format(iris_dataset['target_names']))