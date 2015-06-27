#!/usr/bin/env python

text = [int(x) for x in open('p059_cipher.txt').readline().split(',')]

alphabet = range(ord('a'), ord('z') + 1)

def decipher(key, text, length=0):
    if length == 0:
        length = len(text)
    return "".join(chr(text[i] ^ ord(key[i%3])) for i in range(length))

# Iterate through all the keys    
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            key = "".join([chr(a), chr(b), chr(c)])
            decoded = decipher(key, text, 100)
            location = decoded.find('the')
            if location >= 0:
                print key, decoded

# I just use grep to search for 'the'
"""
gbe (Yie-Fo~qea!ok!Jbin!!ce`pydr-0)-0 Do yie-cejhnchnj!ted Znri!aaseley-dxdrthe.-Ie-va~!wduh-Foi- lod-ie
god (The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he
jkb %Pnh$Abwvhh&bb&Gknc(&nlg}p$7$$7-Mh-pnh$dhcocjocc&ylc-S`&lhthebt$cumuyab#$Nh$qlw&zmre$Ab`*-ehi$nh
"""
# This looks promising key = 'god'

print "\nEnter key: ",
key = raw_input()
message = decipher(key, text)

print "\nMessage:", message
print "\nASCII Sum:", sum(ord(c) for c in message)

