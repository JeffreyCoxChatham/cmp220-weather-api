import sqlite3

def makePrediction():
    con = sqlite3.connect("sample-db.db")
    cur = con.cursor()
    
    try:
        lastID = cur.execute("""
            SELECT ID
            FROM predictions
            ORDER BY ID DESC
            LIMIT 1
        """).__next__()[0]
    except:
        lastID = -1
    
    try:
        lastEntry = cur.execute("""
            SELECT ID, Time, Pm1p0, Pm2p5, Pm4p0, Pm10p0, Humidity, Temp, VocIndex, NoxIndex, CO2
            FROM records
            ORDER BY Time DESC
            LIMIT 1
        """).__next__()
    except:
        lastEntry = (0, 20250326, 1.1, 1.1, 1.1, 1.1, 32.91, 26.37, 103.00, 1.00, 423)
    
    newID = int(lastID) + 1
    newTime = int(lastEntry[1]) + 1
    newPm1p0 = lastEntry[2]
    newPm2p5 = lastEntry[3]
    newPm4p0 = lastEntry[4]
    newPm10p0 = lastEntry[5]
    newHumidity = lastEntry[6]
    newTemp = lastEntry[7]
    newVocIndex = lastEntry[8]
    newNoxIndex = lastEntry[9]
    newCO2 = lastEntry[10]
    
    cur.execute(f"""
        INSERT INTO predictions VALUES
        ({newID}, {newTime}, {newPm1p0}, {newPm2p5}, {newPm4p0}, {newPm10p0}, {newHumidity}, {newTemp}, {newVocIndex}, {newNoxIndex}, {newCO2})
    """)
    
    con.commit()
    
    return (newID, newTime)