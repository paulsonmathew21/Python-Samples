class SkiResortsEasy(object):
    def minCost(self,altitude):
        units=0
        altitude=list(altitude)
        for i in range(1,len(altitude)):
            if altitude[i]>altitude[i-1]:
                units+=altitude[i]-altitude[i-1]
                altitude[i]=altitude[i-1]
        return units
x=SkiResortsEasy()
print x.minCost((712, 745, 230, 200, 648, 440, 115, 913, 627, 621, 186, 222, 741, 954, 581, 193, 266, 320, 798, 745))
