import scapy.all as scapy
from optparse import OptionParser

parser = OptionParser()


def user_interface():
    parser.add_option("-i", "--ip",dest="ip_address", help="?")
    (user_input, args) = parser.parse_args()
    if not user_input.ip_address:
        print("Enter ip range")
    else:
        return user_input


def scan_ip(ip_range):
    arp_request_packet = scapy.ARP(pdst=ip_range)

    arp_broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

    combined_packet = arp_broadcast / arp_request_packet

    (answer_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)

    answer_list.summary()


user_ip = user_interface()
scan_ip(user_ip.ip_address)