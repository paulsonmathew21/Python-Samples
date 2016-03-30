class LetterStrings(object):
    def sum(self,s):
        count = 0
        s="".join(s)
        for c in s:
            if c.isalpha():
                count += 1
        return count
x=LetterStrings()
print x.sum(("aksj"))
