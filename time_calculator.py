from datetime import datetime, timedelta
import re

def add_time(start, duration, day = ""):
  new_time = ""
  week_days = ("", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
  capitalized_day = day.capitalize()
  day_index = week_days.index(capitalized_day)
  splitted_duration = duration.split(":")
  converted_start = datetime.strftime(datetime.strptime(start, "%I:%M %p"), "%H:%M")
  splitted_converted_start = converted_start.split(":")

  time_sum = timedelta(
    days=1,
    minutes = int(splitted_converted_start[1]) + int(splitted_duration[1]),
    hours = int(splitted_converted_start[0]) + int(splitted_duration[0]),
  )

  if day:
    for _ in range(1, time_sum.days):
      day_index += 1
      if day_index > 7:
        day_index = 1

  formatted_time_sum = datetime.strptime(re.sub("[ day| days]", "", str(time_sum)), f'%d,%H:%M:%S')
  final_time = datetime.strftime(formatted_time_sum, '%I:%M %p')[:2].replace("0", "") + datetime.strftime(formatted_time_sum, '%I:%M %p')[2:]
  
  if day and time_sum.days == 1:
    new_time = final_time + ", " + capitalized_day
  elif time_sum.days == 2 and day != "":
    new_time = final_time + ", " + week_days[day_index] + " (next day)"
  elif time_sum.days == 2 and day == "":
    new_time = final_time + " (next day)"
  elif day and time_sum.days > 2:
    new_time = final_time + ", " + week_days[day_index] + f" ({time_sum.days - 1} days later)"
  elif time_sum.days > 2:
    new_time = final_time + f" ({time_sum.days - 1} days later)"
  else:
    new_time = final_time
  return new_time