"""Schedule a task executs every five minutes:
The tas should write the current date and time into a file named:
Marvellous.txt
new Entire should be appended without removing previous entires

"""
import schedule
import time
import datetime

def WriteDateTime():
    CurrentTime=datetime.datetime.now()

    with open("Marvellous.txt","a") as file:
        file.write(f"Task Executed at:{CurrentTime} \n")

def main():
    print("Scheduler Started...")
    schedule.every(1).minutes.do(WriteDateTime)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()

# Expected Output:
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...    