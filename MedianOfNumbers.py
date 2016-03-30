class MedianOfNumbers(object):
    def findMedian(self,numbers):
        numbers=list(numbers)
        #print len(numbers)
        if len(numbers)%2!=0:
            #print "x"
            numbers=sorted(numbers)
            #print m
            return int(numbers[(len(numbers)/2)])  
        else:
            return -1
x=MedianOfNumbers()
print x.findMedian((1, 4, 2, 5, 7))
