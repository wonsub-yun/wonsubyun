from PIL import Image
import os
iter_num=1
original_directory="/home/wonsub/Desktop/abcd"
list_of_files=os.listdir(original_directory)
for image_files in list_of_files:
    impath = original_directory+"/"+image_files
    image=Image.open(impath)
    for a in range (11):
        for b in range(15):
            croppedIm=image.crop((300*(a-1),300*(b-1),300*(a-1)+300,300*(b-1)+300))
            croppedIm.save("/home/wonsub/Desktop/cropped_image/"+"cropped_image"+str(iter_num)+".jpg")
            iter_num+=1