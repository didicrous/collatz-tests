#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------
# making changes yah yah yah

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read (self) :
        s    = "1 603\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 603)

    def test_read (self) :
        s    = "8 212\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  8)
        self.assertEqual(j, 212)                

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)
    
    def test_eval_4 (self) :
        v = collatz_eval(99, 99)
        self.assertEqual(v, 26)
    
    def test_eval_5 (self) :
        v = collatz_eval(1000, 2007)
        self.assertEqual(v, 182)                    


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 99, 99, 26)
        self.assertEqual(w.getvalue(), "99 99 26\n")
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 1000, 2007, 182)
        self.assertEqual(w.getvalue(), "1000 2007 182\n")        


    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("3 3\n4 4\n5 5\n6 6\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "3 3 8\n4 4 3\n5 5 6\n6 6 9\n")   
    def test_solve_3 (self) :
        r = StringIO("100 300\n300 800\n800 900\n900 982\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "100 300 128\n300 800 171\n800 900 179\n900 982 174\n")              

# ----
# main
# ----

if __name__ == "__main__" :
    main()
