# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:12:31 2021

@author: Madhuri
"""
import json
with open('Credential.json', 'rb') as data_file:    
    data = json.load(data_file)
    print(data)