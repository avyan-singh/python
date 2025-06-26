from PIL import Image
mac=Image.open("C:\\avyan\\python\\working_with_images\\example.jpg")
# mac.show()
print(mac.size)
half=1993/2
x=half-200
w=half+200
h=1257
y=800
computer=mac.crop((x,y,w,h))
mac.paste(im=computer, box=(0, 0))
mac.show()