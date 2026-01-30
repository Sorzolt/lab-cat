'''
This program prints stdin to the screen.
'''
#!/usr/bin/env python3
import sys


_BUFFER_SIZE = 1024 * 64


def _cat_stream(in_fh, out_fh) -> None:
    while True:
        chunk = in_fh.read(_BUFFER_SIZE)
        if not chunk:
            break
        out_fh.write(chunk)


def main(argv: list[str]) -> int:
    out_fh = sys.stdout.buffer

    if len(argv) == 0:
        _cat_stream(sys.stdin.buffer, out_fh)
        return 0

    exit_code = 0
    for path in argv:
        if path == "-":
            _cat_stream(sys.stdin.buffer, out_fh)
            continue

        try:
            with open(path, "rb") as fh:
                _cat_stream(fh, out_fh)
        except OSError as exc:
            sys.stderr.write(f"cat.py: {path}: {exc}\n")
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
