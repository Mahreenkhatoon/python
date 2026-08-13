import datetime
import geocoder

# 1. Display current date and time

now = datetime.datetime.now()
print("Current Date and Time:", now)

# 2. Display current date

today = datetime.date.today()
print("Current Date:", today)

# 3. Display current time

current_time = datetime.datetime.now().time()
print("Current Time:", current_time)

# 4. Create a specific date

d = datetime.date(2026, 8, 12)
print("Specific Date:", d)

# 5. Format date and time

print("Formatted Date:", now.strftime("%d-%m-%Y"))
print("Formatted Time:", now.strftime("%H:%M:%S"))

# 6. Subtract days

past_date = today - datetime.timedelta(days=10)
print("Date before 10 days:", past_date)

# 7. Difference between two dates

date1 = datetime.date(2026, 8, 12)
date2 = datetime.date(2026, 8, 20)

difference = date2 - date1
print("Difference between dates:", difference.days, "days")

# 8. Get current location using Geocoder

g = geocoder.ip("me")

print("\nCurrent Location")

if g.ok:
    print("City:", g.city)
    print("State:", g.state)
    print("Country:", g.country)
    print("Latitude:", g.lat)
    print("Longitude:", g.lng)
else:
    print("Unable to find current location")