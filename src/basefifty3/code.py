from pathlib import Path

__parent = Path(__file__).parent
_fives = open(__parent / "words/512.txt").read().splitlines()
_threes = open(__parent / "words/threes.txt").read().splitlines()
_word_to_val = {w: i for i, w in enumerate(_fives)}
for i, w in enumerate(_threes):
    _word_to_val[w] = i

# assert len(_word_to_val) == 512 + 128, len(_word_to_val)


def encode(_bytes: bytes, titlecase: bool = True) -> str:
    outstr = ""
    it = iter(_bytes)

    def title(w: str) -> str:
        return w.title() if titlecase else w

    for byte1 in it:
        word1 = byte1 << 1  # move byte 'up' one bit
        try:
            byte2 = next(it)
            word1 |= byte2 >> 7  # take very highest bit of byte
            outstr += title(_fives[word1 & 0x1FF])  # only 9 bits
            outstr += title(_threes[byte2 & 0x7F])  # only 7 bits
        except StopIteration:
            outstr += title(
                _fives[word1 & 0x1FF]
            )  # 9 bits, but the last one will be zero

    return outstr


def decode(_str: str) -> bytes:
    outbytes = bytearray()

    s_pos = 0
    while s_pos < len(_str):
        w5 = _str[s_pos : s_pos + 5].lower()
        if s_pos + 7 < len(_str):
            w3 = _str[s_pos + 5 : s_pos + 8].lower()
        else:
            w3 = ""

        bit_accum = _word_to_val[w5] << 7
        bit_accum |= _word_to_val[w3] & 0x7F
        outbytes.append(bit_accum >> 8)
        outbytes.append(bit_accum & 0xFF)
        s_pos += 8
    return bytes(outbytes)
