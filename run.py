#!usr/bin/python3
# see https://en.wikipedia.org/wiki/Collatz_conjecture

from collatz import iterate

start = int(input('Enter start: '))
stop = int(input('Enter stop: '))
iterate(start, stop)
