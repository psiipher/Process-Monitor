import os
import time
import process


def file_write(_dir):
    if not os.path.exists(_dir):
        try:
            os.mkdir(_dir)
        except OSError as error:
            pass

    log_path = os.path.join(_dir, f"Log {time.ctime()}")
    f = open(log_path, 'w')
    f.write(f"\n\nProcess Log at {time.ctime()} \n\n")

    processes = process.process_display()
    for item in processes:
        f.write(f"{item}\n")

    print(f"\nLog file created successfully at {_dir}\n")
    return log_path

    


