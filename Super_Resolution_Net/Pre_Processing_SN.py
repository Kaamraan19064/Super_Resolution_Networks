import os
from os import listdir
from os.path import isfile, join 
from PIL import Image

class pre_process: 
    test_path=""
    train_path=""
    
    def __init__(self,test_directory,train_directory): 
        self.test_path = test_directory 
        self.train_path = train_directory
        self.count = 0
    
    def process(self,string):
        self.count = 0
        if string == "train": 
            path = self.train_path 
            processed_input = "/home/harsh.shukla/SRCNN/SR_data_512/train/input"
            processed_target = "/home/harsh.shukla/SRCNN/SR_data_512/train/target"
            processed_dir = "/home/harsh.shukla/SRCNN/SR_data_512/train"
        else:
            path = self.test_path
            processed_input = "/home/harsh.shukla/SRCNN/training_test_data/Manga/input"
            processed_target = "/home/harsh.shukla/SRCNN/training_test_data/Manga/target"
            processed_dir = "/home/harsh.shukla/SRCNN/training_test_data/Manga/"
        
        os.chdir(path)
        walker = list(os.walk(path))
        filenames = walker[0][2]
        
        os.mkdir(processed_dir)
#         if string = "train":
#             os.mkdir(os.path.join(processed_dir,"train"))
#         else: 
#             os.mkdir(os.path.join(processed_dir,"test"))
        os.mkdir(processed_input)
        os.mkdir(processed_target)
#         print(filenames)
        for i in filenames:
            print(i)
            im = Image.open(i)
#             left = int(im.size[0]/2-1600/2)
#             upper = int(im.size[1]/2-1600/2)
#             right = left + 1600
#             lower = upper + 1600
#             im = im.crop((left, upper,right,lower))
            im = im.resize((4*int(im.size[0]/4),4*int(im.size[1]/4)))
            im.save(os.path.join(processed_target, str(self.count) + '.png'))
            im = im.resize((int(im.size[0]/4),int(im.size[1]/4)))
            im.save(os.path.join(processed_input, str(self.count)  + '.png'))
            self.count+=1
#             if i.split('.')[0][-1]== path[-1] :
#                 im = im.resize((64,64))
#                 im = im.resize((128,128))
#                 im.save(os.path.join(processed_input,i.split('.')[0].split('_')[0]+i.split('.')[0].split('_')[1]+"_"+path[-1]+".jpg"))
#             else:
# #             print(name[-1])
#                 im.save(os.path.join(processed_target, i.split('.')[0].split('_')[0]+i.split('.')[0].split('_')[1]+"_"+path[-1]+".jpg"))
#             print(os.path.join(processed_dir, i))
            

##Div 2k
train_directory = "/scratch/harsh_cnn/train"
test_directory = "/home/harsh.shukla/SRCNN/test_Data/Manga109"

##Real SR
# train_directory = "/home/harsh.shukla/SRCNN/RealSR (ICCV2019)/Nikon/Train/2"
# test_directory = "/home/harsh.shukla/SRCNN/RealSR (ICCV2019)/Nikon/Test/2"

ob = pre_process(test_directory,train_directory)
# ob.process("train")
ob.process("test")