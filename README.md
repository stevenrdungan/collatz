# collatz
Working with Collatz conjecture in Python

see https://en.wikipedia.org/wiki/Collatz_conjecture
# version 2 notes (24 Jan 2016)

Things to do:
    -right now the program works under the assumption the conjecture is true.
    think of a way to rewrite it so that it can fail gracefully if not true.
    (right now it would just churn and churn as it would never hit 1 and
    return)
    -Consider whether using a dictionary to stored previously solved numbers
    is the right way to do it. Without a hash function that O(N) complexity
    will probably do more harm than good.
    -Increase functionary - allow for command line arguments for range and
    single natural number
    -Do these musings belong in the commit notes? They're quite long but I
    would assume they'll change as the functionality changes. Hmm...
