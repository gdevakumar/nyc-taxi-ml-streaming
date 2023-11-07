
import urllib.request
import sys
import argparse
import json

# take date input from terminal
date = input("Enter date in YYYY-MM-DD format: ")

try: 
  ResultBytes = urllib.request.urlopen(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/new%20york%2C%20ny/{date}/{date}?unitGroup=us&include=hours&key=43JDXYR6FQXX9GG5PTUB3SZDK&contentType=json")  
  # Parse the results as JSON
  jsonData = json.load(ResultBytes)

  dates = jsonData['days'][0]['hours']
  for date in dates:
      print(f"datime={date['datetime']}, temp={date['temp']}, humidity={date['humidity']}, visibility={date['visibility']}")


#   print(jsonData['days'][0]['hours'][0]['temp'])
        
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()