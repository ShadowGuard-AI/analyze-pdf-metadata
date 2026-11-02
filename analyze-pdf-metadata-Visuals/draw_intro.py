#!/usr/bin/env python3
"""analyze-pdf-metadata intro: night wharf with nothing readable in it. Wet tar black quay stones close in the
foreground, the lowest tarred barrel filling the lower right, the customs shed midground with its door closed,
chain drawn across and padlock hanging still with its amber inspection stripe, rolled charts tied in a crate,
a second barrel row receding, black water in deep sea teal, a moored hull with a pale waterline, limp signal
flags, distant shore lantern points, no moon. Lantern light pools and stops."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(53)
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1200, 520
TEAL = (10, 52, 58); AMBER = (232, 164, 60); TAR = (14, 13, 12); FOAM = (232, 238, 230)
img = Image.new("RGB", (W, H), (6, 22, 28)); d = ImageDraw.Draw(img, "RGBA")
# sky with no moon, far shore reduced to lantern points
d.rectangle([0, 0, W, 150], fill=(5, 16, 22))
for x in (820, 905, 1010, 1120):
    d.ellipse([x - 3, 128, x + 3, 134], fill=(250, 200, 110))
    d.ellipse([x - 9, 122, x + 9, 140], fill=(250, 200, 110, 40))
# black water in deep sea teal behind the quay
d.rectangle([0, 150, W, 330], fill=TEAL)
for _ in range(120):
    x, y = random.uniform(560, 1200), random.uniform(160, 320)
    d.line([(x, y), (x + random.uniform(8, 30), y)], fill=(30, 92, 98), width=2)
# moored hull with a foam white waterline, limp signal flags in the rigging
d.polygon([(700, 236), (1130, 236), (1080, 292), (740, 292)], fill=(18, 20, 20))
d.line([(700, 252), (1118, 252)], fill=FOAM, width=5)  # pale waterline
d.line([(880, 236), (880, 120)], fill=(40, 38, 34), width=4)  # mast
d.line([(880, 126), (1010, 210)], fill=(60, 58, 50), width=2)  # rigging
for i, c in enumerate([(190, 70, 60), (232, 200, 90), (90, 130, 180)]):  # flags hanging limp, straight down
    x = 906 + i * 34
    d.polygon([(x, 138 + i * 10), (x + 20, 142 + i * 10), (x + 18, 168 + i * 10), (x + 2, 164 + i * 10)], fill=c)
# quay stones at close range, wet at the edges
d.polygon([(0, 318), (1200, 292), (1200, H), (0, H)], fill=(26, 24, 22))
for row in range(4):
    y = 336 + row * 46
    for i in range(7):
        x = i * 180 + (row % 2) * 80
        d.rounded_rectangle([x + 6, y, x + 168, y + 36], 8, outline=(58, 54, 48), width=2)
        d.line([(x + 14, y + 30), (x + 90, y + 30)], fill=(70, 84, 88, 90), width=3)  # wet sheen
# customs shed occupying the left midground, door closed
d.polygon([(70, 196), (300, 172), (300, 420), (70, 420)], fill=(30, 26, 22))
d.polygon([(52, 200), (318, 200), (276, 150), (96, 150)], fill=(20, 18, 16))  # roof
d.rectangle([128, 226, 246, 420], fill=(38, 32, 26))  # the shut door, tarred wood
for x in range(140, 240, 24):
    d.line([(x, 232), (x, 414)], fill=(28, 24, 20), width=3)
# compass rose painted on the gable end, faded and decorative, no letters on it
cxr, cyr = 186, 182
for a in range(0, 360, 45):
    r = math.radians(a); ln = 17 if a % 90 == 0 else 11
    d.line([(cxr, cyr), (cxr + math.cos(r) * ln, cyr + math.sin(r) * ln)], fill=(200, 180, 130, 110), width=2)
d.ellipse([cxr - 3, cyr - 3, cxr + 3, cyr + 3], fill=(200, 180, 130, 110))
# chain drawn across the door and the padlock hanging still at centre
for i in range(9):
    x = 132 + i * 13
    d.ellipse([x, 308 + (4 if i % 2 else 0), x + 14, 322 + (4 if i % 2 else 0)], outline=(150, 150, 148), width=3)
lkx, lky = 178, 318
d.arc([lkx - 16, lky - 20, lkx + 16, lky + 14], 180, 360, fill=(216, 220, 218), width=6)  # shackle
d.rounded_rectangle([lkx - 24, lky + 2, lkx + 24, lky + 52], 6, fill=(12, 11, 10), outline=(70, 66, 60), width=2)
if A != "--v2":  # v2 flaw: the amber inspection stripe missing, the seal cannot be read at all
    d.polygon([(lkx - 24, lky + 40), (lkx + 10, lky + 2), (lkx + 24, lky + 2), (lkx - 10, lky + 52), (lkx - 24, lky + 52)], fill=AMBER)
d.ellipse([lkx - 5, lky + 22, lkx + 5, lky + 32], fill=(0, 0, 0), outline=(90, 86, 78))
# rolled charts tied upright in an open crate beside the shed wall
d.rectangle([330, 356, 404, 420], fill=(52, 40, 28)); d.rectangle([330, 356, 404, 368], fill=(66, 52, 36))
for i, x in enumerate((344, 362, 380)):
    d.rectangle([x, 306 + (i % 2) * 8, x + 12, 360], fill=(226, 220, 200))
    d.rectangle([x, 330 + (i % 2) * 8, x + 12, 338 + (i % 2) * 8], fill=TEAL)
# tarred barrels in two rows receding toward the harbor edge
def barrel(x, y, s):
    w, h = 74 * s, 96 * s
    d.rounded_rectangle([x, y, x + w, y + h], int(10 * s), fill=(24, 20, 17))
    for t in (.22, .5, .78):
        d.line([(x + 3, y + h * t), (x + w - 3, y + h * t)], fill=(168, 150, 110), width=max(2, int(3 * s)))
    d.line([(x + w * .3, y + 4), (x + w * .3, y + h - 4)], fill=(14, 12, 10), width=max(2, int(4 * s)))
    d.line([(x + w * .68, y + 4), (x + w * .68, y + h - 4)], fill=(14, 12, 10), width=max(2, int(4 * s)))
for i in range(4):  # second row receding
    barrel(470 + i * 96, 268 - i * 4, .82 - i * .07)
for i in range(3):  # front row
    barrel(452 + i * 128, 330, 1.0)
if A != "--v1":  # v1 flaw: the lowest barrel of the front row missing from the lower right corner
    d.rounded_rectangle([1006, 372, 1200, 540], 26, fill=(24, 20, 17))
    for t in (.18, .44, .7):
        d.line([(1012, 372 + 168 * t), (1196, 372 + 168 * t)], fill=(178, 158, 116), width=5)
    d.line([(1080, 380), (1080, 532)], fill=(14, 12, 10), width=7)
# lantern pools: bright near each lamp and gone within a few yards
for (x, y, r) in [(110, 240, 120), (430, 320, 100), (760, 268, 84)]:
    for rr in range(r, 0, -14):
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(250, 196, 96, 7))
    d.rectangle([x - 5, y - 14, x + 5, y + 8], fill=(30, 26, 20), outline=AMBER, width=2)
    d.ellipse([x - 3, y - 8, x + 3, y - 2], fill=(255, 220, 130))
# amber glint on the lock from the nearest lantern
d.ellipse([lkx - 30, lky - 6, lkx + 30, lky + 58], outline=(250, 196, 96, 60), width=2)
img = img.filter(ImageFilter.GaussianBlur(0.5))
out = {"--v1": "scratch/intro-v1.png", "--v2": "scratch/intro-v2.png"}.get(A, "intro-banner.png")
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
