"""
File Name: sepia.py
Lab Activity: Lab 3._1 part 2 c
Author: Sunil Paudel 
Student ID:(s4664741) 
Date: 15/09/2021

Program Description: c)	Old-fashioned photographs from the nineteenth century are not quite black and white and not quite color, but seem to have shades of gray,
brown, and blue. This effect is known as sepia. Write and test a function named sepia that converts a color image to sepia. This function should first call grayscale
function to convert the color image to grayscale.
peer review: student Name=  Samundra Rayamajhi
Student id= s466370
"""
#here we are importing class Image from images.py file 
from images import Image
def grayscale(image):# this is the function to convert image tnto sepia
    for y in range(image.getHeight()): # getting y as image height along y axis
        for x in range(image.getWidth()): #getting x as image width along x axis
            (r, g, b) = image.getPixel(x, y)#getting the RGB value of image
            # changing image RGB value as given by quesetion
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b # getting the value of lum
            image.setPixel(x, y, (lum, lum, lum))#setting new luminous intensity value to the image

def sepia(image):
    # to converts an Image to Sepia
    grayscale(image)
    '''for converting sepia we need to convert colorfull image to grayscale
    so we are using grayscale funtion to convert the image to grayscale'''
    for y in range(image.getHeight()):#getting y as image height along y axis
        for x in range(image.getWidth()):# getting x as image width along x axis
            (red, green, blue) = image.getPixel(x, y)##getting the RGB value of image
            # condition to be sepia from grayscale as given in quesetion
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            image.setPixel(x, y, (red, green, blue))# setting new RGB value to pixel

def main(filename="smokey.gif"): # defining main function with paramater filename whiich default value is "smokey.gif"
    image = Image(filename)# using Image class to open image
    print("Close the image window to continue. ")
    image.draw() # to draw image
    grayscale(image)
    print("Close the image window to continue. ")
    image.draw() # to draw image 
    sepia(image)
    print("Close the image window to quit. ")
    image.draw() # to draw image
main()# calling main function
