# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:13:12 2022
@author: akhil
"""

#importing libraries to handeling the dataset
import numpy as np
import pandas as pd

#import the tabulate library to generate the graphs
from tabulate import tabulate

#importing libraries to visualize the graph 
import matplotlib.pyplot as plt
import seaborn as sbn



#create object to store the dataset in the dataframe using pandas library
data_f1 = pd.read_csv("dataSet.csv", skiprows = 3)

#create an object and modify the dataset 
data_f = data_f1.drop(columns = ["1960","1961","1962","1963","1964",'1965',"1966","1967","1968",'1969',"1970",'1971',"1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993",'1994',"1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"])

#using drop function to remove unwanted data 
data_f = data_f.drop(columns = ["Unnamed: 66"])



#using isnull fucntion to find the null values in the data and count the total number of null values. 
total_null_values = data_f.isnull().sum()

#fillna fuction use for handel the null values in the data set  
data_f = data_f.fillna(0)

#again using isnull function and sum function to know that above code was work properly or not. 
notnull_values = data_f.isnull().sum()

#describe function use to describe the dataset 
stats = data_f.describe()

#copy data to modify it and for generating the desired result
df1 = data_f.copy()

#change the index usnig set_index function
df1.set_index("Indicator Name",inplace = True)

#using loc fucntion to select the data in the indexing
df1 = df1.loc["Urban population"]

#drop some column with were not required in ploting the dataset
df1 = df1.drop(["Country Code","Indicator Code"],axis =1)

#select the dataframe to plot the selected data
df1 = df1.head(15)

#plot the dataframe 
df1.plot(x= "Country Name", y = ['2016', '2017', '2018', '2019', '2020', '2021'],kind = "bar",stacked=True,figsize = (8,5))
plt.title("Urban population")

#using show function to see the visualization
plt.show()

#store the data to modify it and generate different visual/graph
df2 = data_f

#remove unwanted columns from the dataframe
df2 = df2.drop(["Country Code","Indicator Code"],axis =1)

#Indicator Name set as index to select the particular rows 
df2.set_index("Indicator Name",inplace = True)

#select the data based on the Agriculture land 
df2 = df2.loc["Agricultural land (% of land area)"]
df2 = df2.reset_index(level = "Indicator Name")

#used groupby fucntion with sum function 
df2.groupby(["Country Name"]).sum()

#select 15 values in the dataframe to display the graph
df3 = df2.head(15)
df3.plot.bar(x= "Country Name",y = ['2016', '2017', '2018', '2019', '2020', '2021'],figsize = (15,5),edgecolor = "white")
plt.title("Agricultural land (% of land area)")
plt.show()

#store the data to modify it and generate different visual/graph
df3 = data_f
df3 = df3.drop(["Country Code","Indicator Code"],axis =1)

df3.set_index("Country Name",inplace = True)

#using loc fucntion to select the data in the indexing
df3 = df3.loc["Aruba"]
df3 = df3.reset_index(level = "Country Name")
df3.set_index("Indicator Name",inplace = True)

#using loc fucntion to select the data in the indexing
df3 = df3.loc[["Urban population","Agricultural land (% of land area)","Access to electricity (% of population)","CO2 emissions from liquid fuel consumption (kt)","Terrestrial and marine protected areas (% of total territorial area)"]]

df3=df3.drop(df3.columns[0], axis=1)
sbn.heatmap(df3,annot=True, fmt=".1f",linewidth=1)

#title function used to print title of the graphs
plt.title("Aruba")
plt.show()

#store the data to modify it and generate different visual/graph
df4 = data_f
df4 = df4.drop(["Country Code","Indicator Code"],axis =1)
df4.set_index("Indicator Name",inplace = True)
df4 = df4.loc["Forest area (% of land area)"]
df4 = df4.reset_index(level = "Indicator Name")

#select 15 values in the dataframe to display the graph
df4 = df4.head(15)

df4.set_index("Country Name",inplace = True)
df4 = df4.drop("2021",axis = 1)

df5=df4.drop(df4.columns[0], axis=1)
plt.title("Forest area (% of land area)")
sbn.set(rc = {'figure.figsize':(12,10)})
p1 = sbn.heatmap(df5,annot=True, fmt=".1f",linewidth=1)



"""In this function we used  to transpose the world bank data and set index and dropping some column
 which are not needed for plotting the data and has selected the data frame used to plot the data set"""                                 
def dataframeTranspose(data):

    #change the index using set_index function
    data.set_index("Indicator Name",inplace = True)
    
    #using loc fucntion to select the data in the indexing
    data = data.loc["Arable land (% of land area)"]
    
    #drop some column with were not required in ploting the dataset
    data = data.drop(["Country Code","Indicator Code"],axis =1)
    
    
    #select the dataframe to plot the selected data
    data = data.head(15)
    data = data.reset_index(drop = True)

    y = np.transpose(data)
    y.columns = y.iloc[0]
    y = y.drop(y.index[0])
    z = y.drop(y.index[5])
    return z

df5 = dataframeTranspose(data_f)

df5.plot(figsize = (9,9))
plt.legend(loc = 'center left',bbox_to_anchor=(1,0.5))
plt.title("Arable land (% of land area)")

df6 = data_f.copy()

#using loc fucntion to select the data in the indexing
df6 = df6.loc["Marine protected areas (% of territorial waters)"]

#drop some column with were not required in ploting the dataset
df6 = df6.drop(["Country Code","Indicator Code"],axis =1)

#select the dataframe to plot the selected data
df6 = df6.head(15)
df6 = df6.reset_index(drop = True)

#use transpose function to display graphs based on the years
y = np.transpose(df6)
y.columns = y.iloc[0]
y = y.drop(y.index[0])
df6 = y.drop(y.index[5])

df6.plot(figsize = (9,9))
plt.legend(loc = 'center left',bbox_to_anchor=(1,0.5))
plt.title("Marine protected areas (% of territorial waters)")
plt.show()

#copy data to modify it and for generating the desired result
df7 = data_f.copy()

#modify the data for generating table
df7 = df7.drop(["Country Code","Indicator Code"],axis =1)

#select the renewable energy to show the energy consumption of some counrties
df7 = df7.loc["Renewable energy consumption (% of total final energy consumption)"]
df7 = df7.reset_index(level = "Indicator Name")
df7.groupby(["Country Name"]).sum()

#drop function used to remove unwanted or irrelevant data from the dataframe 
df7 = df7.drop("2020",axis = 1)
df7 = df7.drop("2021",axis = 1)

#select 15 values in the dataframe to display the graph
df7 = df7.head(15)
df7 = df7.drop("Indicator Name",axis = 1)
df7 = df7.set_index("Country Name")


  
#called the tabulate function to see the table
print(tabulate(df7,headers = 'keys', tablefmt = 'fancy_grid')) 












