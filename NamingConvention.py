class NamingConvention(object):
    def toCamelCase(self,variableName):
        variableName=list(variableName)
        for i in range(0,len(variableName)-1):
            if variableName[i]=='_':
                print "fgdf"
                variableName[i+1]=str(variableName[i+1]).upper()
                
            elif i==0:
                variableName[i+1]=str(variableName[i+1]).lower()
        variableName = list(filter(lambda x: x!= '_', variableName))
        return ''.join(variableName)
x=NamingConvention()
print x.toCamelCase(("sum_of_two_numbers"))
