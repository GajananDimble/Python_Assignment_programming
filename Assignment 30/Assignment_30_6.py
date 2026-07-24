""" Write a Script that schedules the following tasks
. print Lunch Time! every day at 1:00 PM
. print Wrap Up Work every day at 6:0 PM
Both tasks should be handled by separate function
"""
import schedule
import time

def LunchTime():
    print("Lunch Time")

def WrapUpWork():
    print("Wrap Up Work")    

def main():
    print("Schedular Started...")

    schedule.every().day.at("13:00").do(LunchTime)

    schedule.every().day.at("18:00").do(WrapUpWork)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()
