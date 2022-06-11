
from os import lseek
import psycopg2
import logging
import json

class postgresConnection:
    def __init__(self,dbname,user,password,host,port,table):
        self.dbname=dbname
        self.user=user
        self.password=password
        self.port=port
        self.host=host
        self.table=table


    def databaseConnection(self):
        #This method creates connection to postgresql and creates table if not exist
        conn=None
        try:
            conn = psycopg2.connect(dbname=self.dbname,user=self.user,password=self.password,host=self.host) 
        except (Exception,psycopg2.DatabaseError) as e:
                logging.debug(e) 
        cur= conn.cursor()    
        #creating table
        try:
            querry="CREATE TABLE IF NOT EXISTS %s(name varchar(30),phone_number integer primary key NOT NULL,spam_count integer,email varchar(20),isregistered bool)" %(self.table)
            cur.execute(querry)
            conn.commit()
        except Exception as e:
            logging.debug(e)
        
        return conn

def main():
    file=open('credentials.json','r')
    json_obj=json.load(file)
    dbname=json_obj['dbname']
    user=json_obj['user']
    password=json_obj['password']
    host=json_obj['host']
    port=json_obj['port']
    table=json_obj['table']
    pc=postgresConnection(dbname,user,password,host,port,table)
    print(pc.databaseConnection())
    
if __name__=="__main__":
    main()