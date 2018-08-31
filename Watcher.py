import time
from ReadArp import ReadArpUtility
from arp import arp

def updateAnaliticsARPsheet():
    pass

def main():
    ArpUtil = ReadArpUtility()
    initial_pair_of_ip_and_mac = ArpUtil.get_pairs_of_mac_and_ip()

    print(initial_pair_of_ip_and_mac)

    while True:
        newListOfArpTable = ArpUtil.get_pairs_of_mac_and_ip()
        for i in range(0,len(newListOfArpTable)):
            for j in range(0,len(initial_pair_of_ip_and_mac)):
                if newListOfArpTable[i][1] == initial_pair_of_ip_and_mac[j][1] and newListOfArpTable[i][0] != initial_pair_of_ip_and_mac[j][0]:
                    print('ALERT!')



main()