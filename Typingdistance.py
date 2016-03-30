class TypingDistance(object):
    def minDistance(self,keyboard,word):
        d=0
       
        print keyboard, word
        #c=keyboard.index(word[0])
        for i in range(len(word)):
            for j in range(len(keyboard)):
                if i==0 and word[i]==keyboard[j]:
                    c=j
                    #print j
                    break
                else:
                    if word[i]==keyboard[j]:
                        c_1=j
                        d+=abs(c_1-c)
                        c=c_1
        
                #if word[i]==keyboard[j]:
                    #a.append(j)
                    #print j
        #for i in word:
            #c_1=keyboard.index(i)
            #d+=abs(c_1-c)
            #c=c_1
        return d
        
x=TypingDistance()
print x.minDistance("qwertyuiop","potter")
                
