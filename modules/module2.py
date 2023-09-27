from random import randrange,randint
from datetime import datetime,date,timedelta

print("****Date time Library using***********")
current_date_time = datetime.now()
print("Today date & Time is:", current_date_time)
today = date.today()
print("Today date is:", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
current_time = current_date_time.time()  # Gives the time
print("Hour:",current_time.hour)
print("Minutes:",current_time.minute)
print("seconds:",current_time.second)
print("Micro seconds:",current_time.microsecond)
custom_date=date(2019, 4, 13)
print("Custom Date:",custom_date)
'''A Unix timestamp is the number of seconds between a particular
date and January 1, 1970 at UTC'''
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)
# Calculating future dates 
# for one year 
future_date_after_1yr = current_date_time + timedelta(days = 365) 
#for 4 days and time
future_date_after_4days = current_date_time + timedelta(days = 4,hours = 5, minutes = 4, seconds = 54) 

# printing calculated future_dates 
print('future_date_after_1yr:', future_date_after_1yr) 
print('future_date_after_4days:', future_date_after_4days)
print("Type is:",type(future_date_after_4days))
#convert string
future_date_after_1yr_str=str(future_date_after_1yr)
future_date_after_4days_str=str(future_date_after_4days)

print('future_date_after_1yr:', future_date_after_1yr_str)
print('future_date_after_4days:', future_date_after_4days_str)
print("Type is:",type(future_date_after_4days_str))

# Calculating past dates 
# for one years 
past_date_before_1yr = current_date_time - timedelta(days = 365) 

# for two hours 
past_date_before_2hours = current_date_time - timedelta(days=2,hours = 2) 


# printing calculated past_dates 
print('past_date_before_1yr:', past_date_before_1yr)
print('past_date_after_2days:', past_date_before_2hours)

# strftime function is used to convert the date time object as string
str_conv_date=current_date_time.strftime("%d/%m/%Y")
print("str_conv_date:", str_conv_date)
str_conv_time=current_date_time.strftime("%H:%M:%S")
print("str_conv_time:", str_conv_time)
# strptime function is used to convert the date time object as string
date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

print("****Random time Library using***********")
print(randrange(100000,999999,2))
print (randint(100000,999999))

