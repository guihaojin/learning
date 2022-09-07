#!/usr/bin/env python
import os

import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user=os.environ['SNOWFLAKE_USERNAME'],
    password=os.environ['SNOWFLAKE_PASSWORD'],
    account=os.environ['SNOWFLAKE_ACCOUNT']
    )

cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])

    cs.execute("show warehouses")
    rows = cs.fetchall()
    print("warehouses:")
    print(rows)

    cs.execute("show databases")
    rows = cs.fetchall()
    print("databases:")
    print(rows)

    cs.execute("show roles")
    rows = cs.fetchall()
    print("roles:")
    print(rows)
finally:
    cs.close()
ctx.close()
