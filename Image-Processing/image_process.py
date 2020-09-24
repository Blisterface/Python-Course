from PIL import Image,ImageFilter

img = Image.open('./Characters/Kata.jpeg')
img_fil = img.convert('L')
img_fil.save('grey.png','png')
img_fil.show()