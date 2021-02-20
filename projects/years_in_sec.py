age = int(input("Enter age in years: "))

age_in_months = age*12
age_in_days = age*365.25 # There are 365.25 days in a year.
secs_in_a_day = 1*24*60*60

age_in_secs = secs_in_a_day * age_in_days

print(f"You are {age_in_secs} seconds years old")

