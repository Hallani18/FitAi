def caloriecalc (feet, inches, lbs,age,gender):
    heightin = feet * 12 + inches
    heightcm = heightin * 2.54
    #print("heightcm:"+str(heightcm))
    kgs = lbs * 0.45359237
   #print("kgs:"+kgs)
    if gender == "male":
        calories = (9.99 * kgs) + (6.25 * heightcm) - (5 * age) + 5
        calories=float(int(calories*100)/100)
        return calories
    
    elif gender == "female":
        calories = (9.99 * kgs) + (6.25 * heightcm) - (4.92 * age) - 161
        calories=float(int(calories*100)/100)
    
   # print ("you should get ", "%.2f" % calories, "Calories per day. If you get ",
           #calories + 500, "Calories per day, you can gain 1lb per week. If you get", float((int(100*(calories - 500))/100)),
           #"Calories per day, you can lose 1lb per week")
    return calories
    #x = input ("press enter to quit")
    
print(caloriecalc(6,0,210,28,'female'))
