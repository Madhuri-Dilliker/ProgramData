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
final_program_df= pd.DataFrame()

#defining the id parameter
id1='a013t000014wJIMAA2'
id2='a013t000014wJIMAA2'

#function to merge dataframes
def merge_function (dataframe1,key1,dataframe2,key2):
    if (key1== key2):  
      final_program_df=pd.merge(dataframe1, dataframe2, how = 'left',left_on='Id1', right_on ='Id2')
      print("merged dataframe", final_program_df)
      return final_program_df

#calling the merge function
final_program_df= merge_function(program_df1,id1,program_df2,id2)

#checking the merge data for given id
data=final_program_df.loc[final_program_df['Id1']== id1]
print("data", data)