import time
current_epoch = time.time()

total_minutes = current_epoch/60 #EPOCH time in minuets
total_hours = total_minutes/60 #EPOCH time in hours
total_days = total_hours/24 #EPOCH time in days
year_in_4 = total_days/1461 #years since EPOCH in blocks of 4 to account for leap years
total_years = year_in_4 * 4 #number of years that have passed since EPOCH

current_second = int(total_minutes%1*60//1) #current second using the remainder from the total minuets
current_minutes = int(total_hours%1*60)//1 #current minute using the remainder from the total hours
current_hour = int(total_days%1*24)//1 #current hour using the remainder from the total days
current_month = round(total_years%1*12) #current month from the remainder of the total years
current_year = int(total_years//1+1970) #current year given Epoch started in 1970

if current_year%4==0: #checking if the current year is a leap year or not
    current_day = int(total_years%1*366)+1 #current year day from remainder of total years if it's a leap year
    day = [1,32,61,92,122,153,185,214,245,275,306,336] #list of each first year-day for each month if it's a leap year
else:
    current_day = int(total_years%1*365)+1 #current year day from remainder of total years if it's not a leap year
    day = [1,32,60,91,121,152,184,213,244,274,305,335] #list of each first year-day for every month if it's not a leap year

i = 0
while current_day > day[i]: #finds what month the current year day is located in
    i = i+1
date = (current_day-(day[i-1]-1)) #calculates the date once the correct month is found

current_second = str(current_second) 
if len(current_second)<2: #adds a 0 before the number if its less than 10 seconds
        current_second = current_second.zfill(2)
        
current_minutes = str(current_minutes)
if len(current_minutes)<2: #adds a 0 before the number if its less than 10 minutes
        current_minutes = current_minutes.zfill(2)  

date = str(date)
if len(date)<2: #adds a 0 before the number if the date is less than the tenth
        date = date.zfill(2) 
        
current_month = str(current_month)
if len(current_month)<2: #adds a 0 before the number if the month is less than the tenth
    current_month = current_month.zfill(2)

print("THE DATE IS:",current_year,end='-')
print(current_month,date,sep='-',end=' ')
print(current_hour,current_minutes,current_second, sep=':',end=' ')
print('GMT')
print('THE TIME SINCE EPOCH IS:',current_epoch,"SECONDS")
