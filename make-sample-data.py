import sqlite3

con = sqlite3.connect("sample-db.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO records VALUES
    (0, 20250326, 0000, 1.1, 1.1, 1.1, 1.1, 32.91, 26.37, 103.00, 1.00, 423),
    (1, 20250326, 0100, 1.1, 1.1, 1.1, 1.1, 32.91, 26.37, 103.00, 1.00, 423)
""")

con.commit()