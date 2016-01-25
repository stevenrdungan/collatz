#!usr/bin/python3
# see https://en.wikipedia.org/wiki/Collatz_conjecture

# returns number of times function needs to iterate for
# natural number n such that a sub i = f^i(n)


solved_ints = dict()

def collatz(n, count=0, stored_ints=[]):
    # is o(N) lookup making program slower?
    if n in stored_ints:
        return count + stored_ints[n]
    if n == 1:
        return count
    elif n % 2 == 0:
        n = n / 2
        count += 1
        return collatz(n, count, stored_ints)
    elif n % 2 == 1:
        n = n * 3 + 1
        count += 1
        return collatz(n, count, stored_ints)

def iterate(start=1, stop=11):
    for i in range(start, stop):
        count = collatz(i, 0, solved_ints)
        solved_ints[i] = count
        print(i, solved_ints[i])
