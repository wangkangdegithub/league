import pymysql
def connect_db(db):
    try:
        conn = pymysql.connect('localhost',user='root',password='root',db='英超',charset='utf8')
    except:
        conn = 400
    return conn


def get_data(db):
    conn = connect_db(db)
    if conn == 400:
        return conn
    else:
        try:
            cur = conn.cursor()
            cur.execute('use 英超')
            cur.execute('select * from new_df')
            data = cur.fetchall()
            cur.close()
            conn.commit()
            conn.close()
            return data
        except :
            return 401

data=get_data('英超')
print (data)

