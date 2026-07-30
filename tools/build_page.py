#!/usr/bin/env python3
"""Gera o index.html autocontido da wiki de Dualidade.

Fontes e imagens de assets/ entram embutidas como data: URI, para que a
página funcione sozinha — offline, em GitHub Pages ou publicada como
artifact, sem depender de nenhum host externo.

Uso:  python3 tools/build_page.py
"""

import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "page.template.html"
OUTPUT = ROOT / "index.html"

ASSETS = {
    "F_BODONI_IT": ("assets/fonts/bodoni-moda-italic.woff2", "font/woff2"),
    "F_BODONI": ("assets/fonts/bodoni-moda.woff2", "font/woff2"),
    "F_SANS_400": ("assets/fonts/fira-sans-400.woff2", "font/woff2"),
    "F_SANS_700": ("assets/fonts/fira-sans-700.woff2", "font/woff2"),
    "F_MONO": ("assets/fonts/fira-mono-400.woff2", "font/woff2"),
    "POSTER": ("assets/art/poster.webp", "image/webp"),
    "LUZ": ("assets/art/luz.webp", "image/webp"),
    "SOM": ("assets/art/som.webp", "image/webp"),
}


def data_uri(path: pathlib.Path, mime: str) -> str:
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def main() -> int:
    html = TEMPLATE.read_text(encoding="utf-8")

    for token, (rel, mime) in ASSETS.items():
        path = ROOT / rel
        if not path.exists():
            print(f"asset ausente: {rel}", file=sys.stderr)
            return 1
        placeholder = "{{" + token + "}}"
        if placeholder not in html:
            print(f"placeholder nao usado no template: {placeholder}", file=sys.stderr)
            return 1
        html = html.replace(placeholder, data_uri(path, mime))

    if "{{" in html:
        leftover = html[html.index("{{"): html.index("{{") + 40]
        print(f"placeholder nao resolvido: {leftover}", file=sys.stderr)
        return 1

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"index.html gerado — {len(html.encode('utf-8')) / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
