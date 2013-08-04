from os import system


def dot(tl, deps):
    dx = "digraph G {\nrankdir=LR\nnode[shape=box]\n"
    for i in deps:
        l = i["requirement"]
        r = i["dependent"]
        left = str(l) + "." + tl[l-1]["name"]
        right = str(r) + "." + tl[r-1]["name"]
        dx += "\"" + left + "\"->\"" + right + "\";\n"
    dx += "}"
    f = open("dotfile.dot", "w")
    f.write(dx)
    f.close()
    system("dot -Tpng dotfile.dot > graph.png")
    system("open graph.png")
