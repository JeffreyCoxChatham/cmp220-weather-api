import sqlite3
import json
from http.server import BaseHTTPRequestHandler

class WeatherDataRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # /records/173856239/data.json -> records with timestamp
        # /predictions/57363464356/data.json -> predictions with timestamp
        # /records/latest/data.json -> records with latest
        # /predictions/latest/data.json -> predictions with latest
        # /latest/data.json -> records with latest
        response = self.do_entry('latest', 'records')
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
    
    
    # get a specified entry based on a timestamp and a sheet. returns a json dump
    def do_entry(self, time, sheet):
        con = sqlite3.connect("sample-db.db")
        cur = con.cursor()
        
        if time == 'latest':
            entry = cur.execute(f"""
                SELECT ID, Time, Pm1p0, Pm2p5, Pm4p0, Pm10p0, Humidity, Temp, VocIndex, NoxIndex, CO2
                FROM {sheet}
                ORDER BY Time DESC
                LIMIT 1
            """).__next__()
        else:
            entry = cur.execute(f"""
                SELECT ID, Time, Pm1p0, Pm2p5, Pm4p0, Pm10p0, Humidity, Temp, VocIndex, NoxIndex, CO2
                FROM {sheet}
                WHERE Time={time}
            """).__next__()
        
        entryDict = {}
        dictLabels = ('ID', 'Time', 'Pm1p0', 'Pm2p5', 'Pm4p0', 'Pm10p0', 'Humidity', 'Temp', 'VocIndex', 'NoxIndex', 'CO2')
        for i in range(len(entry)):
            entryDict[dictLabels[i]] = str(entry[i])
        entryJson = json.dumps(entryDict, indent=4)
        
        return entryJson