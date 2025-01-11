import os

if os.path.exists("hw_solution.db"):
    os.remove("hw_solution.db")
else:
    print("The file does not exist")

import sqlite3

db_name: str = "hw_solution.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS shopping (
        id INTEGER PRIMARY KEY,
        name TEXT,
        amount INTEGER NOT NULL
    )
''')
print("Table created.")

conn.commit()

cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''', ("Avocado", 5))

cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''', ("Milk", 2))

cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''', ("Bread", 3))

cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''', ("Chocolate", 8))

cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''', ("Bamba", 5))

cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''', ("Orange", 10))
print("Data inserted.")

conn.commit()

cursor.execute("SELECT * FROM shopping")
rows = cursor.fetchall()
print("\nData in 'shopping' table:")
for row in rows:
    print(tuple(row))

cursor.execute("SELECT * FROM shopping WHERE amount > 5")
rows = cursor.fetchmany(5)  # It would be better to use 'fetchall', but I wanted to see how it works :)
print("\nAmount > 5")
for row in rows:
    print(tuple(row))

cursor.execute("DELETE from shopping WHERE name like 'Orange'")
print("Data deleted.")

conn.commit()

cursor.execute("UPDATE shopping SET name = ? WHERE name LIKE ?",
               ('Bisli', 'Bamba'))
cursor.execute("UPDATE shopping SET amount = ? WHERE name LIKE ?",
               (1, 'Milk'))
print("Table updated.")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM shopping")
row = cursor.fetchone()
print(f"Count: {list(row)}")

cursor.execute("SELECT * FROM shopping WHERE id > 0")
rows = cursor.fetchmany(5)
print("\nid > 0")
for row in rows:
    print(tuple(row))

conn.close()
