class WhichDay(object):
    def getDay (self,notOnThisDay):
        days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]
        for i in days:
            #print i
            #temp=str(i)
            if not i in notOnThisDay:
                return i
            #for j in range(len(notOnThisDay)):
                #if days[i]!=notOnThisDay[j]:
                    #return days[i]
x=WhichDay()
print x.getDay(("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
