import sqlite3

connection = sqlite3.connect('database.db')

with open('utilities/plan_table_scheme.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO plans (name, validity, operator, type, amount, description, circle_name, extra, benefits)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Popular', '56 days', 'Jio', '1', '598',
             'Data at high speed (Post which unlimited @ 64 Kbps)', 'All', '', '')
            )

cur.execute("INSERT INTO plans (name, validity, operator, type, amount, description, circle_name, extra, benefits)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Popular', '56 days', 'Airtel', '1', '599',
             'Data at high speed (Post which unlimited @ 64 Kbps)', 'All', '', '')
            )

cur.execute("INSERT INTO plans (name, validity, operator, type, amount, description, circle_name, extra, benefits)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Popular', '56 days', 'Airtel', '1', '599',
             'Data at high speed (Post which unlimited @ 64 Kbps)', 'Maharastra', '', '')
            )

connection.commit()
connection.close()
