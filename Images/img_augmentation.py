#Snippet for Image augmentation using Augmentor package. 

import Augmentor
#in case of Augmentor not installed, install using pip install Augmentor
p=Augmentor.Pipeline("Image directory here")
p.flip_left_right(0.5)#Flips left-right with probablity of 0.5
p.rotate(0.3, 25, 20) 
p.skew(0.4, 0.5) 
p.zoom(probability = 0.2, min_factor = 1.1, max_factor = 1.3) 
p.random_distortion(probability=1, grid_width=8, grid_height=8, magnitude=7)
p.crop_random(probability=1, percentage_area=0.8)
p.resize(probability=1.0, width=120, height=120)
p.sample(1600)#No of final images you need in total
