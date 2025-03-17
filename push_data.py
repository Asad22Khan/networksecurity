import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
'''The certifi library in Python provides a bundle of trusted CA (Certificate Authority) root certificates. 
   It is mainly used to ensure that secure HTTPS requests can be properly verified using up-to-date CA certificates.
    
    ~ Why is certifi needed ?
    When making HTTPS requests (e.g., using requests, urllib, http.client, etc.), 
    Python needs a trusted Certificate Authority (CA) bundle to verify the server's SSL/TLS certificate. 
    certifi helps by providing an updated CA bundle that is maintained independently of the OS.

    '''
ca=certifi.where() # it knows that a valid request has been made.


'''The certifi.where() function returns the file path to the CA (Certificate Authority) bundle used by certifi.
    
    It tells Python where to find the trusted root certificates that are used to verify HTTPS connections.
    '''

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# this is my ETL function Class
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL)
                

            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="Asad"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)