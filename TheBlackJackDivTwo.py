class TheBlackJackDivTwo():
    def score(self,cards):
        count=0
        for i in range(len(cards)):
            print cards[i][0]
            if cards[i][0]=='2' or cards[i][0]=='3' or cards[i][0]=='4' or cards[i][0]=='5' or cards[i][0]=='6' or cards[i][0]=='7' or cards[i][0]=='8' or cards[i][0]=='9':
                print "x"
                count+=int(cards[i][0])
            elif cards[i][0]=="T":
                count+=10
            elif cards[i][0]=="A":
                count+=11
            else:
                count+=10
        return count
x=TheBlackJackDivTwo()
print x.score(("3S", "KC", "AS", "7C", "TC", "9C", "4H", "4S", "2S"))
