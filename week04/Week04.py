
1. SELECT * FROM data;

pandas:

import pandas as pd 
excel1 = pd.read_excel(r'data.xlsx')
pd.read_excel(r'data.xlsx', sheet_name = 0)
pd.read_csv(r'c:\data.csv', sep=' ', nrow = 10, encoding = 'utf-8')
pd.read_table( r'data.txt' , sep = ' ')

pandas and pymysql:

import pymysql:
sql = 'SELECT * FROM data'
conn = pymysql.connect('id','name','age','charset=utf-8')
df = pd.read_sql(sql,conn)


2. SELECT * FROM data LIMIT 10;

import pandas as pd 
excel1 = pd.read_excel(r'data.xlsx')
excel1 = pd.read_csv(r'c:\data.csv', sep=' ', nrow = 10, encoding = 'utf-8')

import pymysql:
sql = 'SELECT * FROM data LIMIT 10'
conn = pymysql.connect('id','name','age','charset=utf-8')
df = pd.read_sql(sql,conn)


3. SELECT id FROM data;  //id 是 data 表的特定一列


import pandas as pd 
excel1 = pd.read_excel(r'data.xlsx')

idcolum = excel1['id']


import pymysql:
sql = 'SELECT id FROM data'
conn = pymysql.connect('id','name','age','charset=utf-8')
df = pd.read_sql(sql,conn)


4. SELECT COUNT(id) FROM data;

import pandas as pd 
excel1 = pd.read_excel(r'data.xlsx')

counts = excel1.count()


import pymysql:
sql = 'SELECT COUNT(id) FROM data'
conn = pymysql.connect('id','name','age','charset=utf-8')
df = pd.read_sql(sql,conn)


5. SELECT * FROM data WHERE id<1000 AND age>30;

import pandas as pd 
excel1 = pd.read_excel(r'data.xlsx')

excel1[(excel1["id"]<1000) & (excel1["age"]>30)]


import pymysql:
sql = 'SELECT * FROM data WHERE id<1000 AND age>30'
conn = pymysql.connect('id','name','age','charset=utf-8')
df = pd.read_sql(sql,conn)


6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

import pandas as pd 
table1 = pd.read_excel(r'data.xlsx')


table1['order_id'] = table1.sort_values(by=['id'])
table1['count_id'] = table1['order_id'].count()
sep1 = table1.groupby(‘id’)
res = sep1['id','count_id']

import pymysql:
sql = 'SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id'
conn = pymysql.connect('id','name','age','order_id','charset=utf-8')
df = pd.read_sql(sql,conn)


7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

import pymysql:
sql = 'SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id'
conn = pymysql.connect('id','name','age','order_id','charset=utf-8')
df = pd.read_sql(sql,conn)


8. SELECT * FROM table1 UNION SELECT * FROM table2;

import pymysql:
sql = 'SELECT * FROM table1 UNION SELECT * FROM table2'
conn = pymysql.connect('id','name','age','order_id','charset=utf-8')
df = pd.read_sql(sql,conn)


9. DELETE FROM table1 WHERE id=10;

import pymysql:
sql = 'DELETE FROM table1 WHERE id=10'
conn = pymysql.connect('id','name','age','order_id','charset=utf-8')
df = pd.read_sql(sql,conn)



10. ALTER TABLE table1 DROP COLUMN column_name;

import pymysql:
sql = 'ALTER TABLE table1 DROP COLUMN column_name'
conn = pymysql.connect('id','name','age','order_id','charset=utf-8')
df = pd.read_sql(sql,conn)




