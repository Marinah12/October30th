courses = 0

while (courses < 5) or (courses > 8): #Don't let the user exit this loop without selecting courses between 5-8
    courses = int(input("How many courses have you taken: "))
print("") #For formatting purposes
total = 0.0 #Add a .0 to the end of 0 to make total a float

for i in range(courses):
    grade = float(input("What grade did you receive in course %d: " % (i+1))) #Ask for the grade in each course
    total += grade #Keep track of the total grade

average = total/courses #Calculate the average

if average >= 79.5:
    average = str(round(average, 2)) + "%"  #Convert average to string so we can round and add the % sign for nicer printing
    print("\nCongratulations you have earned the principals award with an average of %s" % average)
