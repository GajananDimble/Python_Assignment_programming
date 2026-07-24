""" Writa a python Program that prints:
Jay Ganesh...
Use:schedule.every(2).seconds.do(Name)

"""
import schedule
import time

def Name():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(Name)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()

# Expected Output:
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...    