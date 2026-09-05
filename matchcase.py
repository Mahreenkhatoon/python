day = input("Enter the day: ")

match day:
    case "saturday" | "sunday":
        print("Weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case _:
        print("Invalid day")