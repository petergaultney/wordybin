# shims for backward-compatibility as the wordlist evolves.


def _add_0_1_threes(d: dict):
    # old word = replacement word
    d["raw"] = d["rap"]
    d["fin"] = d["fit"]
    d["dog"] = d["dot"]
    d["cub"] = d["cup"]


def _add_0_1_fives(d: dict):
    # old word = replacement word
    d["whale"] = d["wharf"]


def add_old_words(d: dict):
    _add_0_1_threes(d)
    _add_0_1_fives(d)
