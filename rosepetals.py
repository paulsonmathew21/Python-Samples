class RosePetals(object):
    def getScore(self,dice):
        self.dice=()
        dice=list(dice)
        score=0
        print dice
        for i in range(0,len(dice)):
            #print dice[i]
            if dice[i]==3:
                score+=2
            elif dice[i]==5:
                score+=4
        return score
x=RosePetals()
print x.getScore((1,2,3,2,1))
