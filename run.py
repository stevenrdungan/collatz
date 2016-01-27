#!usr/bin/python3
# see https://en.wikipedia.org/wiki/Collatz_conjecture

from collatz import iterate, iterate_odds
import argparse


parser = argparse.ArgumentParser(description='Collatz conjecture')
parser.add_argument('-start', '--start', nargs='?', type=int,
    required=True, help= 'specify start of range(inclusive)')
parser.add_argument('-stop', '--stop', nargs='?', type=int,
    required=True, help= 'specify stop of range(non-inclusive)')
parser.add_argument('-odds', '--odds', nargs='?', type=bool,
    help= 'iterate for only odd integers, and return ' +
    'number of function iterations between odd evaluations')
args = parser.parse_args()

# add ability to parse optional arguments start, stop, diffOdds

start = int(input('Enter start: '))
stop = int(input('Enter stop: '))
# iterate(start, stop)
iterate_odds(start, stop)
