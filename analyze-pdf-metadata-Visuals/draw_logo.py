#!/usr/bin/env python3
"""analyze-pdf-metadata logo: a customs shed padlock front on, heavy tar black iron rectangle with corners knocked
soft, foam white steel shackle arched above worn bright at the grip, one lantern amber inspection stripe running
diagonally from lower left to upper right unbroken over the seam between body and hasp, keyhole a clean dark
circle with a short slot below centre. Name in Azeret Mono in foam white on deep sea teal below, letters evenly
spaced like entries typed onto a manifest line."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 900, 520
TEAL = (10, 52, 58); AMBER = (232, 164, 60); FOAM = (232, 238, 230); TAR = (13, 12, 11)
img = Image.new("RGB", (W, H), TEAL); d = ImageDraw.Draw(img, "RGBA")
cx = 450
# shackle: foam white steel arch, legs running down behind the body, bright where hands grip at the crown
d.arc([cx - 108, 52, cx + 108, 340], 180, 360, fill=(198, 204, 200), width=34)
d.arc([cx - 108, 52, cx + 108, 340], 205, 335, fill=(244, 248, 244), width=12)  # worn bright grip
# body: heavy rectangle, corners knocked soft, drawn over the shackle legs so the arch seats into it
d.rounded_rectangle([cx - 168, 196, cx + 168, 402], 26, fill=TAR, outline=(64, 60, 54), width=3)
for (x, y) in [(cx - 150, 214), (cx + 138, 226), (cx - 142, 380), (cx + 146, 372)]:  # handling wear at the corners
    d.ellipse([x - 8, y - 5, x + 8, y + 5], fill=(52, 48, 42))
# the inspection stripe, diagonal lower left to upper right, continuing over the body and hasp seam
if A == "--v1":  # v1 flaw: stripe broken at the seam, two offset segments, the seal reads as already tampered
    d.polygon([(cx - 168, 356), (cx + 60, 196), (cx + 118, 196), (cx - 110, 402), (cx - 168, 402)], fill=AMBER)
    d.rectangle([cx - 168, 286, cx + 168, 302], fill=TAR)
else:
    d.polygon([(cx - 168, 356), (cx + 60, 196), (cx + 118, 196), (cx - 110, 402), (cx - 168, 402)], fill=AMBER)
d.rounded_rectangle([cx - 44, 182, cx + 44, 228], 8, outline=(150, 142, 128), width=2)  # hasp plate outline only, stripe runs unbroken beneath it
# keyhole: one clean dark circle with a short slot beneath it, below centre
d.ellipse([cx - 17, 292, cx + 17, 326], fill=(0, 0, 0), outline=(110, 104, 94), width=2)
d.polygon([(cx - 8, 318), (cx + 8, 318), (cx + 11, 352), (cx - 11, 352)], fill=(0, 0, 0), outline=(110, 104, 94), width=1)
# name in Azeret Mono, foam white, even manifest spacing
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/AzeretMono.ttf", 37)
except Exception:
    f = ImageFont.load_default()
name = "analyze-pdf-metadata"
if A == "--v2":  # v2 flaw: cramped proportional setting, no manifest discipline
    d.text((450, 458), name, font=f, fill=FOAM, anchor="mm")
else:
    total = sum(d.textlength(c, font=f) for c in name) + 6 * (len(name) - 1)
    x = 450 - total / 2
    for c in name:
        d.text((x, 458), c, font=f, fill=FOAM, anchor="lm"); x += d.textlength(c, font=f) + 6
img = img.filter(ImageFilter.GaussianBlur(0.3))
out = {"--v1": "scratch/logo-v1.png", "--v2": "scratch/logo-v2.png"}.get(A, "logo.png")
img.save(__file__.rsplit("/", 1)[0] + "/" + out)
if A == "":
    img.resize((64, 37)).save(__file__.rsplit("/", 1)[0] + "/scratch/logo64-ship.png")
print("saved", out)
