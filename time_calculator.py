def add_time(start, duration, startday=""):
  #what is changable? day, hour, minute, second-they need a house to stay
  #what i need? starting point and what we will add to that.
  #what can i do?use 24 hour for day or 60 for minutes and seconds and divide minutes to 60
  #pm and am also needed
  #calculate hour day minutes and than make a function to make them shown?
  #time 0 duration 1 day 2
    day = 0
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    start_hour = start.split(":")[0]
    start_minute = start.split(":")[1].split()[0]
    pmam = start.split(":")[1].split()[1]
    duration_hour = duration.split(":")[0]
    duration_minutes = duration.split(":")[1]

    #Calculation of the new hours and minutes
    hourresult = int(duration_hour) + int(start_hour)
    minuteresult = int(duration_minutes) + int(start_minute)
    pmamresult = pmam

    #adds extra minutes to new hour
    while minuteresult >= 60:
        minuteresult -=60
        hourresult +=1

    #adds extra hours to new day
    while hourresult >= 12:
        hourresult -= 12
        if pmamresult == "PM":
            pmamresult = "AM"
            day += 1
        else: 
            if pmamresult == "AM":
                pmamresult = "PM"
              
    #requested format
    if hourresult == 0:
        hourresult = 12

    if minuteresult < 10:
        new_time = str(hourresult) + ":" + "0" + str(minuteresult) + " " + pmamresult
    else:
        new_time = str(hourresult) + ":" + str(minuteresult) + " " + pmamresult
    
    if startday != "":
        startindex = days.index(startday.capitalize())
        new_day = days[(day + startindex) % 7]
        new_time += ", " + new_day

    if day == 1:
        new_time += " (next day)"
    else:
        if day > 1:
            new_time += " (" + str(day) + " days later)"
        
    return new_time
