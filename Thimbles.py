class Thimbles(object):
    def thimbleWithBall(self,swaps):
        pos=1
        for i in range(len(swaps)):
            if int(swaps[i][0])==pos:
                print swaps[i][0],"sdsz"
                pos=int(swaps[i][2])
            elif int(swaps[i][2])==pos:
                pos=int(swaps[i][0])
        return pos
x=Thimbles()
print x.thimbleWithBall(("1-2", "3-1"))
