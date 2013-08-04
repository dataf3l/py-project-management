from collections import OrderedDict


def file2dict(file_name, keys):
    lines = open(file_name, "r").readlines()
    data = []
    for line in lines:
        line = line.replace("\n", "").replace("\r", "")
        parts = line.split(";")
        r = OrderedDict()
        x = 0
        for i in keys:
            part = parts[x]
            if part.isdigit():
                part = int(part)
            r[i] = part
            x += 1
        data.append(r)
    return data
