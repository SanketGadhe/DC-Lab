import time

def main():
    cs = 0  # Critical section flag
    pro = 0  # Process count
    run = 5.0  # Time for which a process can run in the critical section
    t1 = time.time() - 5  # Initializing time to simulate the first critical section exit

    print("Press any key (except 'q') to enter a process:")
    print("Press 'q' at any time to exit.\n")

    while True:
        key = input("Press a key: ")  # Simulate keypress detection
        if key == 'q':  # Exit condition
            print("Exiting program.")
            break

        if cs != 0:  # Check if a process is in the critical section
            t2 = time.time()
            if t2 - t1 > run:  # Check if the time exceeds the allowed run time
                print(f"Process {pro - 1} exited critical section.")
                cs = 0

        if cs == 0:  # Enter critical section
            print(f"Process {pro} entered critical section.")
            cs = 1
            pro += 1
            t1 = time.time()
        else:  # Error if a process is already in the critical section
            print("Error: Another process is currently executing!")

if __name__ == "__main__":
    main()
