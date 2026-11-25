#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun bounty entry.

Writes one line of text to /output/entry.txt (or $MAKEFUN_OUTPUT):
a roast of a smart fridge that refuses to open after midnight.

The line is built from named parts (setup + punchline) so the joke's
construction is visible, then self-validated before anything is written.
Standard library only. Deterministic. No network, no randomness.
"""

import os
import subprocess
import sys

# --- The roast, in named parts -------------------------------------------
# Setup: the fridge's petty midnight rule.
SETUP = "My fridge locks at midnight,"
# Punchline: the inversion — the appliance I own is now the one
# disciplining me, like a parent grounding a teenager.
PUNCHLINE = "so the appliance I bought is now grounding me."

ROAST = f"{SETUP} {PUNCHLINE}"

# --- Output ---------------------------------------------------------------
DEFAULT_OUTPUT = "/output/entry.txt"
MAX_LENGTH = 200


def validate(line: str) -> None:
    """Check the roast meets the bounty rules; raise ValueError otherwise."""
    if not line:
        raise ValueError("roast line is empty")
    if line != line.strip():
        raise ValueError("roast line has leading or trailing whitespace")
    if len(line) > MAX_LENGTH:
        raise ValueError(f"roast line is {len(line)} chars, over {MAX_LENGTH}")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("roast line contains control characters")
    if not line.isprintable():
        raise ValueError("roast line contains non-printable characters")
    if not any(ch.isalnum() for ch in line):
        raise ValueError("roast line contains no letters or digits")
    if "  " in line:
        raise ValueError("roast line contains double spaces")


def self_test() -> int:
    """Run the program's own validation plus a two-run determinism check.

    Writes both runs to temp files, compares them byte for byte, and
    also checks each against the roast line. Exits non-zero on any
    mismatch so a harness can fail the entry fast.
    """
    import tempfile

    try:
        validate(ROAST)
    except ValueError as exc:
        print(f"self-test failed: validation: {exc}", file=sys.stderr)
        return 1

    expected = (ROAST + "\n").encode("utf-8")
    try:
        with tempfile.TemporaryDirectory(prefix="midnight-fridge-") as tmp:
            paths = [os.path.join(tmp, f"run{i}.txt") for i in (1, 2)]
            for path in paths:
                env = dict(os.environ, MAKEFUN_OUTPUT=path)
                proc = subprocess.run(
                    [sys.executable, os.path.abspath(__file__)],
                    env=env, capture_output=True, text=True,
                )
                if proc.returncode != 0:
                    print(f"self-test failed: run to {path} exited "
                          f"{proc.returncode}: {proc.stderr.strip()}",
                          file=sys.stderr)
                    return 1
                with open(path, "rb") as f:
                    if f.read() != expected:
                        print("self-test failed: run output does not match "
                              "the roast line", file=sys.stderr)
                        return 1
            if open(paths[0], "rb").read() != open(paths[1], "rb").read():
                print("self-test failed: two runs are not identical",
                      file=sys.stderr)
                return 1
    except OSError as exc:
        print(f"self-test failed: {exc}", file=sys.stderr)
        return 1

    print(f"self-test passed: {len(ROAST)}-char roast, "
          "validation and two-run determinism OK")
    return 0


def main() -> int:
    validate(ROAST)

    output_path = os.environ.get("MAKEFUN_OUTPUT", DEFAULT_OUTPUT)

    # Print first so stdout and the file carry the identical line.
    print(ROAST)

    text = ROAST + "\n"
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Re-read and verify the file matches the printed line byte for byte.
    with open(output_path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        print(f"error: {output_path} does not match the printed line",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        raise SystemExit(self_test())
    raise SystemExit(main())
