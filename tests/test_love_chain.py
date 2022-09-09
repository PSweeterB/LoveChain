#!/usr/bin/python3
import brownie


def test_get_fee(accounts, loveChain):
    assert loveChain.getFee() == 6406519700003638


def test_get_(accounts, loveChain, testOracle):
    loveChain.setETHToUSDOracle(testOracle.address, {'from': accounts[0]})
    assert loveChain.ETHToUSDOracle() == testOracle.address


def test_set_fee_from_wrong_acc(accounts, loveChain, testOracle):
    with brownie.reverts():
        loveChain.setETHToUSDOracle(testOracle.address, {'from': accounts[1]})


def test_make_love(accounts, loveChain):
    msg = 'Pavel + Olga = Love'
    loveChain.makeLove(accounts[1], msg, {'from': accounts[1], 'value': 6406519700003638})
    # tokenId = loveChain.tokenByIndex(0)

    assert loveChain.balanceOf(accounts[1]) == 1
    # assert loveChain.tokenMessage(tokenId) == msg



