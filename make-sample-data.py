import sqlite3

con = sqlite3.connect("sample-db.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO records VALUES
    (1, '20250326', '0000', 5, 'NORTH', 5, 74),
    (2, '20250326', '0100', 6, 'SOUTH', 6, 75)
""")

con.commit()