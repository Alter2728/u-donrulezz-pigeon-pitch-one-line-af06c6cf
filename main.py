"""Revised entry: tightened the draft into startup pitch jargon (fleet size, zero rent, rooftop HQs, a statue moat) and landed the joke on a pigeon-droppings pun."""

import os

TEXT = "Invest in Coo-ber: 10,000 pigeons, zero rent, rooftop HQs, and same-day crumb delivery — our moat is every statue in the city, and business is dropping daily."


def main() -> None:
    assert 1 <= len(TEXT) <= 200
    assert "\n" not in TEXT and "\r" not in TEXT
    assert TEXT == TEXT.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == TEXT


if __name__ == "__main__":
    main()
