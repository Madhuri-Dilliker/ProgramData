# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:37:39 2021

@author: Madhuri
"""

#https://towardsdatascience.com/using-python-to-get-salesforce-data-97bb5a7ef2cf
#https://www.oktana.com/python-and-salesforce/


#importing the libary
#!pip install simple_salesforce
import pandas as pd 
from simple_salesforce import Salesforce

#salesforce credentials
sf = Salesforce(
username='karthik@getreadyguilford.com', 
password='RRDevOrg!156', 
security_token='mOIMDBLw8w09HKqd69vQdSwO')

#soql query to extract data from child object
SOQL="SELECT Date_of_Birth__c,First_Name__c,HSC_Gender__c,Last_Name__c,Test_number__c FROM Child__c"

#SOQL code is put into the method and extract it to a variable, resulting in json data
sf_data = sf.query(SOQL)

#converting json data to pandas dataframe
sf_df = pd.DataFrame(sf_data['records']).drop(columns='attributes')

#printing the child data
print("salesforce data for child object",sf_df)
