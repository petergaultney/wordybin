from wordybin import decode


def test_words_removed_in_0_1():
    assert decode("WhaleRawWhaleFinWhaleDogWhaleCub") == decode("WharfRapWharfFitWharfDotWharfCup")
