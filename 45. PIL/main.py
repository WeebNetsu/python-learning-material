# image filter will allow us to blur images and ImageDraw allows us to put text on image
# ImageFont allows us to add text to image
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os # to loop over the files in a directory {NO NEED FOR TUTORIAL!!}

# Basics, displaying and saving images
# imgFace = Image.open("images/face.png")
# imgFace.show() # displays the image to the screen
# imgFace.save("images/face.jpg") # creates a jpg version of the image

# Other manipulation methods
imgFace = Image.open("images/face.jpg")
# rotate image 45 degrees
imgFace.rotate(45).save("images/manipulated/face_rotated.jpg")
# make image black and white
imgFace.convert(mode="L").save("images/manipulated/face_bnw.jpg")
# blur an image (GaussianBlur(15) will make the image more blurry (default=2))
imgFace.filter(ImageFilter.GaussianBlur()).save("images/manipulated/face_blurred.jpg")

# resizing images
# image_size = (300, 300)
# image.thumbnail(image_size) # creates a resized verion of the image

draw = ImageDraw.Draw(imgFace)
font = ImageFont.truetype("fonts/title_font.ttf", 20)
draw.text(
    (0, 0),  # Coordinates
    'Hello world!',  # Text
    (0, 0, 0),  # Color
    font=font
)
imgFace.save("images/manipulated/face_drawn.jpg")

# DO NOT PUT BELOW IN TUTORIAL
# looping through images and editing multiple of them
for file in os.listdir("images/"): # gets all items inside images folder
    if file.endswith(".jpg"): # gets files that ends in .jpg
        image = Image.open(f"images/{file}") # creates image object
        fileName, _ = os.path.splitext(file) # gets fileName and extension
        image.save(f"images/png/{fileName}.png")
        # print(fileName)

# resizing images
image_size = (300, 300)

for file in os.listdir("images/"):
    if file.endswith(".jpg"):
        # print(file)
        image = Image.open(f"images/{file}")
        image.thumbnail(image_size) # creates a resized verion of the image
        image.save(f"images/resized/{file}")