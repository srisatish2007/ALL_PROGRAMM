import pymysql

connection = pymysql.connect(host="localhost",user="root",password='SRI_ROOTPASS@"2007";',database="testpython")
cur= connection.cursor()
# cur.execute("insert into db values(31,'srisatish',1231,17,1234533330,70000000);")
# connection.commit()

cur.execute("select * from db;")
for i in range(0,3):
    re=cur.fetchone()
    print(re)