# -*- coding: utf-8 -*-
"""DAY_4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bFXf_n5BIxYlc0t_Nw6O2-mbWp2B8DLm
"""

import numpy as np #numpy is known as numeric values of python and to perform mathematical operations on arrays
import matplotlib.pyplot as plt #it is a collection of command style functions like creates a figure, creates a plotting area 
import pandas as pd # analysis toolkit which can be imported using import pandas as pd 
import seaborn as sns #It is used for data visualization and exploratory data analysis.

stockmarket_data = pd.Series(np.random.randn(500)) #Series is a one-dimensional labelled data structure which can hold data such as strings, integers and even other Python objects.
#np.random.rand creates an array of specified shape and fills it with random values.

stockmarket_cumulative = stockmarket_data.cumsum() #used to find the cumulative sum value over any axis.

stockmarket_cumulative.plot() #cumulative plot is a way to draw cumulative information graphically

stock_prices = pd.DataFrame(np.random.randn(500, 5)) #A Pandas DataFrame is a 2 dimensional data structure  table with rows and columns

stock_prices

stock_prices.columns = ['India', 'Pakistan', 'Bhutan','America','china'] #5 columns starting with index 0 to 4

stock_prices

stock_prices.index = pd.date_range('19/6/2021', periods=500) # used to return a fixed frequency DatetimeIndex.

stock_prices

stock_prices.to_csv('stock.csv')

stock_prices_cumulative = stock_prices.cumsum()

stock_prices_cumulative.plot()

!wget https://raw.githubusercontent.com/ckrihub/bridge-sessions/main/ToyotaCorolla.csv  #retrieves content from web servers.

car_data = pd.read_csv('ToyotaCorolla.csv') #used to load a CSV file as a pandas dataframe.

car_data.tail() #The tail() function is used to get the last n rows

car_data.head() #The head() function is used to get the first n rows

car_data.describe() #used for calculating some statistical data like percentile, mean and std of the numerical values of the Series or DataFrame

car_data.sort_values('Age', inplace=True) #arange in order

car_data

plt.hist(car_data['Age'], bins=10) #The hist() function in pyplot module of matplotlib library is used to plot a histogram.

sns.lmplot(x='Price', y='Age', data=car_data, hue='FuelType')  #used to draw a scatter plot

sns.pairplot(car_data, hue='Price') #creates a grid of Axes such that each variable in data will by shared in the y-axis across a single row and in the x-axis across a single column.