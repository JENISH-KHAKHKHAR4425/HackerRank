import schedule
import time as tm 
from datetime import time, timedelta, datetime

def job():
    print("Hello! I'm Jenish P. Khakhkhar")
    

schedule.every(5).seconds.do(job)


while True:
    schedule.run_pending()
    tm.sleep(1)