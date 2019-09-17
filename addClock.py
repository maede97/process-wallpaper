from PIL import Image, ImageDraw
import datetime
import math


# settings
width, height = 1920, 1080
big_pointer_color = "#ff000077"
small_pointer_color = "#00ff0077"
big_pointer_length = 400
small_pointer_lenght = 480
radius = 500

line_inner_point = radius - 20
# end settings

def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))

im = Image.open("wc.png")
draw = ImageDraw.Draw(im, "RGBA")

curr_time = datetime.datetime.now()

hour = curr_time.hour % 12
minute = curr_time.minute

angle_hour = hour * 30 + minute * 0.5 + 90
angle_minute = minute * 6 + 90

# zeiger
draw.line([(width/2,height/2),(width/2 - big_pointer_length * cos(angle_hour), height/2 - big_pointer_length*sin(angle_hour))], big_pointer_color, 10)
draw.line([(width/2,height/2),(width/2 - small_pointer_lenght * cos(angle_minute), height/2 - small_pointer_lenght*sin(angle_minute))], small_pointer_color, 5)

# kreis
draw.ellipse([(width / 2 - radius, height / 2 - radius), (width/ 2 + radius, height/2 + radius)], None,"#ffffff77", 5)

# striche
for i in range(0, 359, 30):
    draw.line([(width/2 - line_inner_point * cos(i), height/2 - line_inner_point*sin(i)),
        (width/2 - radius * cos(i), height/2 - radius*sin(i))], "#ffffff77",7)


im.save("wc.png")