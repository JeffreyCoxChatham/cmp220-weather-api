import sqlite3
import json
from http.server import BaseHTTPRequestHandler

class WeatherDataRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # /records/173856239 -> records with timestamp
        # /predictions/57363464356 -> predictions with timestamp
        # /records/latest -> records with latest
        # /predictions/latest -> predictions with latest
        # /latest -> records with latest
        if self.path.lower().startswith("/records/") or self.path.lower().startswith("/predictions/"):
            sheet = self.path.lower().split("/")[1]
            time = self.path.lower().split("/")[2]
            if time == "latest":
                response = self.getEntry(sheet, "latest")
            else:
                try:
                    time = int(time)
                except:
                    response = ["Invalid query: provided timestamp must be an integer or 'latest'!", "error"]
                else:
                    response = self.getEntry(sheet, time)
        elif self.path.lower().startswith("/latest"):
            response = self.getEntry("records", "latest")
        else:
            response = ["Invalid query: malformed path!", "error"]
        
        if response[1] == "json":
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()
            self.wfile.write(response[0].encode("utf-8"))
        elif response[1] == "error":
            self.send_response(400)
            self.send_header("Content-type", "text")
            self.end_headers()
            self.wfile.write(response[0].encode("utf-8"))
        elif response[1] == "html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(response[0].encode("utf-8"))
        else:
            self.send_response(500)
            self.send_header("Content-type", "text")
            self.end_headers()
            self.wfile.write("Unknown error!".encode("utf-8"))
    
    # get a specified entry based on a timestamp and a sheet. returns a json dump
    def getEntry(self, sheet, time):
        con = sqlite3.connect("AirQualityReadings.db")
        cur = con.cursor()
        
        try:
            if time == "latest":
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
        except:
            return ["Invalid query: SQL error!", "error"]
        
        entryDict = {}
        dictLabels = ("ID", "Time", "Pm1p0", "Pm2p5", "Pm4p0", "Pm10p0", "Humidity", "Temp", "VocIndex", "NoxIndex", "CO2")
        for i in range(len(entry)):
            entryDict[dictLabels[i]] = str(entry[i])
        entryDict["Sheet"] = sheet
        entryJson = json.dumps(entryDict, indent=4)
        
        return [entryJson, "json"]