import cv2 as cv
import os
import zipfile
import numpy as np
import pandas as pd
import gdown

classes={
    0:('akiec', 'actinic keratoses and intraepithelial carcinomae'),
         
    1:('bcc' , 'basal cell carcinoma'),
         
    2:('bkl', 'benign keratosis-like lesions'),
         
    3:('df', 'dermatofibroma'),
         
    4:('nv', ' melanocytic nevi'),
         
    5:('vasc', ' pyogenic granulomas and hemorrhage'),
         
    6:('mel', 'melanoma'),
    }


def create_dataset(resize=None):
    def process_images(srcdir,resize=None):
        imgs = []
        filenames = []
        
        for dir in srcdir:
            dir = download_file(dir)
            with zipfile.ZipFile(dir, 'r') as zipf:
                for temp in zipf.namelist():
                    img = cv.imdecode(np.frombuffer(zipf.read(temp), np.uint8), cv.IMREAD_COLOR)
                    if resize is not None:
                        img = cv.resize(img, resize)
                    imgs.append(img)
                    filenames.append(temp)
        
        # Split filenames to remove file extensions
        filenames = [os.path.splitext(filename)[0] for filename in filenames]
        
        return imgs, filenames
    
    def merge_with_meta(imgs,meta,filenames):
        # Create the DataFrame with flattened pixel values
        dt = pd.DataFrame([img.flatten() for img in imgs])
        dt.columns = ['pixel'+str(i) for i in range(dt.shape[1])]
        dt['image_id'] = filenames

        dd = pd.read_csv(meta)
        dt=dt.merge(dd[['image_id','dx']], on='image_id', how='left')
        dt['label'] = dt['dx'].map({value[0]:key for key, value in classes.items()})

        dt = dt.drop(['image_id','dx'], axis=1)
        return dt,dd
    
    #https://www.intodeeplearning.com/how-to-download-files-or-folders-in-gdrive-in-python/
    def download_file(url):
        output_path = 'file.zip'
        gdown.download(url, output_path, quiet=False,fuzzy=True)
        return output_path
    
    
    # Process the images and filenames
    srcdir = ['1vNLwZ4ao7eZTAeH0JRIhaZ1QbiP3LsDG','1w6eRHc4sKJ1jzh5gU112HK8mfgraqcIj']
    srcdir = ['https://drive.google.com/uc?id=' + x for x in srcdir]
    meta ='https://drive.google.com/uc?id=' + '1x5hrResjvpGAu-xVkJJH-hT1q4wx6xco' 
    imgs, filenames = process_images(srcdir, resize=resize)
    train,train_meta = merge_with_meta(imgs,meta,filenames)

    # Process the images and filenames
    srcdir = ['1n71CVP_3-OpcwSaC6z1Y1JCyCznzVP9t']
    srcdir = ['https://drive.google.com/uc?id=' + x for x in srcdir]
    meta ='https://drive.google.com/uc?id=' + '1gONzrx2LBFRpIsajIc12yEnOA-axPSyt'
    imgs, filenames = process_images(srcdir, resize=resize)
    test,test_meta = merge_with_meta(imgs,meta,filenames)

    return train,test,train_meta,test_meta


def get_default_dataset():
    train = pd.read_csv('https://drive.google.com/uc?id=' + '12tVAC3jbVNUbaQUlchV5-8ZYZXqOzfMr')
    test = pd.read_csv('https://drive.google.com/uc?id=' + '1kYWB6TAoQbaZHtQycE1Jue0lUKc62IV7')
    train_meta = pd.read_csv('https://drive.google.com/uc?id=' + '1x5hrResjvpGAu-xVkJJH-hT1q4wx6xco')
    test_meta = pd.read_csv('https://drive.google.com/uc?id=' + '1gONzrx2LBFRpIsajIc12yEnOA-axPSyt')
    return train,test,train,test,train_meta,test_meta
