import counter
import pytest


def test_counter_inc():
    assert counter.inc(4) == 5
    assert counter.inc(0) == 1
    assert counter.inc(-1) == 0
    assert counter.inc(-2) == -1
    assert counter.inc(99) == 100
    assert counter.inc(999) == 1000


def test_counter_dec():
    assert counter.dec(5) == 4
    assert counter.dec(1) == 0
    assert counter.dec(0) == -1
    assert counter.dec(-1) == -2
    assert counter.dec(100) == 99
    assert counter.dec(1000) == 999
