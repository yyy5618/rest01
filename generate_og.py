"""
OG 이미지 & 파비콘 생성 스크립트
출력: images/og-image.png (1200x630)
      images/favicon.png  (64x64)
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "images")

# ── 색상 ──
BG       = "#064e3b"   # 다크 그린
ACCENT   = "#6ee7b7"   # 연두 (보조)
WHITE    = "#ffffff"
DIMWHITE = "#ffffffcc"
YELLOW   = "#fde047"

W, H = 1200, 630

# ── 한글 폰트 경로 탐색 ──
def find_font(names, size):
    dirs = [
        "C:/Windows/Fonts",
        os.path.expanduser("~/AppData/Local/Microsoft/Windows/Fonts"),
    ]
    for d in dirs:
        for name in names:
            path = os.path.join(d, name)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# ══════════════════════════════════════════════
#  OG IMAGE  1200 × 630
# ══════════════════════════════════════════════
img  = Image.new("RGB", (W, H), hex2rgb(BG))
draw = ImageDraw.Draw(img)

# ── 배경 장식: 우하단 큰 원 ──
draw.ellipse([820, 300, 1380, 860],
             fill=tuple(c + 12 for c in hex2rgb(BG)))

# ── 배경 장식: 좌상단 작은 원 ──
draw.ellipse([-80, -80, 260, 260],
             fill=tuple(max(0, c - 8) for c in hex2rgb(BG)))

# ── 세로 강조선 ──
draw.rectangle([80, 80, 86, H - 80], fill=hex2rgb(ACCENT))

# ── 폰트 로드 ──
font_title  = find_font(["malgunbd.ttf", "malgun.ttf", "NanumGothicBold.ttf"], 96)
font_sub    = find_font(["malgun.ttf", "malgunbd.ttf", "NanumGothic.ttf"],     42)
font_tag    = find_font(["malgun.ttf", "NanumGothic.ttf"],                     30)
font_url    = find_font(["malgun.ttf", "NanumGothic.ttf"],                     26)

# ── 서브 텍스트 ──
draw.text((120, 180), "한국의 웹 개발 전문가", font=font_sub,
          fill=hex2rgb(ACCENT))

# ── 메인 이름 ──
draw.text((118, 250), "유용주", font=font_title, fill=hex2rgb(WHITE))

# ── 구분선 ──
draw.rectangle([120, 400, 580, 404], fill=hex2rgb(ACCENT))

# ── 기술 태그 ──
tags = ["Python", "JavaScript", "HTML5", "CSS3", "Git"]
x = 120
for tag in tags:
    tw = draw.textlength(tag, font=font_tag)
    pad = 14
    draw.rounded_rectangle(
        [x, 425, x + tw + pad * 2, 475],
        radius=8, fill=hex2rgb(ACCENT)
    )
    draw.text((x + pad, 428), tag, font=font_tag, fill=hex2rgb(BG))
    x += tw + pad * 2 + 10

# ── URL ──
draw.text((120, H - 80), "https://yyy5618.github.io/rest01/",
          font=font_url, fill=(255, 255, 255, 140))

# ── 우측 자격증 뱃지 ──
certs = ["빅데이터분석기사", "AICE Associate", "사회조사분석사 2급"]
font_cert = find_font(["malgun.ttf"], 24)
cy = 180
for cert in certs:
    tw = draw.textlength(cert, font=font_cert)
    draw.rounded_rectangle(
        [W - tw - 80, cy, W - 50, cy + 46],
        radius=8,
        outline=hex2rgb(ACCENT), width=2
    )
    draw.text((W - tw - 66, cy + 10), cert, font=font_cert,
              fill=hex2rgb(ACCENT))
    cy += 66

# ── 저장 ──
og_path = os.path.join(OUT_DIR, "og-image.png")
img.save(og_path, "PNG")
print(f"OG image saved → {og_path}")

# ══════════════════════════════════════════════
#  FAVICON  64 × 64
# ══════════════════════════════════════════════
fav  = Image.new("RGB", (64, 64), hex2rgb(BG))
fdraw = ImageDraw.Draw(fav)

# 원형 배경
fdraw.ellipse([4, 4, 60, 60], fill=hex2rgb(ACCENT))

# 'Y' 글자
font_fav = find_font(["malgunbd.ttf", "malgun.ttf"], 36)
bbox = fdraw.textbbox((0, 0), "Y", font=font_fav)
tx = (64 - (bbox[2] - bbox[0])) / 2 - bbox[0]
ty = (64 - (bbox[3] - bbox[1])) / 2 - bbox[1]
fdraw.text((tx, ty), "Y", font=font_fav, fill=hex2rgb(BG))

fav_path = os.path.join(OUT_DIR, "favicon.png")
fav.save(fav_path, "PNG")

# 16x16, 32x32 도 저장
fav.resize((32, 32), Image.LANCZOS).save(
    os.path.join(OUT_DIR, "favicon-32.png"), "PNG")
fav.resize((16, 16), Image.LANCZOS).save(
    os.path.join(OUT_DIR, "favicon-16.png"), "PNG")

print(f"Favicon saved → {fav_path}")
print("Done!")
