class LittleElephantAndBooks(object):
    def getNumber(self,pages,number):
        pages=list(pages)
        pages=sorted(pages)
        lis=pages[0:number-1]
        if number<2:
            return pages[number]
        elif number==2:
            if len(pages)==2:
                return sum(pages[:number])
            else:
                return pages[0]+pages[2]
        else:
            return sum(lis)+int(pages[number])
        #s=0
        #if number<=2:
            #return 
        #for i in range(0,number):
            #s+=pages[i]
        return lis   
x=LittleElephantAndBooks()
print x.getNumber((74, 86, 32, 13, 100, 67, 77),(3))
