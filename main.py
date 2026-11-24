"""The Funniest Out-of-Office — make.fun entry.

Writes one line of an out-of-office auto-reply to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib Python 3.13.
"""
import os

TEXT = "I'm out until Monday. I left my inbox in charge and it's already asking for a raise."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate self-check: 1-140 chars, not whitespace-only, one line,
    # no leading/trailing whitespace.
    assert 1 <= len(TEXT) <= 140, "entry length out of gate"
    assert TEXT.strip(), "entry is whitespace only"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be one line"
    assert TEXT == TEXT.strip(), "entry has leading/trailing whitespace"
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))
    # Post-write verification: read the file back and prove the bytes on
    # disk are exactly the intended text, so a silent write failure or
    # encoding slip fails loudly here instead of reaching the judge.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == TEXT, "written text differs from intended text"
    assert raw == TEXT.encode("utf-8"), "written bytes differ from intended bytes"
    assert len(raw) == len(TEXT.encode("utf-8")), "written byte length differs"
    print(TEXT)


if __name__ == "__main__":
    main()
