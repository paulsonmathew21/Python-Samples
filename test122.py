class ArrayHash(object):
    def getHash(self,input):
        value=0
        for i in range(len(input)):
            for j in range(len(input[i])):
                value+=i+j+ord(input[i][j]) - 65
        return value
x=ArrayHash()
print x.getHash(("ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
