import os
from brownie import accounts, config, SimpleStorage, network

def deploy_simple_storage():
    acccount =get_account()
    # account2 = accounts.add(config["wallets"]["from_key"])
    
    simple_storage = SimpleStorage.deploy({"from": acccount})

    print(simple_storage)

    stored_value = simple_storage.retrieve()
    print("this is the initial value ", stored_value)

    transaction = simple_storage.store(15, {"from": acccount})
    
    updated_stored_value = simple_storage.retrieve()
    print("Updated value : ", updated_stored_value)

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    pass

def main():
    deploy_simple_storage()