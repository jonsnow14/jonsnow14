#!/usr/bin/env python3
"""Binary-alpha looping GIFs: heartbeat green orb + LIVE pill (no chroma-key fringe)."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

GREEN = (34, 197, 94, 255)
GREEN_HI = (74, 222, 128, 255)
WHITE = (240, 253, 244, 255)


def heartbeat(t: float) -> float:
    def peak(x: float, mu: float, sigma: float, amp: float) -> float:
        return amp * math.exp(-((x - mu) ** 2) / (2 * sigma * sigma))

    return min(1.0, peak(t, 0.14, 0.045, 1.0) + peak(t, 0.34, 0.055, 0.78))


def binarize(im: Image.Image, cut: int = 96) -> Image.Image:
    r, g, b, a = im.convert("RGBA").split()
    a = a.point(lambda x: 255 if x >= cut else 0)
    return Image.merge("RGBA", (r, g, b, a))


def draw_orb(size: int, beat: float) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = cy = size / 2.0
    r = size * (0.20 + 0.14 * beat)
    fill = GREEN_HI if beat > 0.45 else GREEN
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)

    if beat > 0.18:
        ring_r = r + size * (0.10 + 0.22 * beat)
        w = max(2, int(size * 0.05))
        d.ellipse(
            [cx - ring_r, cy - ring_r, cx + ring_r, cy + ring_r],
            outline=GREEN_HI,
            width=w,
        )
    return binarize(img, cut=80)


def capsule(draw: ImageDraw.ImageDraw, x0: float, y0: float, x1: float, y1: float, fill) -> None:
    r = (y1 - y0) / 2.0
    draw.ellipse([x0, y0, x0 + 2 * r, y1], fill=fill)
    draw.ellipse([x1 - 2 * r, y0, x1, y1], fill=fill)
    draw.rectangle([x0 + r, y0, x1 - r, y1], fill=fill)


def draw_badge(w: int, h: int, beat: float, font: ImageFont.FreeTypeFont) -> Image.Image:
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    fill = GREEN_HI if beat > 0.45 else GREEN
    pad = 4
    capsule(d, pad, pad, w - pad - 1, h - pad - 1, fill)

    orb = draw_orb(int(h * 0.72), beat)
    img.alpha_composite(orb, (int(h * 0.12), (h - orb.size[1]) // 2))

    text = "LIVE"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = int(w * 0.36)
    ty = (h - th) // 2 - bbox[1]
    d.text((tx, ty), text, font=font, fill=WHITE)
    return binarize(img, cut=80)


def save_transparent_gif(frames: list[Image.Image], path: Path, duration_ms: int) -> None:
    """Palette GIF: index 255 is transparent. Opaque pixels only use 0–254."""
    quantized: list[Image.Image] = []
    for im in frames:
        im = binarize(im)
        alpha = im.getchannel("A")
        rgb = Image.new("RGB", im.size, (0, 0, 0))
        rgb.paste(im.convert("RGB"), mask=alpha)
        pal = rgb.convert("P", palette=Image.ADAPTIVE, colors=255)
        pal_bytes = pal.getpalette() or []
        pal_bytes = (pal_bytes + [0] * 768)[:768]
        out = Image.new("P", im.size)
        out.putpalette(pal_bytes)
        src = list(pal.getdata())
        mask = list(alpha.getdata())
        out.putdata([255 if a < 128 else min(p, 254) for p, a in zip(src, mask)])
        quantized.append(out)

    quantized[0].save(
        path,
        format="GIF",
        save_all=True,
        append_images=quantized[1:],
        duration=duration_ms,
        loop=0,
        disposal=2,
        transparency=255,
        optimize=False,
    )


def write_svg_orb(path: Path) -> None:
    path.write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20">
  <circle cx="10" cy="10" r="6" fill="none" stroke="#4ade80" stroke-width="1.6">
    <animate attributeName="r" values="6;9.5;6;10;6" keyTimes="0;0.14;0.28;0.42;1" dur="1.2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.7;0;0.7;0;0.7" keyTimes="0;0.14;0.28;0.42;1" dur="1.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="10" cy="10" r="4.2" fill="#22c55e">
    <animate attributeName="r" values="3.6;5.1;3.6;5.4;3.6" keyTimes="0;0.14;0.28;0.42;1" dur="1.2s" repeatCount="indefinite"/>
    <animate attributeName="fill" values="#22c55e;#4ade80;#22c55e;#86efac;#22c55e" keyTimes="0;0.14;0.28;0.42;1" dur="1.2s" repeatCount="indefinite"/>
  </circle>
</svg>
""",
        encoding="utf-8",
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    n = 24
    duration = 50

    orbs = [draw_orb(64, heartbeat(i / n)) for i in range(n)]
    save_transparent_gif(orbs, OUT / "live-dot.gif", duration)

    font = ImageFont.truetype(FONT, 26)
    badges = [draw_badge(176, 56, heartbeat(i / n), font) for i in range(n)]
    save_transparent_gif(badges, OUT / "live-badge.gif", duration)

    write_svg_orb(OUT / "live-dot.svg")

    print("frames", n)
    for p in (OUT / "live-dot.gif", OUT / "live-badge.gif", OUT / "live-dot.svg"):
        print("wrote", p, p.stat().st_size)


if __name__ == "__main__":
    main()
