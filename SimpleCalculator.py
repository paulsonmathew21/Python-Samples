class SimpleCalculator(object):
    def calculate(self,input):
        #print input[1]
        if '+' in input:
            x=input.index('+')
            return int(input[:x])+int(input[x+1:])
        elif '-' in input:
            x=input.index('-')
            return int(input[:x])-int(input[x+1:])
        elif '*' in input:
            x=input.index('*')
            return int(input[:x])*int(input[x+1:])
        elif '/' in input:
            x=input.index('/')
            return int(input[:x])/int(input[x+1:])
        
x=SimpleCalculator()
print x.calculate(("17+18"))
