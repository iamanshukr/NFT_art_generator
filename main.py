#Importing pillow("PIL") library for image generation

from PIL import Image, ImageDraw
import random

#Defining a function

def generate_art():
    print("Your NFT art has been generated")
    
    img_size = 128 #(128,128) is the size LXB 
    img_background_colour = (255,255,255) #(255,255,255) is the amount of Red, Green or Blue i want.

    img = Image.new(
        "RGB", 
        size= (img_size,img_size),
        color= img_background_colour) #RGB is the mode
    
    #Draw some lines
    draw = ImageDraw.Draw(img)

    points = []

    #Generates the points
    for _ in range(10):
        
        random_point = (
            random.randint(0, img_size), 
            random.randint(0, img_size),
        )
        points.append(random_point)
    
    #Draw the points
    for i, point in enumerate(points):
        
        p1 = point

        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i + 1]
        
        line_xy = (p1,p2) #coordination of the line on the image
        line_color = (0,0,0) # defining the colour
        draw.line (line_xy,fill=line_color) 

    img.save("test_img.png") #() give the name of the file


generate_art()