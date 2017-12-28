#!/usr/bin/env python3

import os.path
from collections import Counter

def find_faulty_weight(lines):
    """Build the tree structure made of each node, find the node that unbalance
    the tree, and what its weight should be."""

    nodes      = {}
    has_parent = set()

    # read lines to get weight and children of each node
    for line in lines:
        line = line.strip().split('->')
        name, weight = line[0].split()
        weight = int(weight[1:-1]) # because weight data inside ( )
        nodes[name] = {"weight":   weight,
                       "children": []
                      }

        if len(line) > 1: # has children
            for child in line[1].split(','):
                child = child.strip()
                nodes[name]["children"].append(child)
                has_parent.add(child)

    # root is the node that has no parent
    root = (set(nodes.keys()) - has_parent).pop() # .pop() to get the element

    # add the "tower_weight" field to each node
    compute_tower_weight(nodes, root)

    # verify if each node is balanced, find correct weight
    correct_weight = verify(nodes, root)

    return root, correct_weight

def compute_tower_weight(tree, node):
    """Find weight of tower holded by node."""

    # no children = it's a leaf. Tower weight is its own weight
    if tree[node]["children"] == []:
        tree[node]["tower_weight"] = tree[node]["weight"]
        return tree[node]["tower_weight"]

    # else, sum of tower_weight of its children + its own weight
    w = tree[node]["weight"]
    for child in tree[node]["children"]:
        w += compute_tower_weight(tree, child)

    tree[node]["tower_weight"] = w
    return tree[node]["tower_weight"]

def verify(tree, node):
    """Verify that all children of node have the same tower weight.
         - if yes, verify each child individually
         - if no, find the faulty one, then verify if the problem comes from
           this faulty one, or from one of its children
    """

    if tree[node]["children"] == []:
        return -1 # leaf can't have faulty children

    tower_weights = [tree[c]["tower_weight"] for c in tree[node]["children"]]

    # if all same values, need to inspect deeper
    if len(set(tower_weights)) == 1:
        for c in tree[node]["children"]:
            res = verify(tree, c)
            if res != -1:  # stop the verification if we have found answer
                return res
        # all children have no problem, so this node has no problem as well
        return -1
    else:
        # find faulty and correct weights of children tower_weight
        occ = {v:k for k,v in Counter(tower_weights).items()}
        faulty  = occ[1] # faulty weight is unique (so occ=1)
        correct = faulty ^ min(tower_weights) ^ max(tower_weights)

        # find node with faulty weight
        for c in tree[node]["children"]:
            if tree[c]["tower_weight"] == faulty:
                faulty_node = c
                break

        # look if problem comes from the children of faulty node
        for c in tree[faulty_node]["children"]:
            res = verify(tree, c)
            if res != -1: # problem comes from deeper
               return res

        # children are ok, so the problem comes from faulty_node
        return tree[faulty_node]["weight"] + (correct - faulty)

if __name__ == '__main__':
    filename = "day07_structure.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        lines = open(filename).read().strip().split("\n")
        part_1, part_2 = find_faulty_weight(lines)
        print("PART ONE:", part_1)
        print("PART TWO:", part_2)
