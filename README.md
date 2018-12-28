# py-ascii2morse

Convert ASCII string with a limited character set to morse code and inversement.

### Requirements

* Python 3.x
* Windows System (only for sound)

### Usage

* Convert ascii string to morse code : `python ./ascii2morse.py --ascii "hello world"`

* Convert morse code to ascii string : `python ./ascii2morse.py --morse ".... . .-.. .-.. ---       .-- --- .-. .-.. -.. .-.-.-"`

* Add argument `--sound` for playing morse code : `python ./ascii2morse.py --ascii "hello world" --sound`

```
usage: ascii2morse.py [-h] [--morse MORSE] [--ascii ASCII] [--sound]

Morse <-> ASCII

optional arguments:
  -h, --help     show this help message and exit
  --morse MORSE  Morse string
  --ascii ASCII  ASCII string
  --sound        Play sound
```

# License

MIT License
