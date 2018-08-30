import time
from ReadArp import ReadArpUtility
from arp import arp



def main():
    ArpUtil = ReadArpUtility()
    initial_pair_of_ip_and_mac = ArpUtil.get_pairs_of_mac_and_ip()

    while True:
        newListOfArpTable = ArpUtil.get_pairs_of_mac_and_ip()
        for i in range(0,len(newListOfArpTable)):
            print('.')

main()