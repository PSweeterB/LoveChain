from brownie import accounts, LoveChain, network, config


def main():
    lo = LoveChain.deploy(config["networks"][network.show_active()]["oracle-address"], {'from': accounts[0]})
    print(lo.getFee())