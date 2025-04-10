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
latestDict = {}
dictLabels = ('ID', 'Date', 'Time', 'Pm1p0', 'Pm2p5', 'Pm4p0', 'Pm10p0', 'Humidity', 'Temp', 'VocIndex', 'NoxIndex', 'CO2')
for i in range(len(latest)):
    latestDict[dictLabels[i]] = str(latest[i])

# Turn *that* into json
latestJson = json.dumps(latestDict, indent=4)
print(latestJson)