#!/usr/bin/env python

import netfilterqueue
import subprocess


def initialize_queue():
    subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])


def flush_queue():
    subprocess.call(["iptables", "--flush"])


def process_packet(packet):
    packet.drop()


initialize_queue()

try:
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()

except KeyboardInterrupt:
    print("[+] Exiting NetCut...")
    flush_queue()
