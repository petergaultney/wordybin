# WordyBin

What the world needs is yet another word-based encoding system for
binary data. In this case, a 16-bit encoding system, with one of 512
5-letter words standing in for the first 9 bits, and one of 128
3-letter words standing in for the next 7 bits.

## Why?

1. Because the words are fixed length, the encoded string length has a
   stepwise linear relationship to the source data. This can be
   advantageous for humans who are trying to eyeball something, and
   stands in contrast to encodings like BIP39.
2. Each word can have its accent on the first syllable, to make
   reading out loud easier.
3. Each word can be pronounced uniquely, such that there is reduced
   ambiguity when restricted to the built-in list of English words. A
   lot of effort has been put into making 'hearing' these words read
   be as unambigous as possible.
   - Caveats:
     - It is not possible to ensure strong phonetic difference across
       this many words, but we've attempted to provide as much
       phonetic difference as possible.
	 - Future versions could redo the wordlist to improve this at the
       cost of backward-incompatibility; suggestions backed up by
       `jellyfish` are welcomed since this concept is still in its
       early stages.

The words are built on prior art; mostly, this is the
[BIP39 English wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt),
filtered to 5 and 3-letter words, then filtered again for various
words that don't fit the above restrictions or that I felt like
dropping for no particular reason. Since this leaves less than 512
words, I added some 4-letter words from the BIPS wordlist that have
can have an adjectival version ending in `y`, plus a couple of
others. There were not enough 3-letter words, and many of them
diverged from the given criteria, so I added quite a few of those to
get to 128.

## Why would I actually use this?

There are a lot of cases where we want to represent something
determinstically and uniquely. One of the common cases is to provide a
unique, unopinionated, compressed reference to it. This is sometimes
called a `hash`.

Hashes have really nice properties, but they also have some not-nice
properties, and perhaps the main one is that they are just a jumble of
characters. For instance, here is a shortened, 8-character hash of a
commit from the BIP39 repo: `ce1862ac`. That hash contains 32 bits of
entropy, which is sufficient in most cases to uniquely identify a
moment in time in the life of your repository.

What it _isn't_ is memorable, or easy to communicate. But 32 bits is
very easy to communicate using WordyBin, because you can use 4 words
to represent those three bytes. `ce1862ac` (in hexadecimal) is
`SprayCowHandyFee` in WordyBin. I bet you can remember that for long
enough to switch browser tabs!

# Installation/Usage

`pip install wordybin`

* encode:

`cat <file> | python -m wordybin`
`python -m wordybin --input-file <file>`

* decode:

`echo "DirtyGumCycleGetCrossFoxCrazyFog" | python -m wordybin -d > output.b`
`python -m wordybin -d --input-file input.b --output-file output.b`
