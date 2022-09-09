from brownie import accounts, TestOracle


def main():
    my_acc = accounts[0]
    ss = TestOracle.deploy({"from": my_acc})
    print(ss.decimals())
    print(ss.description())
    print(ss.version())
    print(ss.getRoundData(0))
    print(ss.latestRoundData())


