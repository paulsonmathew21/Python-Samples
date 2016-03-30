class MagicalStringDiv2:
    def minimalMoves(self, S):
        mid=len(S)/2
        return S[0:mid].count("<")+S[mid:].count(">")
        
x=MagicalStringDiv2()
print x.minimalMoves(("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))
