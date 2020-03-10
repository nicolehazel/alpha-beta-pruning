# Created for Queen's University CISC352 Assignment 2 part 2

INFINITY = 1000000  # arbitrarily high value
node_dict = {}  # global dictionary of <node_name : node_object> pairs


class Node:
    def __init__(self, idx, ismax):
        self.name = idx  # identification string
        self.isMax = ismax  # boolean to distinguish MAX and MIN
        self.children = []  # list of names of each child node


def main():
    try:  # Parse the input file
        with open("alphabeta.txt", 'r') as infile:
            graphs = infile.read().split('\n\n')  # list of all graphs in file
    except IOError:
        print("Error parsing alphabeta.txt")

    for i in range(len(graphs)):  # run the pruning for each graph in the file
        g = graphs[i].split()  # split the string into two sets using whitespace
        nodes = g[0][2:-2].split('),(')  # list of "NAME,MAX" strings
        root_name = ((nodes[0]).split(','))[0]  #
        edges = g[1][2:-2].split('),(')  # list of "PARENT,CHILD" strings

        for n in nodes:  # Create object for each node in list
            n = n.split(',')
            name = n[0]
            ismax = n[1] == "MAX"
            node_dict[name] = Node(name, ismax)  # add node object to dictionary

        for e in edges:  # add children info to nodes
            e = e.split(',')
            parent = e[0]
            child = e[1]
            node_dict[parent].children.append(child)  # add child names to parent object

        score, leaf_count = alphabeta(root_name, -INFINITY, INFINITY, 0)

        try:  # write the results to the output file
            with open("alphabeta_out.txt", 'a') as outfile:
                outfile.write("Graph %i: Score: %i; Leaf Nodes Examined: %i\n" % (i+1, score, leaf_count))
        except IOError:
            print("Error writing to alphabeta_out.txt")
    return


# Returns optimal value for current player
def alphabeta(name, alpha, beta, leaf_ctr):
    if name.isdigit():
        # print("Found leaf " + name)
        return float(name), leaf_ctr+1
    else:
        # print("On node: " + name)
        node = node_dict[name]
        if node.isMax:
            best = -INFINITY
            for child in node.children:
                value, leaf_ctr = alphabeta(child, alpha, beta, leaf_ctr)
                best = max(best, value)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best, leaf_ctr
        else:
            best = INFINITY
            for child in node.children:
                value, leaf_ctr = alphabeta(child, alpha, beta, leaf_ctr)
                best = min(best, value)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best, leaf_ctr


main()
