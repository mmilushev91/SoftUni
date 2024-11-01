YEAR_LINE = 16

MALE = "m"
FEMALE = "f"

MALE_ABOVE_YEAR_LINE = "Mr." 
MALE_BELLOW_YEAR_LINE = "Master" 

FEMALE_ABOVE_YEAR_LINE = "Ms." 
FEMALE_BELLOW_YEAR_LINE = "Miss" 

age = float(input())
gender = input()

if gender == MALE:
    
    if age >= YEAR_LINE:
        print(MALE_ABOVE_YEAR_LINE)
    else:
        print(MALE_BELLOW_YEAR_LINE)
        
elif gender == FEMALE:
    
    if age >= YEAR_LINE:
        print(FEMALE_ABOVE_YEAR_LINE)
    else:
        print(FEMALE_BELLOW_YEAR_LINE)
      
