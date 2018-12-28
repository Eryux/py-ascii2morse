# coding: utf8
"""
MIT License

Copyright (c) 2018, Candia Nicolas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import winsound
import argparse
import time

ascii2m = {'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
'<EOT>':'.-.-.-',',':'--..--',':':'---...','?':'..--..','\'':'.----.','-':'-....-','/':'-..-.','(':'-.--.-','\"':'.-..-.','=':'-...-','ERR':'........', ' ': '     '}

m2ascii = {}

def to_m(val):
    val = val.upper()
    r = ""
    for c in val:
        r += (ascii2m[c] if c in ascii2m else ascii2m['ERR']) + ' '
    return r + ascii2m['<EOT>']

def to_ascii(val):
    r = ""
    words = val.split('       ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            r += (m2ascii[letter] if letter in m2ascii else '¿')
        r += ' '
    return r

def play_sound(val, freq = 700, base = 200):
    print("Playing sound ...")
    val = val.replace('       ', '§')
    old = ''
    for c in val:
        if (c == '.' or c == '-') and (old == '.' or old == '-'):
            time.sleep(base / 1000)
        
        if c == '.':
            winsound.Beep(freq, base)
        elif c == '-':
            winsound.Beep(freq, base * 3)
        elif c == ' ':
            time.sleep(base * 3 / 1000)
        elif c == '§':
            time.sleep(base * 7 / 1000)
        old = c

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Morse <-> ASCII")
    parser.add_argument('--morse', type=str, required=False, help="Morse string", default=None)
    parser.add_argument('--ascii', type=str, required=False, help="ASCII string", default=None)
    parser.add_argument('--sound', help="Play sound", required=False, action='store_true')

    # Reverse translation
    for k in ascii2m:
        m2ascii[ascii2m[k]] = k

    args = parser.parse_args()

    if args.morse:
        print("Morse : " + args.morse)
        r = to_ascii(args.morse)
        print("ASCII : " + r)
        if args.sound:
            play_sound(args.morse)

    elif args.ascii:
        print("ASCII : " + args.ascii)
        r = to_m(args.ascii)
        print("Morse : " + r)
        if args.sound:
            play_sound(r)