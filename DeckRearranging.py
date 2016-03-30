class DeckRearranging(object):
    def rearrange(self,deck,above):
        result=[]
        for i in range(len(deck)):
            result.insert(above[i],deck[i])
        return ''.join(result)
x=DeckRearranging()
print x.rearrange(("BRBRR"),(0, 0, 1, 0, 3))
