# collatz
Working with Collatz conjecture in Python. See
https://en.wikipedia.org/wiki/Collatz_conjecture for background.



Functionality to implement:

* Implement functionality to allow for checking only odd numbers as arguments,
and return the number of times the function iterates in between evaluating as
an odd number

* The program works under the assumption the conjecture is true. Is there a
way to rewrite it to fail gracefully such that for some natural number n there
exists no integer i such that f^i(n) == 1

* Consider whether using a dictionary to stored previously solved numbers
is the right way to do it. Without a hash function that O(N) complexity
will probably do more harm than good.



Contact author: steven dot r dot dungan at gmail dot com
