from collections import defaultdict

import jellyfish

from wordybin.code import _fives, _threes


def find_collisions(func, wlist):
    collisions = defaultdict(list)

    for word in wlist:
        phon = func(word)
        collisions[phon].append(word)
    return {k: v for k, v in collisions.items() if len(v) > 1}


def test_print_nysiis_collisions():
    print("NYSIIS Collisions:")
    print(find_collisions(jellyfish.nysiis, _fives))
    print(find_collisions(jellyfish.nysiis, _threes))
    print("")


def test_print_match_rating_codex_collisions():
    print("Match Rating Codex Collisions:")
    print(find_collisions(jellyfish.match_rating_codex, _fives))
    print(find_collisions(jellyfish.match_rating_codex, _threes))
    print("")
