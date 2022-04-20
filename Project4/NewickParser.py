import networkx as nx
import sys
sys.setrecursionlimit(20000)

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight = 1):
        self.connectedTo[nbr] = weight

    def __str__(self):
        # return str(self.connectedTo.keys())
        return str(self.id) + ' connectedTo' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return  self.connectedTo.keys()

    def getId(self):
        return self.id

    def getweight(self,nbr):
        return  self.connectedTo[nbr]

    def getwhich(self,i):
        cnt = 0
        ans = False
        for x in self.connectedTo:
            if cnt == i:
                ans = x.id
                break
            cnt += 1
        return ans


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return  newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return  self.vertList[n]
        else:
            return  None

    def getVertexSon(self,n,i):
        if n in self.vertList:
            return self.vertList[n].getwhich(i)
        else:
            return -2
    def getVertexlen(self,n):
        if n in self.vertList:
            return len(self.vertList[n].connectedTo)
        else:
            return None

    def __contains__(self, n):
        return  n in self.vertList

    def addEdge(self,f,t,const = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not  in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],const)

    def getVertices(self):
        return  self.vertList.keys()

    def __iter__(self):
        return  iter(self.vertList.values())

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
        return "{}:{}".format(self.name, self.value)

class TreeNode:
    def __init__(self, name_val):
        self.id = id
        self.parent = None
        self.children = []

def reader(newick = "(A:0.1,B:0.2,(C:0.3,D:0.4)E:0.5,G:0.8)F:0.9" ):
    root = None
    na = "" # "na" variable to name and value.
    stack = []
    for i in list(reversed(newick)):
        if i == ')':

            if na != "":
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
                node = Node(na)
                # print(node)
                na = ""
                stack[-1].children.append(node)
                node.parent = stack[-1]
            stack.pop()
        elif i == ',':
            if (na != ""):
                node = Node(na)
                na = ""
                stack[-1].children.append(node)
                node.parent = stack[-1]
        elif i == '\n':
            continue
        else:
            # n was not defined before, changed to i.
            na += i
            # print(type(na))
            # print(i)
            # print(na)

    """
    print_stack = [root]
    while len(print_stack):
        node = print_stack.pop()
        print(" " * node.get_depth(), node)
        print_stack.extend(node.children)
    """
    return [root]

def adjecent():
    g = Graph()
    # for i in range(6):
    #     g.addVertex(i)
    # print(g.vertList)
    # g.addVertex(i)

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

def readNewick(filename):
    tree = []
    with open(filename, 'r') as fh:
        i = 0
        while True:
            cnt = fh.readline().rstrip('\n')
            # print(cnt)
            if len(cnt) == 0:
                break
            tree.append(cnt)
    # print(tree)
    tree = ''.join(tree)
    return tree

def rootTree(g,u,father,fa,relabel,cnt):
    len = g.getVertexlen(str(u))

    # print(len)
    for i in range(0,len):
        v = g.getVertexSon(str(u),i) ########################### Get the next node
        # print("current node: ", str(u))
        # print("next node: ",v)
        if str(v) != str(father):
            fa[v] = str(u)
            rootTree(g,str(v),str(u),fa,relabel,cnt)
        elif g.getVertexlen(str(u)) == 1: # It is a leaf
            relabel[u] = cnt
            cnt += 1
            # print("AAAAAAAAAAAA")
    # print(fa)
    return relabel,fa
    # print("BBBBBBBBBBBBBBBBBBBBBBBBBBB")

