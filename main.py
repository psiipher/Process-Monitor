import mail
import log
import sys
import schedule
import time


def main():
    global from_id, to_id, password

    if len(sys.argv) != 2 :
        print("\nInvalid number of arguments. Try running with -h for help and -u for usage\n")
        sys.exit()
    
    if sys.argv[1] == '-h':
        print("\nPeriodic Process Logger with Auto Scheduled Log Report Facility.\n")
        sys.exit()
    elif sys.argv[1] == '-u':
        print("\nUsage: python3 main.py absolute_path_of_directory\n")
        sys.exit()

    from_id, to_id, password = mail.get_credentials()

    enable_sch = input("\nDo you want to schedule this process to repeat after for some fixed time interval? [y/n]:\t")
    if enable_sch.lower() == 'y':
        try:
            interval = int(input("\nEnter the time interval in minutes (Eg: 5):\t"))
            schedule.every(interval).minutes.do(execute)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except ValueError:
            print("\nError: Invalid datatype of input\n")
        except Exception as E:
            print("\nError: Invalid input\n", E)

    elif enable_sch.lower() == 'n':
        execute()

    else:
        print("\nNot a valid input\n")
        sys.exit()


def execute():
    log_path = log.file_write(sys.argv[1])
    if mail.check_connection():
        start = time.time()
        mail.send_mail(log_path, time.ctime(),from_id, to_id, password)
        end = time.time()
        print(f"\nTime taken to send mail {end - start}\n")

    else:
        print("\n\nThere is no internet connection!!!!\n\n")


if __name__ == "__main__":
    main()






        

