# vim: ts=4 shiftwidth=4 expandtab

aa = {}  # sort_order
bb = {}  # running_total


def recursive_sort(node, deps, tl, maxreq):
    global aa, bb
    #print("ROOT NODE:" + str(node))
    maxreq += 1
    if maxreq > 300:
        print("ERROR.")
        return
    x = 0
    for d in deps:
        #print(str(x) + "-")
        x += 1
        if node == d["requirement"]:
            child = d["dependent"]
            child_effort = tl[child-1]["effort"]
            if not(child in aa):
                aa[child] = aa[node] + 1
                bb[child] = bb[node] + child_effort
            aa[child] = max(aa[child], aa[node] + 1)
            bb[child] = max(bb[child], bb[node] + child_effort)
            #print("node: %s child: %s , max(%s and %s) is %s" % (node,))

            recursive_sort(child, deps, tl, maxreq)
            #order_result[req] = 1


def get_task_order(deps, tl):
    global aa, bb
    right = []
    for d in deps:
        req = d["requirement"]
        dep = d["dependent"]
        right.append(dep)
    roots = []
    for d in deps:
        req = d["requirement"]
        if not (req in right):
            roots.append(req)
            aa[req] = 1  # order_result
            bb[req] = tl[req-1]["effort"]

    if len(roots) == 0:
        print("ERROR: INVALID FILE.")
        return aa

    for i in roots:
        recursive_sort(i, deps, tl, 0)
    return {"order": aa, "rt": bb}
