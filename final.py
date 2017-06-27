from PIL import Image
im = Image.open('picture.jpg')

imCopy = im.copy()    #Going to create a new picture cropping our faces

RobertFace = im.crop((290, 75, 586, 444))    #Use GIMP to find pixels
AllenFace = im.crop((84, 82, 296, 324))

for i in range (100):    #Drag some patterns across the image to wipe it
    imCopy.paste(AllenFace, (4*i, 0))
    imCopy.paste(RobertFace, (0, 9*i))

for n in range (80):        #Drag our images across the screen to make a new pic
    
    imCopy.paste(AllenFace, ((500-(6*n), 704 - (4*n))))
    imCopy.paste(RobertFace, ((610-(6*n), 288 - (4*n))))

imCopy.show()
