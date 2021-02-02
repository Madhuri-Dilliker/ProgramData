# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:23:06 2021

@author: Madhuri
"""

#https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

#https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/
#!pip install gspread oauth2client
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_data.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("API-Programs-test").sheet1


# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)


# get all the records of the data
records_data = sheet.get_all_records()


# view the data
records_data

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
records_df.head()