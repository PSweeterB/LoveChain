from brownie import accounts, LoveChain


def main():
    my_acc = accounts[0]
    ss = LoveChain.deploy({"from": my_acc})
    print(ss.retrieve())
    print(ss.store(150, {"from": my_acc}))
    print(ss.retrieve())

