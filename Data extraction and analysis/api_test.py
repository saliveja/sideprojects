import requests
import json
from etherscan import Etherscan

eth = Etherscan("CNDJBXBCX8QFJIVNVIZXX5GFNMGKX2T1AX")
eth_balance = eth.get_eth_balance(address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")
eth_balance_multiple = eth.get_eth_balance_multiple()







# data = response_API.text
# parse_json = json.loads(data)
# active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
# print("Active cases in South Andaman:", active_case)

#  "result": [
# "contractAddress": "0x...",
# "tokenName": "Token Name",
# "symbol": "Token Symbol",
# "divisor": "18",
# "tokenType": "ERC20",
# ]
#
# https://api.etherscan.io/api
# module=account
# action=balancemulti
# address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67
# tag=latest
# apikey=YourApiKeyToken