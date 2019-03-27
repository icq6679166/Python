from urllib2 import urlopen
from PIL import Image

url1 = 'https://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/s1p-2019-03-27-09-50.jpg'
fileToSave = urlopen(url1)
image1 = Image.open(fileToSave)
# mkdir photos
image1.save('photos\\normal.jpg')
half = (image1.size[0] // 2, image1.size[1] // 2)
half_image = image1.resize(half, Image.ANTIALIAS)
half_image.save('photos\\half.jpg')
rot1 = image1.transpose(Image.ROTATE_90)
rot1.save('photos\\r90.jpg')
rot2 = image1.transpose(Image.ROTATE_180)
rot2.save('photos\\r180.jpg')
rot3 = image1.transpose(Image.ROTATE_270)
rot3.save('photos\\r270.jpg')
