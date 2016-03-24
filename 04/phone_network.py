#!/usr/bin/env python
import argparse
import os
import sys

_network = None
_calls = None
_adjacency = None
_nodes = None

# Node info
class Node(object):
    def __init__(self):
        self.hops_to_source = -1
        self.path_to_source = -1
        self.visited = False
        return

# Show error message and exit
def show_error(msg):
    print msg
    sys.exit(1)
    return

# Parse command-line arguments
def parse_cmd_line_args():
    global _network
    global _calls
    parser = argparse.ArgumentParser()
    parser.add_argument('network', help='Input file: network nodes and link information')
    parser.add_argument('calls', help='Input file: calls to be placed')
    args = parser.parse_args()
    if not os.path.isfile(args.network):
        show_error("File (%s) does not exist" % args.network)
    _network = args.network
    if not os.path.isfile(args.calls):
        show_error("File (%s) does not exist" % args.calls)
    _calls = args.calls
    return

# Node number is zero-based offset from 'A'
def get_node_number(node_name):
    return ord(node_name) - ord('A')

# Node name is letter at offset from 'A'
def get_node_name(node_number):
    return chr(ord('A') + node_number)

# Build adjacency table
def load_network():
    global _network
    global _adjacency
    with open(_network, 'r') as f:
        lines = f.readlines()
    max_node = 0
    links = []
    for line in lines:
        link = line.split()
        node0 = get_node_number(link[0])
        node1 = get_node_number(link[1])
        max_node = max(max_node, node0, node1)
        links.append([node0, node1, int(link[2])])
    max_node += 1
    _adjacency = [[0 for x in range(max_node)] for x in range(max_node)]
    for link in links:
        _adjacency[link[0]][link[1]] = link[2]
        _adjacency[link[1]][link[0]] = link[2]
    return

# Visit node and mark all neighbors
def visit_node(node_number):
    global _adjacency
    global _nodes
    if _nodes[node_number].visited:
        return
    _nodes[node_number].visited = True
    for i in range(len(_nodes)):
        if _adjacency[node_number][i] > 0 and _nodes[i].hops_to_source < 0:
            _nodes[i].hops_to_source = _nodes[node_number].hops_to_source + 1
            _nodes[i].path_to_source = node_number
    for i in range(len(_nodes)):
        if _adjacency[node_number][i] > 0:
            visit_node(i)
    return

# Build path to source
def build_path_to_source(start):
    global _adjacency
    global _nodes
    name = get_node_name(start)
    if _nodes[start].hops_to_source == 0:
        return [name]
    _adjacency[start][_nodes[start].path_to_source] -= 1
    _adjacency[_nodes[start].path_to_source][start] -= 1
    path = build_path_to_source(_nodes[start].path_to_source)
    path.append(name)
    return path

# Attempt a single call
def attempt_single_call(src, dst):
    global _adjacency
    global _nodes
    global _path
    _nodes = None
    _nodes = [Node() for x in range(len(_adjacency))]
    source_number = get_node_number(src)
    _nodes[source_number].hops_to_source = 0
    _nodes[source_number].path_to_source = source_number
    visit_node(source_number)
    dest_number = get_node_number(dst)
    print "Call", src, dst,'--',
    if _nodes[dest_number].visited:
        path = build_path_to_source(dest_number)
        print "placed",
        for i in path:
            print i,
        print
    else:
        print "failed"
    return

# Read call file and attempt to place calls
def attempt_calls():
    global _calls
    with open(_calls, 'r') as f:
        lines = f.readlines()
    for line in lines:
        call = line.split()
        attempt_single_call(call[0], call[1])
    return
    
# Main program
parse_cmd_line_args()
load_network()
attempt_calls()
