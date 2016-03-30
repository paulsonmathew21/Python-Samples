class WritingWords(object):
	def write(self,word):
		self.word=""
		word=word.upper()
		c=0
		alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		for i in word:
			for check in range(len(alp)):
				if i==alp[check]:
					c+=(check+1)
		return c
x=WritingWords()
print x.write("ABC")
