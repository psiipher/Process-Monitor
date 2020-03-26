import psutil


def process_display():
    process_list = list()

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            process_list.append(proc.info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list


def main():
    print("\n\n\t\tProcess Monitor\n\n")

    processes = process_display()

    for item in processes:
        print(item)


if __name__ == "__main__":
    main()
