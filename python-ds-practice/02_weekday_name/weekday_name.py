def weekday_name(day_of_week):
    if day_of_week == 1:
        return "Sunday"
    elif day_of_week == 2:
        return "Monday"
    elif day_of_week == 3:
        return "Tuesday"
    elif day_of_week == 4:
        return "Wednesday"
    elif day_of_week == 5:
        return "Thursday"
    elif day_of_week == 6:
        return "Friday"
    elif day_of_week == 7:
        return "Saturday"
    else:
        return "None"

print("The day is", weekday_name(1))
print("The day is", weekday_name(7))
print("The day is", weekday_name(9))
print("The day is", weekday_name(0))



   