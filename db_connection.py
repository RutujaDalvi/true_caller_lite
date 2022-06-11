import psycopg2
import logging
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
        cur=None
        try:
            conn = psycopg2.connect(dbname=self.dbname,user=self.user,password=self.password,host=self.host)
            print(conn) 
            cur= conn.cursor()
            #return conn,cur 
        except (Exception,psycopg2.DatabaseError) as e:
                logging.debug(e) 
        return conn,cur 

    def create_table(self,conn,cur):   
        #creating table
        try:
            querry="CREATE TABLE IF NOT EXISTS %s(name varchar(30),phone_number integer,email_address varchar(30),PRIMARY KEY(phone_number))" %(self.table)
            cur.execute(querry)
            conn.commit()
        except Exception as e:
            logging.debug(e)


def main():
    pc=postgresConnection("postgres","postgres","123","127.0.0.1",5432,"user_info")
    conn_req=pc.databaseConnection()
    print(conn_req)
    pc.create_table(conn_req[0],conn_req[1])

if __name__=="__main__":
    main()
