def convert(time_str):
    # extract the hour and minute from the time string
    hour, minute = map(int, time_str.split(":"))
    # convert the time to a floating-point number of hours
    return hour + minute / 60

def main():
    time_str = input("What time is it?")
    time = convert(time_str)

    if time >= 7 and time < 8:
        meal_time = "breakfast time"
    elif time >= 12 and time < 13:
        meal_time = "lunch time"
    elif time >= 18 and time < 19:
        meal_time = "dinner time"
    else:
        # if it's not time for a meal, don't output anything
        return

    print(meal_time)

if __name__ == "__main__":
    main()