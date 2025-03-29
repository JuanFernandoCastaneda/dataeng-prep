import requests
import schedule 
import time 
import sqlite3

# TODO: add the new results of the request to the db.

url = "https://tenders.guru/api/hu/tenders"
def request():
    response = requests.get(url)
    with sqlite3.connect('tenders.sqlite') as conn:
        pass

request()
schedule.every(1).hours.do(request) 
  
while True: 
    schedule.run_pending() 
    time.sleep(1)

