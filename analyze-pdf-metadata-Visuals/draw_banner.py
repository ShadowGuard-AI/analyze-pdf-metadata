#!/usr/bin/env python3
"""analyze-pdf-metadata wordmark banner: working wharf at night under lanterns, customs shed at the left third
with its door shut and chained, the padlock catching lantern amber, tarred barrels ranked in two rows, rolled
charts tied upright in an open crate, anchor chain links running from a bollard at the quay edge down into black
water, harbor in deep sea teal beyond with one moored hull at a foam white waterline and limp signal flags, a
faded compass rose on the shed gable, and the project name chalked in Azeret Mono in foam white across the shed
door itself, one line only and no other writing on the wharf."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(31)
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1200, 420
TEAL = (10, 52, 58); AMBER = (232, 164, 60); FOAM = (232, 238, 230)
img = Image.new("RGB", (W, H), (6, 22, 28)); d = ImageDraw.Draw(img, "RGBA")
d.rectangle([0, 96, W, 268], fill=TEAL)  # harbor
for _ in range(90):
    x, y = random.uniform(480, 1200), random.uniform(120, 250)
    d.line([(x, y), (x + random.uniform(8, 26), y)], fill=(30, 92, 98), width=2)
# moored hull, foam white waterline, limp flags
d.polygon([(760, 196), (1150, 196), (1108, 240), (796, 240)], fill=(18, 20, 20))
d.line([(762, 208), (1144, 208)], fill=FOAM, width=4)
d.line([(950, 196), (950, 96)], fill=(40, 38, 34), width=4)
for i, c in enumerate([(190, 70, 60), (232, 200, 90), (90, 130, 180)]):
    x = 972 + i * 30
    d.polygon([(x, 108 + i * 8), (x + 17, 111 + i * 8), (x + 15, 132 + i * 8), (x + 2, 129 + i * 8)], fill=c)
for x in (1060, 1130):  # far shore lantern points
    d.ellipse([x - 3, 108, x + 3, 114], fill=(250, 200, 110))
# quay
d.polygon([(0, 258), (1200, 240), (1200, H), (0, H)], fill=(26, 24, 22))
for row in range(3):
    y = 276 + row * 44
    for i in range(7):
        x = i * 182 + (row % 2) * 80
        d.rounded_rectangle([x + 6, y, x + 168, y + 34], 8, outline=(58, 54, 48), width=2)
# customs shed, left third
d.polygon([(36, 168), (392, 146), (392, 356), (36, 356)], fill=(30, 26, 22))
d.polygon([(20, 172), (408, 172), (356, 118), (72, 118)], fill=(20, 18, 16))
d.rectangle([88, 196, 338, 356], fill=(38, 32, 26))  # shed door
for x in range(102, 330, 26):
    d.line([(x, 202), (x, 350)], fill=(28, 24, 20), width=3)
# faded compass rose on the gable end, decorative, no letters
cxr, cyr = 214, 138
for a in range(0, 360, 45):
    r = math.radians(a); ln = 15 if a % 90 == 0 else 10
    d.line([(cxr, cyr), (cxr + math.cos(r) * ln, cyr + math.sin(r) * ln)], fill=(200, 180, 130, 100), width=2)
# chain across the door, padlock at centre catching the amber
for i in range(15):
    x = 96 + i * 16
    d.ellipse([x, 262 + (4 if i % 2 else 0), x + 16, 276 + (4 if i % 2 else 0)], outline=(150, 150, 148), width=3)
lkx, lky = 206, 272
d.arc([lkx - 18, lky - 22, lkx + 18, lky + 16], 180, 360, fill=(216, 220, 218), width=7)
d.rounded_rectangle([lkx - 27, lky + 2, lkx + 27, lky + 58], 6, fill=(12, 11, 10), outline=(70, 66, 60), width=2)
d.polygon([(lkx - 27, lky + 44), (lkx + 12, lky + 2), (lkx + 27, lky + 2), (lkx - 12, lky + 58), (lkx - 27, lky + 58)], fill=AMBER)
d.ellipse([lkx - 5, lky + 24, lkx + 5, lky + 34], fill=(0, 0, 0))
# name chalked across the shed door in Azeret Mono, foam white, slightly uneven chalk pressure
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/AzeretMono.ttf", 19)
except Exception:
    f = ImageFont.load_default()
if A == "--v1":  # v1 flaw: name painted on a signboard hung beside the shed, not chalked on the door it guards
    d.rectangle([430, 120, 800, 176], fill=(52, 44, 34), outline=(90, 78, 58), width=3)
    d.text((615, 148), "analyze-pdf-metadata", font=f, fill=FOAM, anchor="mm")
elif A == "--v2":  # v2 flaw: chalk line floats above the door on the gable, detached from the lock and chain
    d.text((213, 92), "analyze-pdf-metadata", font=f, fill=FOAM, anchor="mm")
else:
    name = "analyze-pdf-metadata"
    x = 213 - d.textlength(name, font=f) / 2; y = 216
    for i, c in enumerate(name):
        d.text((x, y + (2 if i % 5 == 3 else 0)), c, font=f, fill=(232, 238, 230, 235), anchor="lm")
        x += d.textlength(c, font=f) + 1
    for _ in range(30):  # chalk dust under the line
        d.point((random.uniform(96, 330), random.uniform(240, 248)), fill=(220, 224, 218))
# rolled charts in their crate beside the shed wall
d.rectangle([424, 300, 488, 356], fill=(52, 40, 28)); d.rectangle([424, 300, 488, 311], fill=(66, 52, 36))
for i, x in enumerate((436, 452, 468)):
    d.rectangle([x, 258 + (i % 2) * 7, x + 11, 304], fill=(226, 220, 200))
    d.rectangle([x, 280 + (i % 2) * 7, x + 11, 287 + (i % 2) * 7], fill=TEAL)
# barrels ranked in two rows awaiting inspection
def barrel(x, y, s):
    w, h = 70 * s, 92 * s
    d.rounded_rectangle([x, y, x + w, y + h], int(9 * s), fill=(24, 20, 17))
    for t in (.22, .5, .78):
        d.line([(x + 3, y + h * t), (x + w - 3, y + h * t)], fill=(168, 150, 110), width=max(2, int(3 * s)))
for i in range(4):
    barrel(560 + i * 92, 226 - i * 3, .8 - i * .06)
for i in range(4):
    barrel(540 + i * 118, 282, 1.0)
# bollard at the quay edge with anchor chain links running down into black water
d.rounded_rectangle([1052, 292, 1096, 348], 10, fill=(34, 32, 30), outline=(80, 76, 68), width=2)
for i in range(5):
    x, y = 1074 - i * 4, 330 + i * 15
    d.ellipse([x - 11, y - 7, x + 11, y + 7], outline=(140, 140, 138), width=3)
# lantern pools
for (x, y, r) in [(70, 200, 104), (470, 268, 88), (820, 226, 72)]:
    for rr in range(r, 0, -13):
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(250, 196, 96, 7))
    d.rectangle([x - 5, y - 13, x + 5, y + 7], fill=(30, 26, 20), outline=AMBER, width=2)
    d.ellipse([x - 3, y - 7, x + 3, y - 1], fill=(255, 220, 130))
img = img.filter(ImageFilter.GaussianBlur(0.5))
out = {"--v1": "scratch/banner-v1.png", "--v2": "scratch/banner-v2.png"}.get(A, "banner.png")
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
