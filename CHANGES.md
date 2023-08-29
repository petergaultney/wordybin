# 0.2.0

Backward incompatible changes - the wordlist has changed based on some
phonetic analysis using `jellyfish`.

The order of the words has not changed, so previously-encoded strings
can still be decoded, but newly encoded bytes will sometimes differ in
their encoding.

### 0.1.1

- Add `py.typed`.
