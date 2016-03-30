class CssPropertyConverter(object):
    def getCamelized(self,cssPropertyName):
        cssPropertyName=list(cssPropertyName)
        result=""
        for i in range(len(cssPropertyName)):
            if cssPropertyName[i] == '-':
                #result+=''.join(cssPropertyName[:i])
                cssPropertyName[i+1]=cssPropertyName[i+1].upper()
                #print cssPropertyName
                #result+=''.join(cssPropertyName[i+2:])
        for i in cssPropertyName:
            if i!='-':
                result+=i
        return result
x=CssPropertyConverter()
print x.getCamelized(("top-border-width"))
        
