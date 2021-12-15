"""
File Name: invertimage.py
Lab Activity: Lab 3._1 part 2 b
Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 15/09/2021

Program Description: Inverting an image makes it look like a photographic negative. Define and test a function named invert.
    This function expects an image as an argument and resets each RGB component to 255 minus that component.
    Be sure to test the function with images that have been converted to grayscale and black and white as well as color images.'''
Peer review student id and name : 
Parichhit Basnet
s4662952
Parichhit.basnet@live.vu.edu"""
# here i have taken 3 different type of images as shown in comment below as a result of VU collaborate example and save them using Image.save("filename") function
# i have imported Image class from images.py file which is in same directory as this file.
from images import Image
def invert(filename):# here i am defining function with name invert and parameter filename
    image = Image(filename)# using Image class to open the filename
    for y in range(image.getHeight()):# getting y as image height along y axis 
        for x in range(image.getWidth()):# getting x as image width along x axis
            (r, g, b) = image.getPixel(x, y)# getting the RGB value of image
            # changing image RGB value as given by quesetion
            r = int(255 - r)
            g = int(255 - g)
            b = int(255 - b)
            image.setPixel(x, y, (r, g, b))# setting new RGB value to the image
    return image.draw()# returning function to drawi image in the window
# inverting image using color smokey.gif from the same directory as the file
print("Close the image window to continue.")
invert("smokey.gif")
#inverting image using grayscaled "graysmokey.gif" from the same directory as the file
print("Close the image window to continue.")
invert("graysmokey.gif")
#inverting image using black and white photo "blackandwhitesmokey.gif" from the same directory as the file
print("Close the image window to continue. ")
invert("blackandwhitesmokey.gif")
