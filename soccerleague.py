class SoccerLeagues(object):
    def points(self,matches):
        r=[]
        for i in range(len(matches)):
            p=0
            for j in range(len(matches[i])):
                while(i!=j):
                    if matches[i][j]=='W':
                        p+=3
                        break
                    elif matches[i][j]=='D':
                        p+=1
                        break
            r.append(p)
        return r
x=SoccerLeagues()
print x.points(("-WW","W-W","WW-"))
