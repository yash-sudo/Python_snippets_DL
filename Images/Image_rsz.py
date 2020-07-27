#Simple python snippet to get all images redimensioned and padded to required dimension while maintaining the aspect ratio using the python pillow

from PIL import Image
import os
dsrd_sz=512
parent_path="set path of parent folder of all image"
for path in os.listdir(parent_path):
  address= parent_path +path
  img=Image.open(address)
  if(max(img.shape[0],img.shape[1])>dsrd_sz): 
    #if any dimension is >dsrd_sz, resize both dimensions to dsrd_sz
      img.thumbnail((dsrd_sz,dsrd_sz),PIL.Image.ANTALIAS)
      # resizes the image whie simutaneously maintaining the aspect ratio


  #Pad the images to dsrd_sz*dsrd_sz dimension, in case if any(or both) dimension(s) <dsrd_sz
  new_size = (dsrd_sz, dsrd_sz)
  new_im = Image.new("RGB", = new_size)   
  new_im.paste(img, ((new_size[0]-img.shape[0])/2,
                        (new_size[1]-img.shape[1])/2))
  new_im.save(address)
  #replace the old image 
