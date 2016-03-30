class SumOfPower(object):
    def findSum(self,array):
        count=0
        for i in range(0,len(array)):
            print "a[%i]"%i
            #if i==0:
            for j in range(i,len(array)):
                print "j",j,array[j]
                count+=sum(array[i:j+1])
                print array[i:j+1]
                
                print count
                print "this is ",count
            #else:
                
        return count
x=SumOfPower()
print x.findSum((3,14,15,92,65))
            
