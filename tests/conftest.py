#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def loveChain(LoveChain, TestOracle, accounts):
    to = TestOracle.deploy({"from": accounts[0]})
    lo = LoveChain.deploy({'from': accounts[0]})
    lo.setETHToUSDOracle(to.address, {'from': accounts[0]})
    return lo

@pytest.fixture(scope="module")
def testOracle(TestOracle, accounts):
    to = TestOracle.deploy({"from": accounts[0]})
    return to
