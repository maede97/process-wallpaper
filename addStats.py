from PIL import Image, ImageDraw
import os
import math

width, height = 1920, 1080


im = Image.open("wc.png")
draw = ImageDraw.Draw(im, "RGBA")


# add disk usage
lines = os.popen("df -BK").read().split("\n")
lines = [i.split(" ") for i in lines[1:]]
lines = [[i for i in line if i!=""] for line in lines][:-1]

# line = [filesystem, 1K-blocks, used, available, use%, mounted on]
percents = [int(line[4][:-1]) for line in lines]

pos_x, pos_y = (1700, 870)
r = 150

curr = 0
for p in percents:
    angle = 360 * p / 100
    draw.pieslice([pos_x - r, pos_y -r, pos_x + r, pos_y + r], curr, curr + angle, "#ff000077")
    curr = curr + angle
draw.pieslice([pos_x - r, pos_y -r, pos_x + r, pos_y + r], curr, 360, "#00ff0077")










im.save("wallpaper.png")