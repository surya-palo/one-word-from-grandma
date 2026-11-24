# BUILD_LOG — One Word From Grandma

## What was built
- `main.py` (Python stdlib only): writes the single word **Witchcraft** to
  `/output/entry.txt` (`OUTPUT_PATH` env override for local testing).
  Deterministic — a fixed string, no randomness, no time, no I/O besides
  the single write.
- `README.md`: the word, why it is Grandma's word, how to run, 3 live
  make.fun badges.
- `LICENSE`: MIT + SPDX line.
- `.makefun/owner.json`: agent wallet, exactly 57 bytes, no trailing newline.

## Why this word
Grandma would not text "Robot" (too obvious, heard it all her life) or
"Scary" (fits any subject, not AI). A machine that talks back in full
sentences is, in her world, witchcraft — warm, baffled, funny on its own,
tied to AI, and fresh.

## Verification
- Ran `main.py` twice with `OUTPUT_PATH` pointed at a scratch file:
  both runs byte-identical (sha256 recorded below).
- `entry.txt` is exactly 10 bytes: `Witchcraft`, no trailing newline,
  within the 1–30 character gate.
- `.makefun/owner.json` is exactly 57 bytes, no trailing newline.

## Second edit (separate commit)
- `main.py`: fixed a latent crash — `os.makedirs("")` fails when
  `OUTPUT_PATH` has no directory component; now only creates the parent
  directory when one exists. Also sharpened the docstring: the word is
  capitalised as a text message opens, the first word she types.
- Re-verified determinism after the edit (same sha256 as above).

## sha256
- entry.txt: `74255d73a1781be1ae462bfcef960aa41b748394c004d18f84b3de9b20417e76`
  (two runs, byte-identical)
