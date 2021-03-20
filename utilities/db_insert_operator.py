import sqlite3

connection = sqlite3.connect('database.db')


with open('utilities/operator_table_scheme.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO operators (id, name, icon, status) VALUES (?, ?, ?, ?)",
            ('O-1', 'Jio', 'https://cdn.iconscout.com/icon/free/png-512/jio-2363161-1970123.png', '1')
            )

cur.execute("INSERT INTO operators (id, name, icon, status) VALUES (?, ?, ?, ?)",
            ('O-2', 'Airtel', 'https://s3-ap-southeast-1.amazonaws.com/bsy/iportal/images/airtel-logo1.png', '1')
            )

cur.execute("INSERT INTO operators (id, name, icon, status) VALUES (?, ?, ?, ?)",
            ('O-3', 'BSNL', 'https://s3-ap-southeast-1.amazonaws.com/bsy/iportal/images/airtel-logo1.png', '1')
            )

connection.commit()
connection.close()