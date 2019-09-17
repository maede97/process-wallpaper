from PIL import Image, ImageDraw, ImageFont
import os
import math
import psutil

width, height = 1920, 1080


im = Image.open("wc.png")
draw = ImageDraw.Draw(im, "RGBA")


# disk usage
lines = os.popen("df -BK").read().split("\n")
lines = [i.split(" ") for i in lines[1:]]
lines = [[i for i in line if i!=""] for line in lines][:-1]

# line = [filesystem, 1K-blocks, used, available, use%, mounted on]
percents = [int(line[4][:-1]) for line in lines]

pos_x, pos_y = (1700, 870)
r = 150

abstand = r * 2 + 50

font = ImageFont.truetype('/usr/share/fonts/TTF/VeraMono.ttf', 32)

curr = 0
for p in percents:
    angle = 360 * p / 100
    draw.pieslice([pos_x - r, pos_y -r, pos_x + r, pos_y + r], curr, curr + angle, "#ff000077")
    curr = curr + angle
draw.pieslice([pos_x - r, pos_y -r, pos_x + r, pos_y + r], curr, 360, "#00ff0077")
text = "Disk Usage"
w,h = draw.textsize(text, font=font)
draw.text([pos_x -w/2, pos_y - h/2], text, "black", font=font)


# CPU
percent = psutil.cpu_percent() * 360 / 100

draw.pieslice([pos_x - r, pos_y - r - abstand, pos_x + r, pos_y + r - abstand], 0, percent, "#ff000077")
draw.pieslice([pos_x - r, pos_y - r - abstand, pos_x + r, pos_y + r - abstand], percent, 360, "#00ff0077")
text = "CPU"
w,h = draw.textsize(text, font=font)
draw.text([pos_x - w/2, pos_y - h/2 - abstand], text, "black", font=font)

# memory
percent = psutil.virtual_memory().percent * 360 / 100

draw.pieslice([pos_x - r, pos_y - r - 2*abstand, pos_x + r, pos_y + r - 2*abstand], 0, percent, "#ff000077")
draw.pieslice([pos_x - r, pos_y - r - 2*abstand, pos_x + r, pos_y + r - 2*abstand], percent, 360, "#00ff0077")
text = "Memory"
w,h = draw.textsize(text, font=font)
draw.text([pos_x - w/2, pos_y - h/2 - 2*abstand], text, "black", font=font)


im.save("wallpaper.png")