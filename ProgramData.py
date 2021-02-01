# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:12 2021

@author: Madhuri
"""
#create a function to merge two dataset
#1.loading the excel file
#2.Loading dataset present in different sheets in dataframes
#3.Define merge function
#4.Call merge function
#5.Testing the function using key used as parameter


#importing python library
import pandas as pd

#loading the data from excel file
program_df = pd.ExcelFile('PythonProgrammingData.xlsx')

#Data is present in two different sheets loaing the data from in two different dataframes
program_df1 = program_df.parse(0)
program_df2= program_df.parse(1)

#defining the empty dataframe to store the merge data 
df_3= pd.DataFrame()



#function to merge dataframes
def merge_function (df1,key1,df2,key2):
      df_3 = df1.merge (df2, left_on = key1, right_on = key2)
      print("merged dataframe", df_3)
      return df_3
  
#calling the merge function
final_program_df1= merge_function(program_df1, 'Id1' , program_df2, 'Id2')

#checking the merge data for given id
#data=final_program_df.loc[final_program_df['Id1']== id1]
#print("data", data)

final_program_df1.to_excel (r'C:\Users\Madhuri\Documents\GitHub\ProgramData\final_program_df1.xlsx', index = False, header=True)
