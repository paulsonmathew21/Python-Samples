class Justifier(object):
    def justify(self,textIn):
        textIn=list(textIn)
        print max(textIn)
        s=[]
        for i in range(len(textIn)):
            s.append(len(textIn[i]))
        #print s
        x= max(s)
        
        for i in range(len(textIn)):
            
            temp=list(textIn[i])
            if len(textIn[i])<x:
                for j in range(x-len(textIn[i])):
                    temp.insert(j," ")
                textIn[i]=''.join(temp)
        return textIn
                
x=Justifier()
print x.justify(("LONGEST","A","LONGER","SHORT"))
