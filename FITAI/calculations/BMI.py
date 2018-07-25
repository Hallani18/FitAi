def BMIcalc (feet,inches,lbs):
    heightin = (feet * 12) + inches
    heightm = heightin * 2.54 / 100
    kgs = lbs * 0.453495
    #print("heightcm"+str(heightm))
    BMI = kgs / (heightm ** 2)
    print ("your BMI is: ", "%.2f" % BMI)
    #if BMI <= 16:
        #print ("you need to eat more and get more nutrition, you are too thin")
        #return BMI
    #elif 16 < BMI <= 18.5:
        #print ("your weight is a little bit light, the best way for you is to eat more")
        #return BMI
    #elif 18.5 < BMI <= 25:
        #print ("great, you are in the right way, keep going on")
        #return BMI
    #elif 25 < BMI <= 30:
        #print ("oops, you are just a little bit heavy. However, stand in front of the mirror to watch yourself, if you are not fat, you must have some muscles")
        #return BMI
    #elif 30 < BMI <= 35:
        #print ("hmmm... Compare with other people, you are heavy. However, stand in front of the mirror to watch yourself, if you are not fat, you must have some muscles")
        #return BMI
    #elif 35 < BMI <= 40:
        #print ("Hey, do something, you need to keep fit. However, stand in front of the mirror to watch yourself, if you are not fat, you must have some muscles")
        #return BMI
    #elif 40 < BMI:
        #print (" Wow, your BMI is very hight, please try to keep fit. However, if you are a body builder, just ignore it")
    return BMI
    #x = input ("press enter to quit")