def unrootReader(newick1):
    g = Graph()
    g2 = Graph()

    # for i in list(newick):
    #     if i != '(' or i != ')' or i != ',' or i != '\n':
    #         g.addVertex(i)

    root = None
    na = ""  # "na" variable to name and value.
    s1 = [] # for symbols
    s2 = [] # for str
    tmp = []
    cnt = 0
    for i in list(reversed(newick1)):
        # print("S1: ",s1)
        # print("S2: ",s2)
        if i == '(':
            m = i
            len1 = 0
            s1.append(i)
            # s2.append(na)
            if na != "":
                if na[0] == ':':  ############## internal
                    na = str(cnt)
                    cnt += 1
                    # print("NANANA: ",na)
                    s2.append(na)
                else:
                    j = 0
                    while j < len(na):
                        if na[j] == ':':
                            break
                        j += 1
                    # print("len: ", j, len(na),na)
                    s2.append(na[:j])
            na = ""
            m = s1.pop()
            while m != ')':
                # print(s2)
                n = s2.pop()
                tmp.append(n)
                m = s1.pop()
                len1 += 1
            # print("N: ",n)
            # print("M: ",m)
            # print("tmp: ",tmp)
            # print("1: ",s2)
            # print("lens2: ",len(s2))

            if len(s2) > 0:
                par = s2.pop()
                s2.append(par)
                for k in range(len(tmp)):
                    if len(tmp[k]) > 27:
                        # print(tmp[k][:24])

                        a = tmp[k][:26]
                        g.addEdge(a, par)
                        g.addEdge(par, a)
                    else:
                        g.addEdge(tmp[k],par)
                        g.addEdge(par,tmp[k])
            else:
                for k in range(len(tmp)):
                    for l in range(len(tmp)):
                        # print("K: ",k)
                        if k != l:
                            if len(tmp[k]) > 27:
                                a = tmp[k][:26]
                                b = tmp[l][:26]
                                g.addEdge(a, b)
                                g.addEdge(b, a)
                            else:
                                g.addEdge(tmp[k],tmp[l])
                                g.addEdge(tmp[l],tmp[k])


            na = ""
            # print("Tmp: ",tmp)
            ############# 然后和stack连接 ############
            tmp.clear()


        elif i == ')': # push in
            if na == "":
                s1.append(i)
            # s2.append(na)
            else:
                s1.append(i)
                if na[0] == ':':  ############## internal
                    na = str(cnt)
                    cnt += 1
                    # print("NANANA: ", na)
                    s2.append(na)
                else:
                    j = 0
                    while j < len(na):
                        if na[j] == ':':
                            break
                        j += 1
                    # print("len: ", j, len(na),na)
                    s2.append(na[:j])

            # print("2: ",s2)

        elif i == ',':
            if na == "":
                s1.append(i)
            # s2.append(na)
            else:
                s1.append(i)
                if na[0] == ':':  ############## internal
                    na = str(cnt)
                    cnt += 1
                    # print("MAMAMA: ", na)
                    s2.append(na)
                else:
                    j = 0
                    while j < len(na):
                        if na[j] == ':':
                            break
                        j += 1
                    s2.append(na[:j])
            # print("3: ",s2)
            na = ""
        elif i == ";":
            na = ":" + na
        else:
            na = str(i) + na
            # print("na: ",na)
    return g



def getRoot(g):
    # print("AAAAAAAAAAAAAAAAAA")
    for v in g:
    #     print(v)
        t2rootname = v.getId()
        break
    return t2rootname

def Relabel(g,t2rootname):
    fa = {}
    son = {}
    for v in g:
        son[v.getId()] = -1
    # print("initial: ",son)
    """
        for w in v.getConnections():
            print("(%s,%s)" % (v.getId(), w.getId()))
            # print(v.getId())
    """
    ############## Above is Using adjecent list to store the map ####################

    # print("first node: ",g.getVertex(t2rootname))
    fa[t2rootname] = -1 ################ root
    # print(g.getVertexSon('C',0))

    relabel1,fa = rootTree(g,t2rootname,-1,fa,son,0) ### DFS
    # print(relabel1)
    relabel = {}
    cnt = 1
    for i in relabel1:
        if relabel1[i] == 0:
            relabel[i] = cnt
            cnt += 1
    # print(fa)
    # print(relabel)
    # print(len(fa) - len(relabel)-2) # minus "root" and one internal
    return relabel,(len(fa) - len(relabel)-2),fa

"""
def getScales(g,u,father,fa,relabel):
    len = g.getVertexlen(str(u))
    # print(len)
    for i in range(0, len):
        v = g.getVertexSon(str(u), i)  ########################### Get the next node
        # print("current node: ", str(u))
        # print("next node: ",v)
        if str(v) == str(father):
            if g.getVertexlen(str(u)) == 1:  # It is a leaf
                relabel[u] = cnt
                cnt += 1
            # print("AAAAAAAAAAAA")
    # print(fa)
    return relabel
"""


def dfs(g,u,father,fa,minscale,maxscale, size, ROOT):
    len = g.getVertexlen(str(u))
    # print(len)
    for i in range(0,len):
        # print("AAAAAAAAAAAA")
        v = g.getVertexSon(str(u),i) ########################### Get the next node
        # print("current node: ", str(u))
        # print("next node: ",v)

        if str(v) != str(father):
            if father != -1:
                minscale[father] = min(minscale[u], minscale[father])
                maxscale[father] = max(maxscale[father], maxscale[u])
                # size[father] += size[u]
            fa[v] = str(u)
            dfs(g,str(v),str(u),fa,minscale,maxscale, size, ROOT)
        # print(v)
        # rootTree(g,str(v),str(u),fa,relabel,cnt)
        elif str(father) == ROOT:
            minscale[u] = -1
            maxscale[u] = 11111
        else:
            if minscale[fa[u]] != -1:
                minscale[fa[u]] = min(minscale[fa[u]], minscale[u])
                maxscale[fa[u]] = max(maxscale[fa[u]], maxscale[u])
                size[fa[u]] += size[u]


        """
        if str(v) == str(father):
            if str(father) == ROOT:
                minscale[v] = -1
                maxscale[v] = 11111
            else:
                fa[v] = str(u)
                # print(v)
                # rootTree(g,str(v),str(u),fa,relabel,cnt)
                if g.getVertexlen(str(u)) == 1: # It is a leaf
                    minscale[fa[v]] = min(minscale[fa[v]], minscale[v])
                    maxscale[fa[v]] = max(maxscale[fa[v]],maxscale[v])
        """

            # print("AAAAAAAAAAAA")
    # print(fa)
    return minscale,maxscale,size

