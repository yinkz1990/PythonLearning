from PIL import Image, ImageFilter

img = Image.open('./image_compress/denys_oyhaxc.jpg')
filtered_Img = img.filter(ImageFilter.BLUR)
filtered_Img.save('blur.png', 'png')

# To resize an image
img2 = Image.open(
    './image_compress/daniel-korpai-HyTwtsk8XqA-unsplash_gz8uu7.jpg')
# resize accept a tuple
GreyImage = img2.convert('L')
new_image = GreyImage.resize((300, 300))
new_image.save('resized.png', 'png')

# To Crop an image
img3 = Image.open('./image_compress/denys_oyhaxc.jpg')
# resize accept a tuple
box = (100, 100, 400, 400)
region = img3.crop(box)
region.save('cropped.png', 'png')


# Keeping the aspect ratio

img4 = Image.open('./Image_compress/sessler.jpg')
img4.thumbnail((400, 400))
img4.save('thumbnail.jpeg')
print(img4.size)
