HOUR_MINUTES = 60
ON_TIME_MINUTES = 30

BEFORE_EXAM = "before"
AFTER_EXAM = "after"

exam_hour = int(input())
exam_minutes = int(input())

arrival_hour = int(input())
arrival_minutes = int(input())


exam_time_minutes = exam_hour * HOUR_MINUTES + exam_minutes
arrival_time_minutes = arrival_hour * HOUR_MINUTES + arrival_minutes

difference = abs(exam_time_minutes - arrival_time_minutes)

time = None

if exam_time_minutes == arrival_time_minutes:
    print("On time")
    
elif exam_time_minutes > arrival_time_minutes:
    time = BEFORE_EXAM
    
    if difference <= ON_TIME_MINUTES:
        print("On time")
    
    elif difference > ON_TIME_MINUTES:  
        print("Early")
else:
    time = AFTER_EXAM
    
    print("Late")

if difference != 0:

    if difference >= HOUR_MINUTES:
        difference_hours = difference // HOUR_MINUTES
        difference_minutes = difference % HOUR_MINUTES
        
        print(f"{difference_hours}:{difference_minutes:02d} hours {time} the start" )
        
    else:
        print(f"{difference} minutes {time} the start")
