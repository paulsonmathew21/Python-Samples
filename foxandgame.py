class FoxAndGame(object):
    def countStars(self,result):
        #self.result=()
        stars=0
        for i in range(len(result)):
            for j in range(len(result[i])):
                if  result[i][j]=='0':
                    stars+=1
        return stars

x=FoxAndGame()
print x.countStars(("000","0--","00-"))
