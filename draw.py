#!/usr/bin/env python3
"""Draw the news-image-01 entry: one infographic summing up Friday 13 November 2026.

Renders a 1024x1024 PNG with a header and six flat-illustration story tiles.
Run:  python3 draw.py            (writes entry.png next to this script)
Uses only Pillow and the DejaVu fonts present on this machine.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (19, 35, 63)
AMBER = (232, 163, 23)
PAPER = (247, 245, 240)
INK = (24, 28, 34)
GREY = (90, 96, 104)
CARD = (255, 255, 255)
BORDER = (214, 212, 206)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def center_text(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)


# ---------------------------------------------------------------- header
def draw_header(d):
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 152], fill=AMBER)
    center_text(d, W // 2, 18, "F R I D A Y   1 3   N O V E M B E R   2 0 2 6",
                font(BOLD, 25), AMBER)
    center_text(d, W // 2, 52, "THE WORLD TODAY", font(BOLD, 64), (255, 255, 255))
    center_text(d, W // 2, 122, "Six stories that defined the day",
                font(REG, 22), (196, 205, 220))


# ---------------------------------------------------------------- tile art
def art_huang(d, x, y, w, h):
    """Empty Senate witness chair with a green Nvidia chip on the desk."""
    d.rectangle([x, y, x + w, y + h], fill=(230, 242, 230))
    # hearing desk
    d.rectangle([x + 18, y + h - 58, x + w - 18, y + h - 20], fill=(122, 84, 52))
    d.rectangle([x + 18, y + h - 58, x + w - 18, y + h - 48], fill=(146, 104, 66))
    # chair: legs, seat, backrest in mid brown
    cx = x + w // 2
    d.rectangle([cx - 58, y + 112, cx - 48, y + h - 58], fill=(58, 48, 40))
    d.rectangle([cx + 48, y + 112, cx + 58, y + h - 58], fill=(58, 48, 40))
    d.rectangle([cx - 58, y + 100, cx + 58, y + 116], fill=(94, 80, 66))
    d.rectangle([cx - 52, y + 30, cx + 52, y + 102], fill=(112, 94, 74))
    d.rectangle([cx - 44, y + 38, cx + 44, y + 94], fill=(130, 110, 88))
    # leather jacket draped over the top rail only, white shirt collar
    d.polygon([(cx - 52, y + 26), (cx + 52, y + 26), (cx + 46, y + 66), (cx - 46, y + 66)],
              fill=(28, 28, 32))
    d.polygon([(cx - 12, y + 26), (cx, y + 46), (cx + 12, y + 26)], fill=(240, 240, 240))
    # green chip on the desk, with a red downward arrow beside it
    cx2, cy = x + 56, y + h - 88
    d.rounded_rectangle([cx2 - 30, cy - 30, cx2 + 30, cy + 30], radius=8, fill=(30, 122, 52))
    d.rounded_rectangle([cx2 - 18, cy - 18, cx2 + 18, cy + 18], radius=5,
                        outline=(255, 255, 255), width=3)
    d.line([cx2 - 30, cy - 14, cx2 - 38, cy - 14], fill=(30, 122, 52), width=4)
    d.line([cx2 - 30, cy + 14, cx2 - 38, cy + 14], fill=(30, 122, 52), width=4)
    d.line([cx2 + 30, cy - 14, cx2 + 38, cy - 14], fill=(30, 122, 52), width=4)
    d.line([cx2 + 30, cy + 14, cx2 + 38, cy + 14], fill=(30, 122, 52), width=4)
    ax = cx2 + 66
    d.line([(ax, cy - 28), (ax, cy + 18)], fill=(201, 45, 45), width=7)
    d.polygon([(ax - 10, cy + 12), (ax + 10, cy + 12), (ax, cy + 30)], fill=(201, 45, 45))
    # microphone
    mx = x + w - 62
    d.ellipse([mx - 11, y + h - 108, mx + 11, y + h - 86], fill=(40, 40, 44))
    d.line([(mx, y + h - 86), (mx, y + h - 58)], fill=(40, 40, 44), width=5)


def art_talks(d, x, y, w, h):
    """Round table with three small flags: Ukraine, USA, EU."""
    d.rectangle([x, y, x + w, y + h], fill=(227, 236, 245))
    # table
    d.ellipse([x + 58, y + 118, x + w - 58, y + 168], fill=(146, 104, 66))
    d.rectangle([x + w // 2 - 12, y + 158, x + w // 2 + 12, y + h - 8], fill=(122, 84, 52))
    d.ellipse([x + 58, y + 112, x + w - 58, y + 158], fill=(176, 130, 84))
    # three flag poles with flags
    flags = [
        ("UA", [(0, 0, 120, 170), (255, 215, 0)]),   # blue over yellow
        ("US", [(178, 34, 34), (255, 255, 255)]),   # red/white stripes
        ("EU", [(0, 51, 153), (255, 215, 0)]),      # blue, gold stars
    ]
    fx = [x + 78, x + w // 2 - 24, x + w - 126]
    for (label, bands), fx0 in zip(flags, fx):
        d.line([(fx0 + 24, y + 30), (fx0 + 24, y + 116)], fill=(80, 70, 60), width=4)
        d.rectangle([fx0, y + 30, fx0 + 48, y + 52], fill=bands[0])
        d.rectangle([fx0, y + 52, fx0 + 48, y + 74], fill=bands[1])
        if label == "US":
            for sy in (34, 44, 54, 64):
                d.rectangle([fx0, y + sy, fx0 + 48, y + sy + 5], fill=(178, 34, 34))
            d.rectangle([fx0, y + 30, fx0 + 20, y + 50], fill=(30, 50, 110))
        if label == "EU":
            for sx, sy in ((10, 40), (24, 36), (38, 40), (10, 52), (38, 52), (24, 58)):
                d.ellipse([fx0 + sx, y + sy, fx0 + sx + 5, y + sy + 5], fill=(255, 215, 0))
    # handshake resting on the table: two clasped hands
    hx, hy = x + w // 2, y + 134
    d.ellipse([hx - 44, hy - 12, hx - 4, hy + 14], fill=(232, 190, 150))
    d.ellipse([hx + 4, hy - 12, hx + 44, hy + 14], fill=(198, 152, 112))
    d.ellipse([hx - 16, hy - 6, hx + 16, hy + 10], fill=(214, 172, 132))


def art_warship(d, x, y, w, h):
    """Grey warship on a cold sea, smoke rising, small drone above."""
    d.rectangle([x, y, x + w, y + h], fill=(223, 231, 236))
    # sky + smoke
    for i, r in enumerate((34, 26, 18)):
        d.ellipse([x + w - 150 + i * 6, y + 6 + i * 16, x + w - 150 + i * 6 + r * 2,
                   y + 6 + i * 16 + r * 2], fill=(150, 156, 162))
    # sea
    d.rectangle([x, y + 128, x + w, y + h], fill=(127, 168, 188))
    d.line([(x + 14, y + 152), (x + 90, y + 152)], fill=(255, 255, 255), width=3)
    d.line([(x + w - 120, y + 168), (x + w - 30, y + 168)], fill=(255, 255, 255), width=3)
    d.line([(x + 100, y + 176), (x + 210, y + 176)], fill=(255, 255, 255), width=3)
    # warship hull + superstructure
    d.polygon([(x + 34, y + 128), (x + w - 34, y + 128), (x + w - 66, y + 158),
               (x + 66, y + 158)], fill=(74, 85, 96))
    d.rectangle([x + 96, y + 100, x + w - 150, y + 128], fill=(90, 101, 112))
    d.rectangle([x + 150, y + 82, x + 176, y + 100], fill=(90, 101, 112))
    d.line([(x + 163, y + 82), (x + 163, y + 62)], fill=(74, 85, 96), width=4)
    d.line([(x + w - 120, y + 100), (x + w - 120, y + 78)], fill=(74, 85, 96), width=4)
    # fire + smoke at the stern
    d.polygon([(x + w - 74, y + 128), (x + w - 52, y + 96), (x + w - 30, y + 128)],
              fill=(235, 130, 40))
    d.ellipse([x + w - 74, y + 66, x + w - 34, y + 106], fill=(170, 174, 178))
    d.ellipse([x + w - 92, y + 44, x + w - 58, y + 78], fill=(150, 156, 162))
    # drone quadcopter
    dx, dy = x + 66, y + 44
    d.line([(dx - 22, dy - 10), (dx + 22, dy + 10)], fill=(40, 40, 44), width=4)
    d.line([(dx - 22, dy + 10), (dx + 22, dy - 10)], fill=(40, 40, 44), width=4)
    d.ellipse([dx - 8, dy - 8, dx + 8, dy + 8], fill=(40, 40, 44))
    d.ellipse([dx - 28, dy - 16, dx - 16, dy - 4], fill=(120, 124, 128))
    d.ellipse([dx + 16, dy + 4, dx + 28, dy + 16], fill=(120, 124, 128))


def art_radar(d, x, y, w, h):
    """Radar dome on a desert coast under a missile streak."""
    d.rectangle([x, y, x + w, y + h], fill=(191, 217, 232))
    # sun
    d.ellipse([x + w - 66, y + 14, x + w - 26, y + 54], fill=(245, 200, 90))
    # desert coast
    d.polygon([(x, y + 118), (x + w, y + 100), (x + w, y + h), (x, y + h)],
              fill=(217, 179, 128))
    d.rectangle([x, y + 128, x + w, y + h], fill=(210, 168, 116))
    # sea strip
    d.rectangle([x, y + 100, x + w, y + 118], fill=(110, 160, 190))
    # radar dome + dish on a base
    bx = x + w // 2 - 40
    d.rectangle([bx, y + 118, bx + 80, y + 150], fill=(140, 140, 138))
    d.pieslice([bx - 26, y + 34, bx + 106, y + 124], start=180, end=360, fill=(240, 240, 238))
    d.ellipse([bx - 26, y + 34, bx + 106, y + 124], outline=(180, 180, 178), width=3)
    d.line([(bx + 40, y + 80), (bx + 40, y + 118)], fill=(120, 120, 118), width=5)
    # missile streak ending at the dome's left edge, burst at the impact point
    ix, iy = x + 118, y + 92
    d.line([(x + 22, y + 22), (ix, iy)], fill=(235, 120, 40), width=7)
    d.line([(x + 22, y + 22), (ix, iy)], fill=(255, 220, 120), width=3)
    d.polygon([(ix, iy), (ix - 16, iy - 8), (ix - 8, iy + 12)], fill=(201, 60, 40))
    for ang in range(0, 360, 45):
        import math
        r0, r1 = 6, 17
        a = math.radians(ang)
        d.line([(ix + r0 * math.cos(a), iy + r0 * math.sin(a)),
                (ix + r1 * math.cos(a), iy + r1 * math.sin(a))],
               fill=(235, 130, 40), width=3)


def art_faa(d, x, y, w, h):
    """Airliner silhouette above a runway, red STOP octagon."""
    d.rectangle([x, y, x + w, y + h], fill=(224, 237, 247))
    # clouds
    for cx, cy in ((52, 30), (150, 52), (250, 26)):
        d.ellipse([x + cx, y + cy, x + cx + 44, y + cy + 16], fill=(255, 255, 255))
        d.ellipse([x + cx + 12, y + cy - 8, x + cx + 36, y + cy + 12], fill=(255, 255, 255))
    # runway
    d.rectangle([x, y + 138, x + w, y + h], fill=(120, 126, 132))
    for i in range(5):
        d.rectangle([x + 22 + i * 62, y + 158, x + 52 + i * 62, y + 166], fill=(255, 255, 255))
    # airliner
    px, py = x + 58, y + 78
    d.ellipse([px, py - 14, px + 170, py + 14], fill=(30, 50, 80))
    d.polygon([(px + 150, py - 10), (px + 196, py - 2), (px + 150, py + 8)], fill=(30, 50, 80))
    d.polygon([(px + 96, py - 14), (px + 128, py - 44), (px + 142, py - 14)], fill=(24, 42, 68))
    d.polygon([(px + 110, py + 10), (px + 132, py + 34), (px + 146, py + 10)], fill=(24, 42, 68))
    for wx in range(6):
        d.ellipse([px + 18 + wx * 18, py - 6, px + 26 + wx * 18, py + 2], fill=(180, 210, 235))
    # red STOP octagon
    ox, oy, r = x + w - 66, y + 44, 34
    pts = []
    import math
    for k in range(8):
        a = math.radians(22.5 + 45 * k)
        pts.append((ox + r * math.cos(a), oy + r * math.sin(a)))
    d.polygon(pts, fill=(192, 57, 43))
    d.polygon(pts, outline=(255, 255, 255), width=3)
    center_text(d, ox, oy - 13, "STOP", font(BOLD, 19), (255, 255, 255))


def art_kane(d, x, y, w, h):
    """Footballer in white on a green pitch, ball at his feet, big 126."""
    d.rectangle([x, y, x + w, y + h], fill=(228, 240, 220))
    # pitch
    d.rectangle([x, y + 118, x + w, y + h], fill=(62, 155, 79))
    d.rectangle([x, y + 118, x + w, y + 128], fill=(255, 255, 255))
    d.ellipse([x + w // 2 - 58, y + 118, x + w // 2 + 58, y + 122], fill=(255, 255, 255))
    # big 126 badge
    center_text(d, x + w - 66, y + 16, "126", font(BOLD, 52), (30, 90, 45))
    # footballer: head, white shirt, shorts, arms raised
    cx, cy = x + w // 2 - 40, y + 40
    d.ellipse([cx - 14, cy, cx + 14, cy + 28], fill=(232, 190, 150))          # head
    d.ellipse([cx - 14, cy - 4, cx + 14, cy + 12], fill=(60, 44, 30))         # hair
    d.line([(cx - 30, cy + 66), (cx - 52, cy + 30)], fill=(232, 190, 150), width=9)  # left arm up
    d.line([(cx + 30, cy + 66), (cx + 52, cy + 30)], fill=(232, 190, 150), width=9)  # right arm up
    d.polygon([(cx - 30, cy + 34), (cx + 30, cy + 34), (cx + 24, cy + 92),
               (cx - 24, cy + 92)], fill=(255, 255, 255))                      # shirt
    d.rectangle([cx - 24, cy + 92, cx + 24, cy + 108], fill=(20, 40, 90))     # shorts
    d.line([(cx - 14, cy + 108), (cx - 20, cy + 138)], fill=(232, 190, 150), width=9)
    d.line([(cx + 14, cy + 108), (cx + 30, cy + 128)], fill=(232, 190, 150), width=9)
    # ball
    bx, by = x + w // 2 + 52, y + 148
    d.ellipse([bx - 15, by - 15, bx + 15, by + 15], fill=(255, 255, 255))
    d.polygon([(bx, by - 7), (bx + 7, by - 2), (bx + 4, by + 6), (bx - 4, by + 6),
               (bx - 7, by - 2)], fill=(30, 30, 34))


# ---------------------------------------------------------------- tiles
STORIES = [
    ("TECH · USA", "SENATE CALLS HUANG",
     "Ex-Nvidia chief called to testify a day after quitting in scandal.",
     (30, 122, 52), art_huang),
    ("UKRAINE · DIPLOMACY", "UKRAINE TALKS OPEN UP",
     "Zelensky meets US envoys; Europe joins the peace talks.",
     (0, 90, 140), art_talks),
    ("UKRAINE · WAR", "DRONE HITS WARSHIP",
     "Ukrainian drone strikes a Russian ship in the Gulf of Finland.",
     (90, 110, 130), art_warship),
    ("MIDDLE EAST", "IRAN CLAIMS RADAR STRIKE",
     "Tehran says it hit a US radar site in Bahrain.",
     (170, 90, 30), art_radar),
    ("USA · TRAVEL", "US FLIGHTS HALTED",
     "FAA grounds departures for hours after a comms failure.",
     (192, 57, 43), art_faa),
    ("SPORT", "KANE BREAKS RECORD",
     "126th cap breaks England's appearance record vs Croatia.",
     (30, 90, 45), art_kane),
]


def draw_tile(d, x, y, w, h, kicker, headline, sub, accent, art):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD, outline=BORDER, width=2)
    art_h = 180
    art(d, x + 2, y + 2, w - 4, art_h)
    ty = y + art_h + 14
    d.text((x + 18, ty), kicker, font=font(BOLD, 17), fill=accent)
    hl = wrap(d, headline, font(BOLD, 30), w - 36)
    hy = ty + 26
    for line in hl:
        d.text((x + 18, hy), line, font=font(BOLD, 30), fill=INK)
        hy += 36
    sl = wrap(d, sub, font(REG, 20), w - 36)
    sy = hy + 6
    for line in sl[:3]:
        d.text((x + 18, sy), line, font=font(REG, 20), fill=GREY)
        sy += 26


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    margin, gap = 12, 12
    cols, rows = 3, 2
    tw = (W - 2 * margin - (cols - 1) * gap) // cols
    th = (984 - 164 - (rows - 1) * gap) // rows
    for i, (kicker, headline, sub, accent, art) in enumerate(STORIES):
        cx = i % cols
        cy = i // cols
        tx = margin + cx * (tw + gap)
        ty = 164 + cy * (th + gap)
        draw_tile(d, tx, ty, tw, th, kicker, headline, sub, accent, art)
    center_text(d, W // 2, 992, "Sources: BBC, Al Jazeera, Reuters  ·  Friday 13 November 2026",
                font(REG, 17), GREY)
    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
