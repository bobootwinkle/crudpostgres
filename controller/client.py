# หาไฟล์ไม่เจอ เพราะอยู่คนละที่ + ใส่ path เต็มก็ไม่เจอ
# import service.connectpostgres as db
# import basicpython.crudpostgres.service.connectpostgres as db

import sys
# ถอย 1 step ใส่ 1
sys.path.insert(1, 'service')
import connectpostgres as condb

#insert into person
def insert(fullname,email,age):
    conn = condb.connectdb()
    cursor = conn.cursor();
    sql = "INSERT INTO person (fullname,email,age) VALUES(%s,%s,%s)"
    cursor.execute(sql, (fullname,email,age))
    conn.commit()
    cursor.close()

#select all data
def selectall():
    conn = condb.connectdb()
    cursor = conn.cursor()
    sql = "SELECT * FROM person"
    cursor.execute(sql)
    result = cursor.fetchall()
    rows = []
    for data in result:
        rows.append(data)
    cursor.close()
    return rows

#select by id
def selectbyid(id):
    conn = condb.connectdb()
    cursor = conn.cursor()
    sql = "SELECT * FROM person WHERE id = %s"
    result=cursor.execute(sql, (id,))
    rows = []
    for data in result:
        rows.append(data)
    cursor.close()
    return rows

#update by id
def updatebyid(id,fullname,email,age):
    conn = condb.connectdb()
    cursor = conn.cursor()
    sql = "UPDATE person SET fullname = %s, email = %s, age = %s WHERE id = %s"
    cursor.execute(sql, (fullname,email,age,id))
    conn.commit()
    cursor.close()

#delete by id
def deletebyid(id):
    conn = condb.connectdb()
    cursor = conn.cursor()
    sql = "DELETE FROM person WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()