#!/usr/bin/python
# vim: ts=4 shiftwidth=4 expandtab

from table import table
from file2dict import file2dict
from task_order import get_task_order
#from pprint import pprint
from graphics import dot
from collections import OrderedDict
#from common import format_2digit_number
from datelib import date_add
from datelib import format_hour

# strike1609@gmail.com andres root, lujan
# roluisker@gmail.com luis bejarano


def calculate_hours(tl):
    for task in tl:
        units = {"h": 1, "d": 8}
        if task["unit"] in units:
            task["hours"] = units[task["unit"]] * task["effort"]
        else:
            task["hours"] = units["h"] * task["effort"]

    return tl


def running_total(tl):
    rt = 0
    for i in tl:
        rt = i["effort"] + rt
        i["bad"] = rt
    return tl

task = ["id", "name", "effort", "unit"]
tl = calculate_hours(file2dict("tasklist.txt", task))
resource = ["id", "name", "cost"]
res = file2dict("resources.txt", resource)
dep = ["requirement", "dependent"]
deps = file2dict("dependencies.txt", dep)
table(res, "Resources")
table(deps, "Dependencies")


def implode(a, sep):
    return sep.join(a)


def add_deps(tl, deps):
    for i in tl:
        for d in deps:
            if not("deps" in i):
                i["deps"] = []
            if d["dependent"] == i["id"]:
                i["deps"].append(str(d["requirement"]))

    for i in tl:
        i["deps"] = implode(i["deps"], ",")
    return tl


def add_rt(tl, deps):
    obj = get_task_order(deps, tl)
    #order_a = obj["order"]
    rt = obj["rt"]
    #print("RT:")
    #pprint(rt)
    for k in rt:
        tl[k-1]["st"] = rt[k] - tl[k-1]["effort"]
        tl[k-1]["rt"] = rt[k]
    return tl


def get_resource_timetable(resource_name):
    timetable_line = ["weekday", "hour", "available"]
    r = file2dict("./time." + resource_name + ".txt", timetable_line)
    return r


def print_resource_timetable(resource_name):
    t = get_resource_timetable(resource_name)
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours_of_day = range(0, 23)
    a = {}
    for i in t:
        a["%s-%s" % (i["weekday"], i["hour"])] = i["available"]

        result = []
    lbl = {0: " ", 1: "X"}
    #print headers
    for hour in hours_of_day:
        line = OrderedDict()
        line["Hour"] = format_hour(hour)
        d = 1
        for day in weekdays:
            available = a[str(d) + "-" + str(hour)]
            line[day] = lbl[available]
            d = d + 1
        result.append(line)
        #line
    table(result, "Time Table for:" + resource_name)

tl = running_total(tl)
dot(tl, deps)
tl = add_rt(tl, deps)
tl = add_deps(tl, deps)
table(tl, "Task List")

project_start = "2013-08-05"


def holydays():
    return file2dict("holydays.txt", ["date", "is_holyday"])


def big_table(tl, res):
    #h = holydays()
    #100
    #if bisiesto...
    pass


def print_all_timetables(res):
    for i in res:
        #print(i["name"])
        print_resource_timetable(i["name"])

print_all_timetables(res)
print(date_add("2013-01-01", 365))
