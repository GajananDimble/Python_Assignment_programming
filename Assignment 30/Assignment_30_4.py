""" Create a task that executs every day at 9:00 AM and Prints
Namaskar...
Use:schedule.every().day.at("09:00").do(Name)

"""
import schedule
import time

def Name():
    print("Namaskar...")

def main():
    schedule.every().day.at("09:00").do(Name)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()

# Expected Output:
# Namaskar    