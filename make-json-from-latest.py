import sqlite3
import json

con = sqlite3.connect("sample-db.db")
cur = con.cursor()

# for now assume this is a way to get the latest entry, as a tuple
latest = cur.execute("""
    SELECT ID, Date, Time, Pm1p0, Pm2p5, Pm4p0, Pm10p0, Humidity, Temp, VocIndex, NoxIndex, CO2
    FROM (
        SELECT ID, Date, Time, Pm1p0, Pm2p5, Pm4p0, Pm10p0, Humidity, Temp, VocIndex, NoxIndex, CO2
        FROM records
        WHERE (Date = 20250327)
    ) sub
    ORDER BY Time DESC
    LIMIT 1
""").__next__()
print(latest)

# Turn that tuple into a dict (so that each item has a label)
latestDict = {
    'ID': latest[0],
    'Date': latest[1],
    'Time': latest[2],
    'Pm1p0': latest[3],
    'Pm2p5': latest[4],
    'Pm4p0': latest[5],
    'Pm10p0': latest[6],
    'Humidity': latest[7],
    'Temp': latest[8],
    'VocIndex': latest[9],
    'NoxIndex': latest[10],
    'CO': latest[11]
}
print(latestDict)

# Turn *that* into json
latestJson = json.dumps(latestDict, indent=4)
print(latestJson)