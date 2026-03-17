"""Generate SVG image samples and a PDF booklet from translation examples."""

from pathlib import Path
import textwrap

from swahili_translation_refinement import build_examples


PAGE_WIDTH = 595
PAGE_HEIGHT = 842


def wrap_text(text: str, width: int = 82) -> list[str]:
    return textwrap.wrap(text, width=width) or [""]


def make_svg_pages(output_dir: Path, examples, per_page: int = 4) -> list[Path]:
    """Create SVG sample sheets that can be used as image examples."""
    paths: list[Path] = []
    for start in range(0, len(examples), per_page):
        group = examples[start : start + per_page]
        index = (start // per_page) + 1
        path = output_dir / f"translation_sample_{index}.svg"

        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">',
            '<rect width="100%" height="100%" fill="#f8fafc"/>',
            f'<text x="40" y="50" font-size="28" font-family="Arial" font-weight="bold" fill="#0f172a">Swahili Translation Samples ({start+1}-{start+len(group)})</text>',
        ]

        y = 95
        for number, example in enumerate(group, start=start + 1):
            lines.append(f'<text x="40" y="{y}" font-size="20" font-family="Arial" font-weight="bold" fill="#1e293b">Example {number}</text>')
            y += 28

            sections = [
                ("EN", example.description, "#111827"),
                ("MT SW", example.description_sw, "#b45309"),
                ("Refined SW", example.description_sw_refined, "#166534"),
            ]
            for label, content, color in sections:
                wrapped = wrap_text(content, width=84)
                for i, row in enumerate(wrapped):
                    prefix = f"{label}: " if i == 0 else "    "
                    safe = (prefix + row).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    lines.append(
                        f'<text x="60" y="{y}" font-size="16" font-family="Arial" fill="{color}">{safe}</text>'
                    )
                    y += 22
            y += 12

        lines.append("</svg>")
        path.write_text("\n".join(lines), encoding="utf-8")
        paths.append(path)

    return paths


def escape_pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def make_pdf(output_dir: Path, examples) -> Path:
    """Create a simple multi-page PDF using native PDF syntax."""
    pdf_path = output_dir / "swahili_translation_samples.pdf"

    objects: list[bytes] = []

    # 1: Catalog, 2: Pages, 3: Font
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(b"<< /Type /Pages /Kids [ ] /Count 0 >>")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    page_ids = []

    for idx, example in enumerate(examples, start=1):
        content_lines = ["BT", "/F1 12 Tf", "50 800 Td", f"(Sample {idx}) Tj", "ET"]

        y = 770
        blocks = [
            ("Original English", example.description),
            ("Machine Swahili", example.description_sw),
            ("Refined Swahili", example.description_sw_refined),
            ("Issue", example.error_comment),
            ("Why better", example.improvement_comment),
        ]

        for title, text in blocks:
            content_lines.extend([
                "BT",
                "/F1 11 Tf",
                f"50 {y} Td",
                f"({escape_pdf_text(title + ':')}) Tj",
                "ET",
            ])
            y -= 18
            for row in wrap_text(text, 88):
                content_lines.extend([
                    "BT",
                    "/F1 10 Tf",
                    f"62 {y} Td",
                    f"({escape_pdf_text(row)}) Tj",
                    "ET",
                ])
                y -= 14
            y -= 10

        stream_data = "\n".join(content_lines).encode("latin-1", errors="replace")
        content_obj = f"<< /Length {len(stream_data)} >>\nstream\n".encode("ascii") + stream_data + b"\nendstream"
        objects.append(content_obj)
        content_id = len(objects)

        page_obj = f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] /Resources << /Font << /F1 3 0 R >> >> /Contents {content_id} 0 R >>".encode("ascii")
        objects.append(page_obj)
        page_ids.append(len(objects))

    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    objects[1] = f"<< /Type /Pages /Kids [ {kids} ] /Count {len(page_ids)} >>".encode("ascii")

    pdf = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{i} 0 obj\n".encode("ascii"))
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")

    xref_pos = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    pdf.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        pdf.extend(f"{off:010d} 00000 n \n".encode("ascii"))

    pdf.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("ascii")
    )

    pdf_path.write_bytes(pdf)
    return pdf_path


def main() -> None:
    out = Path("samples")
    out.mkdir(exist_ok=True)

    examples = build_examples()
    svgs = make_svg_pages(out, examples)
    pdf = make_pdf(out, examples)

    readme = out / "README.md"
    with readme.open("w", encoding="utf-8") as f:
        f.write("# Sample Assets\n\n")
        f.write("Sample files generated from the translation refinement examples.\n\n")
        f.write("## Image files\n")
        for svg in svgs:
            f.write(f"- `{svg.name}` (SVG image sheet)\n")
        f.write("\n## PDF file\n")
        f.write(f"- `{pdf.name}` (printable multi-page booklet)\n")


if __name__ == "__main__":
    main()
