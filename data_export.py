#-*- coding:utf-8 -*-
import pandas as pd
import sys
from sqlalchemy import create_engine, MetaData, Table, select

SERVER_NAME = "127.0.0.1"
DATABASE="test"
TABLE_NAME="test"


engine = create_engine('mysql+mysqldb://root:123456@localhost/test')
conn = engine.connect()

metadata = MetaData(conn)

# 查询表
tbl = Table(TABLE_NAME,metadata,autoload=True, schema="test")

# select
sql = tbl.select()

# 执行SQL
result = conn.execute(sql)

# save to dataFrame
df = pd.DataFrame(data=list(result), columns=result.keys())

# close conn
conn.close()

df.to_csv('table.csv', index=False)
df.to_excel('table.xls', index=False)
df.to_csv('table.txt', index=False)