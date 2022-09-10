#!/usr/bin/python3

import pytest
from brownie import network, config

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def loveChain(LoveChain, TestOracle, accounts):
    lo = None
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        to = TestOracle.deploy({"from": accounts[0]})
        lo = LoveChain.deploy(to.address, {'from': accounts[0]})
    else:
        lo = LoveChain.deploy(config["networks"][network.show_active()]["oracle-address"], {'from': accounts[0]})
    return lo


@pytest.fixture(scope="module")
def testOracle(TestOracle, accounts):
    to = TestOracle.deploy({"from": accounts[0]})
    return to
