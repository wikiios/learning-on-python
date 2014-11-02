from PIL import Image
from pylab import *
im = array(Image.open('empire.jpg').convert('L'))
figure()
gray()
contour(im,origin = 'image')
figure()
axis('equal')
axis('off')
hist(im.flatten(),128)
imshow(im)
x = [100,100,400,400]
y = [200,500,200,500]
plot(x,y,'r*')    #在坐标轴上标记，r*是红色星状
plot(x[:2],y[:2])
plot(x[2:],y[:2])
title('Plotting:"empire.jpg"')
show()
