import time
from ReadArp import get_arp_table
from arp import arp

initial_pair_of_ip_and_mac = []

def main():
    
    for i in list(get_arp_table()): 
        d = {}
        key = i['HW address']
        value = i['IP address']
        d[key] = value
        initial_pair_of_ip_and_mac.append(d)

    #print(initial_pair_of_ip_and_mac)

    # while(True):
    #     time.sleep(3)
    #     for i in list(get_arp_table()): 
    #         for j in initial_pair_of_ip_and_mac:
    #             if i == j and i['HW address'] != j['HW address']:
    #                 print('WORNING!!')
    #             else:
    #                 print("{0}   {1}  {2}  {3}".format(i,j,i['HW address'],j['HW address']))

main()