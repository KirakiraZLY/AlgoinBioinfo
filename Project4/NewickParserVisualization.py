class Node:
    def __init__(self, name_val):
        name, val_str = name_val[::-1].split(":")
        self.name = name
        self.value = float(val_str)
        self.children = []
        self.parent = None

    def get_depth(self):
        current_node = self
        depth = 0
        while current_node.parent:
            current_node = current_node.parent
            depth += 1
        return depth

    def __str__(self):
        # return "{}:{}".format(self.name, self.value)
        return "{}".format(self.name)
def reader(newick = "(A:0.1,B:0.2,(C:0.3,D:0.4)E:0.5,G:0.8)F:0.9" ):
    root = None
    na = "" # "na" variable to name and value.
    stack = []
    cnt = 0
    for i in list(reversed(newick)):
        if i == ')':
            if na != "":

                if na[len(na)-1] == ':':
                    # print(na)
                    na = '1:' + str(cnt)
                    # print(na)
                    cnt += 1

                node = Node(na)
                # print(node)
                na = ""
                if len(stack):
                    stack[-1].children.append(node)
                    node.parent = stack[-1]
                else:
                    root = node
                stack.append(node)

        elif i == '(':
            if (na != ""):

                if na[len(na)-1] == ':':
                    # print(na)
                    na = '1:' + str(cnt)
                    cnt += 1

                node = Node(na)
                # print(node)
                na = ""
                stack[-1].children.append(node)
                node.parent = stack[-1]
            stack.pop()
        elif i == ',':
            if (na != ""):

                if na[len(na)-1] == ':':
                    # print(na)
                    na = '1:' + str(cnt)
                    cnt += 1

                node = Node(na)
                na = ""
                stack[-1].children.append(node)
                node.parent = stack[-1]
        elif i == '\n':
            continue
        elif i == ';':
            na += ':'
        else:
            # n was not defined before, changed to i.
            na = na + str(i)
            # print(na)


    print_stack = [root]
    while len(print_stack):
        node = print_stack.pop()
        print(" " * node.get_depth(), node)
        print_stack.extend(node.children)
    return [root]

def readNewick(filename):
    tree = []
    with open(filename, 'r') as fh:
        i = 0
        while True:
            cnt = fh.readline()
            # print(cnt)
            if len(cnt) == 0:
                break
            tree.append(cnt)
    # print(tree)
    tree = ''.join(tree)
    return tree

def NewickParse(filename):
    newick = readNewick(filename)
    # print(newick)
    # newick = "(AAA:0.1,B:0.2,(C:0.3,D:0.4):0.5,G:0.8):0.9"
    reader(newick)

if __name__ == "__main__":
    NewickParse("t1.txt")