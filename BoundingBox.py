class BoundingBox(object):
    def smallestArea(self,X,Y):
        return (max(X)-min(X))*(max(Y)-min(Y))
x=BoundingBox()
print x.smallestArea((9,-88,-40,98,-55,41,-38),(-65,56,-67,7,-58,33,68))
