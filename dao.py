import argparse
import requests, bs4
from etherscan import Etherscan
import sys

class MintingCalculation:
    """Program which calculate number of new shares, total shares and price 
    based on allocated funds."""

    def __init__(self):
        """initializing."""
        self.treasury = self._treasury_balance()
        self.shares = self._shares_balance()

    def _treasury_balance(self):
        """Parsing etherscan for account balance"""

        key = "11NA6DSE388KMM3BXWRHAK27WRQP66S66J"
        eth = Etherscan(key)
        
        treasury = "0x59f77dc848c2e45b5954975ee1969e7a22fa25f6"
        balance = eth.get_eth_balance(treasury)
        balance = float(balance)
        balance = balance / 1000000000000000000

        return balance

    def _shares_balance(self):
        """Parsing ethplorer for shares balance"""

        url="https://api.ethplorer.io/getTokenInfo/0x33e6ded5073f512475e17b5f19dda90d9a782478?apiKey=freekey"
        res=requests.get(url)
        res.raise_for_status()
        data = res.json()
        supply = data['totalSupply']
        supply = float(supply)
        balance = supply / 1000000000000000000

        return balance

    def stats(self, args):
        """calculations and printing of dao stats"""

        allocation = float(args.amount)
        fractal = allocation / self.treasury
        new_shares = self.shares / (1 - fractal) - self.shares
        new_total_shares = self.shares / (1 - fractal)
        new_price = new_total_shares / self.treasury
        dilution = allocation / self.treasury * 100
        shares_price = self.shares / self.treasury

        print("--------------------------------------\n")
        print("LunarDAO stats")
        print("\n")
        print(f"Treasury: {self.treasury} ETH")
        print(f"Total shares: {self.shares} $VOX")
        print(f"Price: {shares_price} (shares/1 ETH)")
        print("\n====================================\n")
        print(f"If the dao allocate {allocation} eth to mint new shares:")
        print("\n")
        print(f"New shares: {new_shares} $VOX")
        print(f"New total shares: {new_total_shares} $VOX")
        print(f"New price: {new_price} (shares/1 ETH)")
        print(f"Dilution: {dilution} %")
        print("\n--------------------------------------")

    def panic(self, msg):
        """Error message print"""
        print(f"error: {msg}", file=sys.stderr)
        sys.exit(-1)
        
    def parser_main(self):
        """argparser - storing arguments and setting default functions."""
        
        parser = argparse.ArgumentParser(
            prog='Minting calculation',
            description='Calculation of # of new shares, toal shares and price')

        # version
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
        subparsers = parser.add_subparsers(
            help="{subcommand}[-h] shows all the options")

        # allocated asset
        parser_allocation = subparsers.add_parser('allocation', 
            help='allocated asset. Syntax: <a> <index>', aliases=['a'])

        parser_allocation.add_argument('amount', help='enter amount in eth')

        parser_allocation.set_defaults(func=self.stats)

        args = parser.parse_args()

        try:
            args.func(args)
        except AttributeError as e:
            msg = f"{e}.\nPlease run: ./dao.py --help"
            self.panic(msg)

        except IndexError as e:
            msg = f"{e}.\nPlease run: ./dao.py --help"
            self.panic(msg)

if __name__ == '__main__':
    mc = MintingCalculation()
    mc.parser_main()
