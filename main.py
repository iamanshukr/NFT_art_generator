#Importing pillow("PIL") library for image generation

from PIL import Image, ImageDraw, ImageChops
import random
import colorsys #this module help in defining "HSV: Hue Saturation Value" Google HSV.

#Defining a function

def random_color():
    
    h = random.random() #random give random no between 0 and 1
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h,s,v)
    
    rgb = [int(x*255) for x in float_rgb]

    return tuple(rgb)

def interpolate(Start_Color, End_color, factor: float):
    recip = 1- factor
    return (
        int(Start_Color[0] * recip + End_color[0] * factor),
        int(Start_Color[1] * recip + End_color[1] * factor),
        int(Start_Color[1] * recip + End_color[2] * factor),
    )

def generate_art(path: str):
    print("Your NFT art has been generated")
    
    target_size = 256
    scale_factor = 2 
    img_size = target_size * scale_factor #(128,128) is the size LXB 
    padding_px = round(img_size*0.10)
    Start_Color = random_color()
    End_color = random_color()
    img_background_colour = (0,0,0) #(0,0,0) is the amount of Red, Green or Blue i want.

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
            random.randint(padding_px, img_size-padding_px), 
            random.randint(padding_px, img_size-padding_px),
        )
        points.append(random_point)
    
    #Draw the bounding borders

    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    # dimensions_box = min_x, min_y, max_x, max_y
    # draw.rectangle(dimensions_box, outline=(255,0,0))

    # Center the image
    
    delta_x = min_x - (img_size - max_x)
    delta_y = min_y - (img_size - max_y)
    
    for i, point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1]- delta_y // 2)

    # min_x = min([p[0] for p in points])
    # max_x = max([p[0] for p in points])
    # min_y = min([p[1] for p in points])
    # max_y = max([p[1] for p in points])
    # dimensions_box = min_x, min_y, max_x, max_y
    # draw.rectangle(dimensions_box, outline=(210,210,210))


    #Draw the points
    thickness = 0
    n_points = len(points) - 1
    for i, point in enumerate(points):

        #Overlay canvas
        overlay_image = Image.new("RGB",size= (img_size,img_size),color= img_background_colour)
        overlay_draw = ImageDraw.Draw(overlay_image)
        p1 = point

        if i == n_points:
            p2 = points[0]
        else:
            p2 = points[i + 1]
        
        line_xy = (p1,p2) #coordination of the line on the image
        color_factor = i / n_points
        line_color = interpolate(Start_Color, End_color,color_factor) # defining the colour
        thickness += scale_factor
        overlay_draw.line (line_xy,fill=line_color, width= thickness)
        img = ImageChops.add(img,overlay_image)
    
    img = img.resize([target_size, target_size], resample=Image.ANTIALIAS)
    img.save(path) #() give the name of the file

# n = int(input("Enter number of images: \n "))
for i in range(1):
    generate_art(f"test_img{i}.png")
