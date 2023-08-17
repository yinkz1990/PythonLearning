import sys
import os
from PIL import Image

# selecting the folder names from terminal
image_folder = sys.argv[1]
new_folder = sys.argv[2]

# check if the new folder exist, if not create a new one
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    print('created the folder')

# check the list of images in the folder

for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)
    print(clean_name)
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{new_folder}{clean_name[0]}.png', 'png')
    print('It is all done')
