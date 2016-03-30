class ImageDithering(object):
    def count(self,dithered,screen):
        c=0
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                if screen[i][j] in dithered:
                    c+=1
        return c
x=ImageDithering()
print x.count(("BW"),("AAAAAAAA","ABWBWBWA","AWBWBWBA","ABWBWBWA","AWBWBWBA","AAAAAAAA"))
