from time import sleep

import pytest


@pytest.mark.last
def test_foo():
    sleep(1)
    assert True

@pytest.mark.run(order=2)
def test_bar():
    sleep(1)
    assert True

@pytest.mark.run(order=1)
def test_aar():
    sleep(1)
    assert True