import sys

from .code import decode, encode


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "rb") as f:
            print(encode(f.read()))
    else:
        for line in sys.stdin:
            line = line.strip()
            sys.stdout.buffer.write(decode(line))


if __name__ == "__main__":
    main()