def cmp(a,b):
    # print(a[0],b[0])

    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    if a[1] < b[1]:
        return -1
    if a[1] > b[1]:
        return 1
    return 0
def CompRFDistance(inter1,inter2,T1,T2):
    len1 = len(inter1)
    len2 = len(inter2)
    i = 0; j = 0
    share = 0
    while i < len1 and j < len2:
        if(cmp(inter1[i],inter2[j]) > 0): # inter1[i] > inter2[j], could possibly exist in inter2 later
            j += 1
        elif cmp(inter1[i],inter2[j]) == 0: ###### share += 1
            share += 1
            i += 1
            j += 1
        else: #### could not be existed
            i += 1
    # print("Share: ",share)
    return T1 + T2 - 2 * share
def NewickParse(filename1,filename2):
    newick1 = readNewick(filename1)
    newick2 = readNewick(filename2)
    # print(newick2)
    g1 = unrootReader(newick1)
    # print("AAAAAAAAAAAAAAAAAAAAAAAA")
    # return 0
    g2 = unrootReader(newick2)

    t2rootname = getRoot(g1)
    print("Root: ",t2rootname)
    # t2rootname = 'A'
    # print("T2RootName: ",t2rootname)
    relabel,T1,fa1 = Relabel(g1,t2rootname)
    relabel2,T2,fa2 = Relabel(g2,t2rootname)
    # print("label: ",relabel)
    # print("T1,T2: ",T1,T2)
    # print("Fa: ",fa1)
    # getScales(g1,t2rootname,-1,fa1,relabel) ############################ Get scales

    minscale = {}
    maxscale = {}
    size = {}
    for v in fa1:
        minscale[v] = 10000
        maxscale[v] = 0
        size[v] = 0

    for v in relabel:
        # print(v)
        minscale[v] = relabel[v]
        maxscale[v] = relabel[v]
        size[v] = 1
    minscale[t2rootname] = -1
    maxscale[t2rootname] = -1
    # print(minscale)
    minscale1, maxscale1, size1 = dfs(g1,t2rootname,-1,fa1,minscale,maxscale, size, t2rootname)
    # print("Min Scale: ",minscale)
    # print("Max Scale: ",maxscale)
    # print("Size: ",size)

    minscale = {}
    maxscale = {}
    size = {}
    for v in fa2:
        minscale[v] = 10000
        maxscale[v] = 0
        size[v] = 0

    for v in relabel:
        # print(v)
        minscale[v] = relabel[v]
        maxscale[v] = relabel[v]
        size[v] = 1
    minscale[t2rootname] = -1
    maxscale[t2rootname] = -1
    minscale2, maxscale2, size2 = dfs(g2,t2rootname,-1,fa2,minscale,maxscale, size, t2rootname)
    # print("Min Scale: ",minscale2)
    # print("Max Scale: ",maxscale2)
    # print("Size: ",size2)

    internode1 = []
    for v in fa1:
        if maxscale1[v] - minscale1[v] + 1 == size1[v] and maxscale1[v] != minscale1[v]:
            ########################## This is an internal node
            internode1.append((minscale1[v],maxscale1[v]))
    # print(internode[0][1])
    internode1.sort(key = lambda s:(s[0],s[1]))

    internode2 = []
    for v in fa2:
        # print(v,maxscale2[v],minscale2[v])
        if maxscale2[v] - minscale2[v] + 1 == size2[v] and maxscale2[v] != minscale2[v]:
            ########################## This is an internal node
            # print(v)
            internode2.append((minscale2[v], maxscale2[v]))
    # print(internode[0][1])
    internode2.sort(key=lambda s: (s[0], s[1]))
    # print("inter2: ",internode2)

    ans = CompRFDistance(internode1,internode2,T1,T2)
    print("RF-Distance == ",ans)

if __name__ == "__main__":
    # NewickParse("a.newick")

    # adjecent()


    na = "333"
    j = 0
    while j < len(na):
        if na[j] == "\'":
            break
        j += 1
    print(j)

    if j < len(na)-1:
        print(na[j:])
    else:
        print(na)
