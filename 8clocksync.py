from datetime import datetime, timedelta

def berkeley_algo(server_time, time1, time2):
    print(f"Server Clock   = {server_time}")
    print(f"Client Clock1  = {time1}")
    print(f"Client Clock2  = {time2}")

    time_format = "%M:%S"
    
    try:
        # Parse the times
        server_time = datetime.strptime(server_time, time_format)
        t1 = datetime.strptime(time1, time_format)
        t2 = datetime.strptime(time2, time_format)

        # Calculate time differences
        st1 = (t1 - server_time).total_seconds()
        print(f"t1 - s = {st1:.0f}")

        st2 = (t2 - server_time).total_seconds()
        print(f"t2 - s = {st2:.0f}")

        # Calculate average time difference
        avg = (st1 + st2) / 2
        print(f"(st1 + st2) / 2 = {avg:.0f}")

        # Adjustments
        adj_server = server_time + timedelta(seconds=avg)
        adj_t1 = avg - st1
        adj_t2 = avg - st2

        print(f"t1 adjustment = {adj_t1:.0f}")
        print(f"t2 adjustment = {adj_t2:.0f}")

        # Adjusted clocks
        sync_server = adj_server.strftime(time_format)
        sync_client1 = (t1 + timedelta(seconds=adj_t1)).strftime(time_format)
        sync_client2 = (t2 + timedelta(seconds=adj_t2)).strftime(time_format)

        print(f"Synchronized Server Clock = {sync_server}")
        print(f"Synchronized Client1 Clock = {sync_client1}")
        print(f"Synchronized Client2 Clock = {sync_client2}")

    except ValueError as e:
        print("Error parsing time:", e)

def main():
    server_time = input("Enter Server Time (mm:ss): ")
    time1 = input("Enter Client 1 Time (mm:ss): ")
    time2 = input("Enter Client 2 Time (mm:ss): ")
    berkeley_algo(server_time, time1, time2)

if __name__ == "__main__":
    main()
