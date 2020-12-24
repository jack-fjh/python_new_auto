import  pymysql

def conn_database():
    db=pymysql.connect('tripdb.saicmuat.local','saic_test','Sit_saic_test181030','saic_trip_order')
    cursor=db.cursor()
    cursor.execute("select status from saic_trip_order.t_order where status='91' limit 1")
    data=cursor.fetchone()
    print('status:',)
    cursor.close()
    db.close()

conn_database()