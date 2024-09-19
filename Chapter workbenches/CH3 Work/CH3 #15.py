def convert_seconds(seconds):
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400
    
    days = seconds // SECONDS_IN_DAY
    seconds %= SECONDS_IN_DAY

    hours = seconds // SECONDS_IN_HOUR
    seconds %= SECONDS_IN_HOUR

    minutes = seconds // SECONDS_IN_MINUTE
    seconds %= SECONDS_IN_MINUTE

    return days, hours, minutes, seconds

def main():
    total_seconds = int(input("Enter the number of seconds: "))

    if total_seconds < 0:
        print("Error")
        return

    days, hours, minutes, seconds = convert_seconds(total_seconds)


    print(total_seconds, "seconds is equivalent to: ", days ,"days", hours, "hours", minutes, "minutes,", seconds, "seconds.")



main()
