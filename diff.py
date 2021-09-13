#!/usr/bin/python3

import cv2
import os
import glob
from skimage.metrics import structural_similarity as compare_ssim

# Find most recent folder in imgs, to process
recent = max(glob.glob('imgs/*'), key=os.path.getmtime)

# Find all speckle images in above folder
imgs = glob.glob(os.path.join(recent, '*.jpg'))

# Sort images by time they where modified
imgsn= sorted(imgs, key=os.path.getmtime)

# Create file of list of speckle pattern differences, from original speckle pattern
fl = open("list.txt","w")

for n in range(1,len(imgsn)):
    a = cv2.imread(imgsn[0])[:,:,2] # original speckle pattern (red channel)
    b = cv2.imread(imgsn[n])[:,:,2] # nth speckle pattern      (red channel)
    (score, diff) = compare_ssim(a, b, full=True) # get difference between original and nth speckle pattern
    diff = (diff * 255).astype("uint8")
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] # show difference through thresholding
    cv2.imwrite("out-{}.jpg".format(n), thresh)
    fl.write("""file 'out-{}.jpg'\n""".format(n))

fl.close()

# Generate video of speckle pattern differences
os.system("ffmpeg -y -r 0.5 -f concat -safe 0 -i list.txt -vcodec libx264 -crf 23 out.mkv")
