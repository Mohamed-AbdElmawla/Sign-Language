{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2 #opencv \n",
    "import os\n",
    "import time\n",
    "import uuid\n",
    " \n",
    " \n",
    "Images_Path='Tensorflow/workspace/images/collectedimages'\n",
    " \n",
    " \n",
    "labels = {'Water', 'Movie','Game','Me','Help','What'}\n",
    "number_images=15\n",
    " \n",
    "for label in labels:\n",
    "        dir= r'images/collectedimages/' + label\n",
    "        os.makedirs(dir, exist_ok=True)\n",
    "        cap=cv2.VideoCapture(0)\n",
    "        print('Collecting images for {}'.format(label))\n",
    "        time.sleep(5)\n",
    "        for imgnum in range(number_images):\n",
    "                ret,frame=cap.read()\n",
    "                imagename=os.path.join(Images_Path,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))\n",
    "                cv2.imwrite(imagename,frame)\n",
    "                cv2.imshow('frame',frame)\n",
    "                time.sleep(2)\n",
    " \n",
    "                if cv2.waitKey(1) and  0xFF==ord('q'):\n",
    "                        break\n",
    "        cap.release()\n",
    " "
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
