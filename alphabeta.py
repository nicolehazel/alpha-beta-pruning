# Created for Queen's University CISC352 Assignment 2 part 2

INFINITY = 1000000

# Open input file alphabeta.txt

# Read input and put into data structure..
# single whitespace separates the two sets..
# multiple graphs separated by blank newline
# set one is {(NODE1,MIN),(NODE2,MAX)}
# set two is {(NODE1,NODE2)}
# no order given to the first input set, except that it will start with the root node
# edges are listed in left-to-right top-to-bottom order

# Node as a class?
# Attributes: edges, MIN/MAX, ptrs to children, ptrs to parents(?) --> no, recursion takes care of that
# is_child attribute OR child class is child
#

# Write output to alphabeta_out.txt
# output the score and number of leaf nodes examined
# Graph n: Score: X; Leaf Nodes Examined: Y


class Node:
    def __init__(self, idx, ismax):
        self.name = idx  # identification string
        self.isMax = ismax
        self.children = []  # list of names of each child node

node_dict = {}  # dictionary of node objects

def main():

    # Parse the input file
    try:
        with open("alphabeta.txt", 'r') as infile:
            graphs = infile.read().split('\n\n')  # list of all graphs in file
    except IOError:
        print("Error parsing alphabeta.txt")

    g = graphs[1]
    g = g.split()
    nodes = g[0][2:-2].split('),(')  # list of NAME,MAX strings
    root_name = ((nodes[0]).split(','))[0]
    edges = g[1][2:-2].split('),(')  # list of PARENT,CHILD strings
    # print(nodes)
    # print(edges)

    # Create node objects for each item in list
    for n in nodes:
        n = n.split(',')
        name = n[0]
        minmax = n[1]
        # print name
        # print minmax
        node_dict[name] = Node(name, minmax)

    # Add names of child nodes
    for e in edges:
        e = e.split(',')
        parent = e[0]
        child = e[1]
        node_dict[parent].children.append(child)

    # for nd in node_dict.values():
    #     print(nd.name)
    #     print(nd.children)

    ret = alphabeta(root_name, -INFINITY, INFINITY)
    print(ret)


# Returns optimal value for current player
def alphabeta(name, alpha, beta):
    # print("ALPHABETA")
    if name.isdigit():
        print("Leaf!!: " + name)
        return float(name)
    else:
        node = node_dict[name]
        if node.isMax:
            best = -INFINITY
            for child in node.children:
                value = alphabeta(child, alpha, beta)
                best = max(best, value)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = INFINITY
            for child in node.children:
                value = alphabeta(child, alpha, beta)
                best = min(best, value)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best

main()