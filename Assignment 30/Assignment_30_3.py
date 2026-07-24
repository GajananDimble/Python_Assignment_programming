""" Writa a python Program that schedules a function to print
Coding Kar...!
Use:schedule.every(30).minutes.do(Name)

"""
import schedule
import time

def Name():
    print("Coding Kar...")

def main():
    schedule.every(30).minutes.do(Name)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()

# Expected Output:
# Coding Kar...!
# Coding Kar...!
# Coding Kar...!   