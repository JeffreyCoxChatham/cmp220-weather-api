import sqlite3
from makePredictions import makePrediction

con = sqlite3.connect("AirQualityReadings.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO records VALUES
    (0, 20250326, 1.1, 1.1, 1.1, 1.1, 32.91, 26.37, 103.00, 1.00, 423),
    (1, 20250327, 1.2, 1.1, 1.1, 1.1, 32.91, 26.37, 103.00, 1.00, 423),
    (2, 20250328, 1.3, 1.1, 1.1, 1.1, 32.91, 26.37, 103.00, 1.00, 423),
    (3, 20250329, 1.4, 1.1, 1.1, 1.1, 32.91, 26.37, 103.00, 1.00, 423)
""")

con.commit()

makePrediction()