""" Writa a python Program that Displays the current date and time
after every one minute

Use the date time module

"""
import schedule
import time
import datetime

def Name():
    print("Current Date And Time:",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(Name)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()

# Expected Output:
# Current Date And Time: 2026-07-23 10:50:12.187332
# Current Date And Time: 2026-07-23 10:51:12.196654