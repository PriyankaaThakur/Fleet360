import sqlite3
import os
path = os.path.join(os.getcwd(), 'db.sqlite3')
print('DB PATH:', path)
print('EXISTS:', os.path.exists(path))
conn = sqlite3.connect(path)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
tables = [r[0] for r in cur.fetchall()]
print('TABLES:', tables)
checks = ['aircraft_search','faa_registry_raw','boeing_orders_deliveries','boeing_cmo_2025','boeing_airport_planning','airbus_gmf_2025_2044','airbus_orders_deliveries','airbus_orders_deliveries_archive','opensky_aircraft_database','opensky_aircraft_sample','opensky_state_vectors_sample']
for table in checks:
    try:
        cur.execute(f'SELECT count(*) FROM "{table}"')
        print(table, cur.fetchone()[0])
    except Exception as e:
        print(table, 'ERROR', e)
conn.close()
