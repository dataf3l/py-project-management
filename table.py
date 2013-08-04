def table(data, title=""):
    print(title)

    if len(data) == 0:
        print("No records found.")
        return
    dy = ""
    dx = ""
    m = {}
    for row in data:
        s = ""
        for cell_name in row:
            cell = str(row[cell_name])
            if not (cell_name in m):
                m[cell_name] = len(cell_name)
            m[cell_name] = max(m[cell_name], len(cell))

    for row in data:
        s = ""
        for cell_name in row:
            cell = str(row[cell_name])
            spaces = m[cell_name] - len(cell)
            s += "%s %s" % (cell, spaces * " ")
        dx += s + "\n"

    for header in data[0]:
        spaces = m[header] - len(header)
        dy += header.capitalize() + " " + (" " * spaces)

    print(dy)
    print(len(dy) * "-")
    print(dx)
