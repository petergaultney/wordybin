import os
import re

import pytest

from wordybin import decode, encode


def _bytes(_bytes):
    return " ".join([f"{b:0>8_b}" for b in _bytes])


def test_simple_roundtrip():
    assert decode(encode(b"012345678")) == b"012345678"


def test_properly_encoded_with_overflow_roundtrips():
    the_bytes = decode("AgentGumCauseHub")
    print(_bytes(the_bytes))
    assert encode(the_bytes) == "AgentGumCauseHub"


def test_invalid_words_with_error_message():
    with pytest.raises(
        ValueError,
        match=re.escape(
            r"'Pot' at position 13 (context: AgentGumCausePot) is not a valid WordyBin word."
        ),
    ):
        decode("AgentGumCausePot")


def test_improperly_encoded_with_overflow_decodes_to_correct_bytes(caplog):
    the_bytes = decode("WagonCowTruckEgg")
    print(_bytes(the_bytes))
    assert encode(the_bytes) == "WagonCowTruckEgg"


def test_lots_of_random_bytes():
    for n in range(100):
        for i in range(10):
            the_bytes = os.urandom(n)
            encoded = encode(the_bytes)
            result_bytes = decode(encoded)
            assert result_bytes == the_bytes, (
                n,
                i,
                _bytes(the_bytes),
                _bytes(result_bytes),
            )


def test_having_exactly_eight_bytes_results_in_special_encodings():
    assert encode(b"76543210") == "DirtyGumCycleGetCrossFoxCrazyFly"
    assert encode(b"76543211") == "DirtyGumCycleGetCrossFoxCrazyFog"
    assert encode(b"76543212") == "DirtyGumCycleGetCrossFoxCrazyFox"
    assert encode(b"01234567") == "CrashFogCrimeFunCrushGigDepthGuy"
    assert encode(b"01234568") == "CrashFogCrimeFunCrushGigDepthHad"
    assert encode(b"01234569") == "CrashFogCrimeFunCrushGigDepthHam"


def test_having_exactly_eight_bytes_results_in_no_extra_zero_bytes():
    bs = b"76543212"
    assert decode(encode(bs))[-1] == int(bs[-1])
    assert len(decode(encode(bs))) == 8


def test_pad_digits_two():
    assert decode(encode(b"0123456789")) == b"0123456789"


def test_lots_of_random_bytes():
    for n in range(100):
        for i in range(10):
            the_bytes = os.urandom(n)
            encoded = encode(the_bytes)
            result_bytes = decode(encoded)
            print(n, i, encoded, _bytes(the_bytes))
            assert result_bytes == the_bytes, (
                n,
                i,
                _bytes(the_bytes),
                _bytes(result_bytes),
            )
