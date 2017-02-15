import sqlite3
#connection = sqlite3.connect("D:/Sqlite3/test.db")
connection = sqlite3.connect(":memory:")
vcursor = connection.cursor()
vcursor.execute("SELECT DATE('NOW'),DATE('sysdate')")
#connection.commit()
for vdate in vcursor.fetchall() :
    print(vdate)
connection.close()


#execute()--执行sql语句   
#executemany--执行多条sql语句   
#close()--关闭游标   
#fetchone()--从结果中取一条记录，并将游标指向下一条记录   
#fetchmany()--从结果中取多条记录   
#fetchall()--从结果中取出所有记录   
#scroll()--游标滚动  