#http://www.nutristrategy.com/caloriesburned.htm
#Maths: (Y=130*60*X)->(130*60X=Y)->((13*60x/7800)=(Y/7800))->(x=Y/7800)
#Excersises are calculated using the weight of 130 lbs and 60 minutes

#Dictionary: 'workout' : calories/min 
exercises = {
        #Light, Moderate, Heavy Excersises
         'jump rope light' : .0605128205,
         'jump rope medium' : .07564,
         'jump rope heavy' : .0907692,
         'cycling rough terrain':.06435897435,
         'cycling light':.030256419256,
         'cycling moderate':.045384615,
         'cycling heavy':.12102564,
         'stationary cycling light':.022592307,
         'stationary cycling moderate':.052948717,
         'stationary cycling heavy':.0946153846,
         'calisthenics light':.0265384,
         'calisthenics moderate':.0337820512,
         'calisthenics heavy':.06051282,
         'circuit training':.06051282,
         'weight lifting heavy' :.04538461,
         'weight lifting moderate':.034102564,
         'weight lifting light' : .022692307,
         'health club exercise' : .041666,
         'rowing machine light' : .0265384615,
         'rowing machine moderate' : .0529487,
         'rowing machine heavy' : .09076923,
         'aerobics light': .037820512,
         'aerobics moderate' : .0492307,
         'aerobics heavy' : .0642307,
         'stretching light' : .01897435,
         'stretching moderate' : .030256410254,
         'streching heavy' : .0453846,
         'dancing light' : .022692,
         'dancing moderate' :  .034102564,
         'dancing heavy' : .041666,
         'running light' : .060512,
         'running moderate' : .08320512,
         'running heavy' : .13615384,
            #Single Excersise
         'archery' : .02653846153, 
         'jazzercise' : .0453846,
         'ski machine' : .0529487174,
         'stair machine' : .068076923,
         'badminton' : .034102564,
         'basketball' : .06051282,
         'billards' : .01897435,
         'bowling' : .022692,
         'boxing' : .09076932,
         'cricket' : .037820512,
         'croquet' : .018974358,
         'curling' : .03025641925,
         'darts' : .018974,
         'fencing' : .045384615,
         'football' : .0603846,
         'frisbee' : .022592307592,
         'ultimate frisbee' : .0605128205,
         'golf' : .034102,
         'gymnastics' : .042307682,
         'hacky sack' : .0302564,
         'jai alai' : .0907692,
         'martial arts' : .07564102,
         'juggling' : .0302564,
         'kickball' : .0529487,
         'lacrosse' : .0605128205,
         'orienteering' : .06807,
         'paddleball' : .045384,
         'polo' : .060512,
         'racquetball' : .06435897,
         'rock climbing' : .083205,
         'rugby' : .07564192564,
         'shuffleboard' : .02292307,
         'skateboarding': .0378205,
         'rollerskating' : .0529487,
         'skydiving' : .022692307,
         'soccer' : .07564,
         'baseball' : .0378205,
         'squash' : .0907692307,
         'table tennis' : .0302564,
         'tai chi' : .0302564,
         'tennis' : .052948717,
         'trampoline' : .026538,
         'volleyball' : .060512,
         'wrestling' : .0453846,
         'wallyball' : .0529487,
         'backpacking' : .0529487,
         'marching' : .0492307,
         'kayaking' : .037820512,
         'walking' : .018974,  
                              
        }
#a=(130*60*exercise['aerobics light'])

#print(a)
#251/3900
#299/4650
#for i in exercise:
    #print(i)
    #print(exercise[i])

def maths(weight,time,exercise):
    calories=weight*time*exercise
    calories=int(calories*100)
    calories=float(calories/100)
    return calories
#if __name__=="__main__":
    #print(maths(171, 30, exercises['running moderate']))















