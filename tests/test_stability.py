from wordybin import encode


def test_SprayCowHandyFee():
    assert "SprayCowHandyFee" == encode(bytes.fromhex("ce1862ac"))
