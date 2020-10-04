from django.test import TestCase
import pymysql

# Create your tests here.
def connection():
    try:
        db=pymysql.connect("localhost","root1","Sahil@19970","blogs" )
        cursor=db.cursor()
        return cursor
    except Exception as e:
        print("there is an exception in creating the cursor",e)

def dashboard():
        cursor=connection()
        cursor.execute("SELECT Title,id,date,description FROM posts ")
        results=cursor.fetchall()
        
        data=[]
        for i in range(len(results)):
           data.append(results[i])
        print(data[0])
dashboard()

# cursor.execute("SELECT Title,description,id,date FROM posts ")
#             results=cursor.fetchall()
#             results_page=[i for i in results]
            
#             id_s=[]
#             data=[]
#             for i in results:
#                 id_s.append(i[2])
#                 dict_data[i[2]]={i[3]:{i[0]:i[1][0:100]}}