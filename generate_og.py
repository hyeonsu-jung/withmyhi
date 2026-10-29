from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
out = Image.new("RGB", (W, H), "#fbf2ed")
pixels = out.load()
top, bottom = (255, 249, 245), (247, 234, 226)
for y in range(H):
    t = y / (H - 1)
    color = tuple(round(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
    for x in range(W):
        pixels[x, y] = color

draw = ImageDraw.Draw(out)
font_dir = r"C:\Windows\Fonts"
def font(name, size):
    return ImageFont.truetype(f"{font_dir}\\{name}", size)

regular = font("NotoSansKR-Regular.ttf", 22)
medium = font("NotoSansKR-Medium.ttf", 22)
bold = font("NotoSansKR-Medium.ttf", 58)
small = font("NotoSansKR-Medium.ttf", 17)

def star(cx, cy, radius, color):
    points = []
    for i in range(8):
        angle = -90 + i * 45
        r = radius if i % 2 == 0 else radius * .24
        from math import cos, sin, radians
        points.append((cx + cos(radians(angle)) * r, cy + sin(radians(angle)) * r))
    draw.polygon(points, fill=color)

def heart(cx, cy, size, color):
    draw.ellipse((cx - size, cy - size * .55, cx, cy + size * .35), fill=color)
    draw.ellipse((cx, cy - size * .55, cx + size, cy + size * .35), fill=color)
    draw.polygon(( (cx - size, cy), (cx + size, cy), (cx, cy + size * 1.35) ), fill=color)

# Soft background accents
draw.ellipse((880, -190, 1320, 250), fill="#f8e1d8")
draw.ellipse((-145, 440, 170, 755), fill="#f6e4dc")

# Main paper card and subtle shadow
draw.rounded_rectangle((42, 34, 1158, 596), radius=42, fill="#e9d9d0")
draw.rounded_rectangle((38, 28, 1154, 588), radius=42, fill="#fffdfa", outline="#f0e3dc", width=2)

# Brand wordmark
brand = "WITH.MY.HI"
bx, by = 102, 90
for letter in brand:
    draw.text((bx, by), letter, font=font("Pretendard-SemiBold.ttf", 23), fill="#745c54")
    bx += draw.textlength(letter, font=font("Pretendard-SemiBold.ttf", 23)) + 3

# Headline and description
draw.rounded_rectangle((102, 145, 330, 184), radius=20, fill="#fff0e9")
draw.text((120, 153), "엄마의 다정한 추천 노트", font=small, fill="#b77668")
draw.text((98, 213), "작은 발견,", font=bold, fill="#382e2a", stroke_width=0)
draw.text((98, 287), "진짜 추천", font=bold, fill="#382e2a", stroke_width=0)
draw.text((103, 385), "엄마의 하루를 조금 더 편하게", font=regular, fill="#776760")
draw.text((103, 420), "직접 써보고 고른 육아 아이템을 모았어요.", font=regular, fill="#776760")

# Small signature capsule
draw.rounded_rectangle((102, 489, 410, 539), radius=25, fill="#fbf5f1", outline="#efe3dc", width=1)
draw.ellipse((119, 504, 140, 525), fill="#eea091")
heart(129.5, 513.5, 4.3, "#fff")
draw.text((152, 499), "WITH LOVE, WITH.MY.HI", font=font("Pretendard-SemiBold.ttf", 15), fill="#80665d")

# Warm illustrated spotlight
draw.ellipse((695, 92, 1118, 515), fill="#fae9e1")
draw.ellipse((751, 116, 1065, 430), fill="#f4d9ce")
draw.ellipse((780, 130, 1042, 392), fill="#fffaf6", outline="#fff", width=7)

# A simple, friendly face illustration
draw.ellipse((823, 175, 1000, 352), fill="#f7d0b8")
draw.ellipse((817, 159, 1006, 292), fill="#493a35")
draw.ellipse((828, 204, 997, 361), fill="#f7d0b8")
draw.ellipse((842, 202, 875, 241), fill="#493a35")
draw.ellipse((950, 207, 980, 244), fill="#493a35")
draw.ellipse((851, 229, 865, 243), fill="#302724")
draw.ellipse((958, 233, 972, 247), fill="#302724")
draw.ellipse((831, 259, 864, 279), fill="#eea59b")
draw.ellipse((963, 263, 995, 283), fill="#eea59b")
draw.arc((887, 258, 941, 300), start=15, end=165, fill="#a95652", width=4)

# Little star and heart stickers around the portrait
star(753, 211, 17, "#e8ad76")
star(1039, 214, 13, "#e89a8a")
heart(770, 363, 13, "#e99284")
star(1032, 360, 15, "#d6a966")

# Recommendation card layered over the illustration
draw.rounded_rectangle((742, 406, 1093, 526), radius=24, fill="#e7d5cc")
draw.rounded_rectangle((735, 398, 1086, 518), radius=24, fill="#fffdfa", outline="#f0e4de", width=2)
draw.rounded_rectangle((756, 418, 831, 493), radius=17, fill="#f9ece3")
# Minimal diaper-pad and bottle silhouettes
draw.rounded_rectangle((773, 443, 815, 478), radius=6, fill="#fff")
draw.rounded_rectangle((780, 438, 809, 449), radius=4, fill="#d8cec4")
draw.line((781, 461, 807, 461), fill="#c9beb5", width=2)
draw.rounded_rectangle((818, 447, 828, 485), radius=4, fill="#8eaa82")
draw.rounded_rectangle((820, 439, 826, 450), radius=2, fill="#79936e")
draw.text((852, 422), "TODAY'S PICK", font=font("Pretendard-SemiBold.ttf", 13), fill="#bf8274")
draw.text((851, 447), "매일 손이 가는 아이템", font=medium, fill="#453833")
draw.text((852, 478), "직접 써보고 담았어요  ♡", font=font("NotoSansKR-Regular.ttf", 16), fill="#938079")

out.save("og-image.png", format="PNG", optimize=True)
