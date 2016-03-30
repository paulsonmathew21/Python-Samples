class TournamentJudging(object):
    def getPoints(self,rawScores,conversionFactor):
        s=0
        for i in range(len(rawScores)):
            s+=round(rawScores[i]*1.0/conversionFactor[i])
            print s
        return s
x= TournamentJudging()
print x.getPoints((8, 16, 32),(10, 10, 5))
