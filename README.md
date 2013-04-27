PasswordMaker
=============

What is it ?
------------

A quick an dirty project using JohnTheRipper Markov generator in order to generate word-like passwords.

Idea
----

The markov generator has been implemented in order to compute words which are close to real words, according to markov chains.
This models the fact that it is more likely to find after a c the letter h than the letter z.

Usage
-----

The basic usage is :
>$ python passwordmaker.py 150 /path/to/jtr/
>veursyzzau1m

If you want to compute a data file on your own, you should use the '-r' option.
To specify the maximum length of the ouput password, use the '-m' option. 


Reference
---------

JohnTheRipper Markov on openwall [wiki](http://openwall.info/wiki/john/markov).

