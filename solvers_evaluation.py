import json
from dsl import *
from arc_types import *
from constants import *

def solve_f4081712():
    input_file = '../data/evaluation/f4081712.json' 
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = hmirror(dt)
    x2 = vmirror(dt)
    x3 = ofcolor(dt,THREE)
    x4 = subgrid(x3, x1)
    x5 = subgrid(x3, x2)
    x6 = palette(x4)
    x7 = contained(THREE, x6)
    O = branch(x7, x5, x4)
    return O


def solve_e95e3d83():
    input_file = '../data/evaluation/e95e3d8e.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    # x1 = replace(dt, ZERO, ZERO)
    # x2 = dmirror(x1)
    # x3 = papply(pair, x1, x2)
    # x4 = lbind(apply, maximum)
    # x5 = apply(x4, x3)
    # O = hmirror(dt)
    x1 = height(dt)
    x2 = width(dt)
    x3 = partition(dt)
    x4 = colorfilter(x3, ZERO)
    x5 = difference(x3, x4)
    x6 = merge(x5)
    x7 = astuple(x1, ONE)
    x8 = astuple(ONE, x2)
    x9 = decrement(x1)
    x10 = decrement(x2)
    x11 = toivec(x10)
    x12 = tojvec(x9)
    x13 = crop(dt, x11, x8)
    x14 = crop(dt, x12, x7)
    x15 = asobject(x14)
    x16 = asobject(x13)
    x17 = vperiod(x15)
    x18 = hperiod(x16)
    x19 = astuple(x17, x18)
    x20 = lbind(multiply, x19)
    x21 = neighbors(ORIGIN)
    x22 = mapply(neighbors, x21)
    x23 = apply(x20, x22)
    x24 = lbind(shift, x6)
    x25 = mapply(x24, x23)
    O = paint(dt, x25)
    return O


def solve_50a16a69():
    input_file = '../data/evaluation/50a16a69.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = asobject(dt)
    x2 = shape(dt)
    x3 = decrement(x2)
    x4 = index(dt, x3)
    x5 = double(x2)
    x6 = canvas(x4, x5)
    x7 = paint(x6, x1) 
    x8 = objects(x7, F, F, T)
    x9 = first(x8)
    x10 = shift(x9, LEFT)
    x11 = vperiod(x10)
    x12 = hperiod(x10)
    x13 = neighbors(ORIGIN)
    x14 = lbind(mapply, neighbors)
    x15 = power(x14, TWO)
    x16 = x15(x13)
    x17 = astuple(x11, x12)
    x18 = lbind(multiply, x17)
    x19 = apply(x18, x16)
    x20 = lbind(shift, x10)
    x21 = mapply(x20, x19)
    O = paint(dt, x21)
    return O


def solve_506d28a5():
    input_file = '../data/evaluation/506d28a5.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = tophalf(dt)
    x2 = bottomhalf(dt)
    x3 = ofcolor(x1, 0)
    x4 = ofcolor(x2, 0)
    x5 = intersection(x3, x4)
    x6 = astuple(4, 5)
    x7 = canvas(3, x6)
    O = fill(x7, 0, x5)
    return O



# def solve_712bf12e():
#     #d9f24cd1
#     input_file = '../data/evaluation/712bf12e.json'
#     with open(input_file, 'r') as f:
#         data=json.load(f)
#     test_inputs = [item['input'] for item in data.get('test')][0]
#     dt = tuple(map(tuple, test_inputs))
#     x1 = ofcolor(dt, TWO)
#     x2 = ofcolor(dt, FIVE)
#     x3 = prapply(connect, x1, x2)
#     x4 = mfilter(x3, vline)
#     x5 = underfill(dt, TWO, x4)
#     x6 = matcher(numcolors, TWO)
#     x7 = objects(x5, F, F, T)
#     x8 = sfilter(x7, x6)
#     x9 = difference(x7, x8)
#     x10 = colorfilter(x9, TWO)
#     x11 = mapply(toindices, x10)
#     x12 = apply(urcorner, x8)
#     x13 = shift(x12, UNITY)
#     x14 = rbind(shoot, UP)
#     x15 = mapply(x14, x13)
#     x16 = fill(x5, TWO, x15)
#     x17 = mapply(vfrontier, x11)
#     O = fill(x16, TWO, x17)

#     # ans = [list(item) for item in O]
#     # with open('output.txt','w') as f:
#     #     f.write(str(dt))
#     #     f.write('\n')
#     #     f.write(str(ans))

# def solve_8fbca751():
#     # 6d75e8bb
#     input_file = '../data/evaluation/8fbca751.json'
#     with open(input_file, 'r') as f:
#         data=json.load(f)
#     test_inputs = [item['input'] for item in data.get('test')][0]
#     dt = tuple(map(tuple, test_inputs))
#     x1 = objects(dt, T, T, T)
#     x2 = first(x1)
#     x3 = ulcorner(x2)
#     x4 = subgrid(x2, dt)
#     x5 = replace(x4, ZERO, TWO)
#     x6 = asobject(x5)
#     x7 = shift(x6, x3)
#     O = paint(dt, x7)
#     return O
#     # ans = [list(item) for item in O]
#     # with open('output.txt','w') as f:
#     #     f.write(str(dt))
#     #     f.write('\n')
#     #     f.write(str(ans))

def solve_d19f7514():
    input_file = '../data/evaluation/d19f7514.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = tophalf(dt)
    x2 = bottomhalf(dt)
    x3 = ofcolor(x1, 0)
    x4 = ofcolor(x2, 0)
    x5 = intersection(x3, x4)
    x6 = astuple(6, 4)
    x7 = canvas(4, x6)
    O = fill(x7, 0, x5)
    return O


def solve_195ba7dc():
    input_file = '../data/evaluation/195ba7dc.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = lefthalf(dt)
    x2 = righthalf(dt)
    x3 = ofcolor(x1, 7)
    x4 = ofcolor(x2, 7)
    x5 = combine(x3, x4)
    O = fill(x1, 1, x5)
    return O

def solve_0c9aba6e():
    input_file = '../data/evaluation/0c9aba6e.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = tophalf(dt)
    x2 = bottomhalf(dt)
    x3 = ofcolor(x1, 0)
    x4 = ofcolor(x2, 0)
    x5 = intersection(x3, x4)
    x6 = astuple(6, 4)
    x7 = canvas(0, x6)
    O = fill(x7, 8, x5)
    return O

def sovle_34b99a2b():
    input_file = '../data/evaluation/34b99a2b.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = lefthalf(dt)
    x2 = righthalf(dt)
    x3 = ofcolor(x1, 8)
    x4 = ofcolor(x2, 5)
    x5 = ofcolor(x1, 0)
    x6 = ofcolor(x2, 0) 
    x7 = combine(x3, x4)
    x8 = combine(x5, x6)
    x9 = intersection(x7, x8)
    x10 = astuple(5, 4)
    x11 = canvas(0, x10)
    O = fill(x11, 2, x9)
    return O


def solve_5d2a5c43():
    input_file = '../data/evaluation/5d2a5c43.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = lefthalf(dt)
    x2 = righthalf(dt)
    x3 = ofcolor(x1, 4)
    x4 = ofcolor(x2, 4)
    x5 = combine(x3, x4)
    O = fill(x1, 8, x5)
    return O

def solve_292dd178():
    #d4f
    input_file = '../data/evaluation/292dd178.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = apply(delta, x1)
    x3 = merge(x2)
    x4 = fill(dt, 2, x3)
    x5 = apply(box, x1)
    x6 = merge(x5) 
    x7 = apply(toindices, x1)
    x8 = merge(x7)
    x9 = papply(difference, x5, x7)
    x10 = merge(x9)
    x11 = papply(arcposition, x5, x9)
    x12 = papply(shoot, x10, x11)
    x13 = merge(x12)
    O = fill(x4, 2, x13)
    return O


def solve_4e469f39():
    input_file = '../data/evaluation/4e469f39.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = apply(delta, x1)
    x3 = merge(x2)
    x4 = fill(dt, 2, x3)
    x5 = apply(box, x1)
    x6 = first(x5)
    x7 = last(x5)
    x8 = apply(toindices, x1)
    x9 = first(x8)
    x10 = last(x8)
    x11 = difference(x7, x9)
    x12 = difference(x6 ,x10)
    x13 = totuple(shift(x11, UP))
    x14 = totuple(shift(x12, UP))
    x15 = shoot(first(x13), LEFT)
    x16 = shoot(first(x14), LEFT)
    O = fill(x4, 2, x15)
    O = fill(O, 2, x16)

def solve_60c09cac():
    input_file = '../data/evaluation/60c09cac.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    O = upscale(dt, 2)
    return O

def solve_d4b1c2b1():
    input_file = '../data/evaluation/d4b1c2b1.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = numcolors(dt)
    O = upscale(dt, x1)
    return O

def solve_21f83797():
    input_file = '../data/evaluation/21f83797.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = fork(combine, vfrontier, hfrontier)
    x3 = compose(x2, center)
    x4 = mapply(x3, x1)
    x5 = underfill(dt, 2, x4)
    x6 = mapply(toindices, x1)
    x7 = box(x6)
    x8 = delta(x7)
    O = fill(x5, 1 ,x8)
    return O

def solve_0c786b71():
    input_file = '../data/evaluation/0c786b71.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))

    x1 = vmirror(dt)
    x2 = hmirror(x1)
    x3 = hmirror(dt)
    x4 = hconcat(x2, x3)
    x5 = hmirror(x4)
    O  = vconcat(x4, x5)



def solve_59341089():
    input_file = '../data/evaluation/59341089.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = vmirror(dt)
    x2 = hconcat(x1, dt)
    O = hconcat(x2, x2)
    return O


def solve_e7639916():
    input_file = '../data/evaluation/e7639916.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = merge(x1)
    x3 = box(x2)
    O = underfill(dt, 1, x3)
    return O


def solve_32e9702f():
    input_file = '../data/evaluation/32e9702f.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = apply(toindices,x1)
    x3 = rbind(shift, LEFT)
    x4 = apply(x3, x2)
    x5 = astuple(height(dt),width(dt))
    x6 = canvas(5, x5)
    x7 = color(first(x1))
    x8 = merge(x4)
    O = fill(x6, x7, x8)
    return O


def solve_00576224():
    input_file = '../data/evaluation/00576224.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = vmirror(dt)
    x2 = hconcat(dt, dt)
    x3 = hconcat(x2, dt)
    x4 = hconcat(x1, x1)
    x5 = hconcat(x4 ,x1)
    x6 = vconcat(x3 ,x5)
    O  = vconcat(x6, x3)
    return O


def solve_84db8fc4():
    input_file = '../data/evaluation/84db8fc4.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, F)
    x2 = colorfilter(x1 , 0)
    x3 = rbind(bordering, dt)
    x4 = mfilter(x2, x3)
    x5 = fill(dt, 2, x4)
    x6 = merge(x2)
    x7 = difference(x6, x4)
    O  = fill(x5, 5, x7)
    return O

def solve_00dbd492():
    input_file = '../data/evaluation/00dbd492.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = apply(delta, x1)
    x3 = merge(sizefilter(x2, 49))
    x4 = merge(sizefilter(x2, 25))
    x5 = merge(sizefilter(x2, 9))
    x6 = fill(dt, 3, x3)
    x7 = fill(x6, 4, x4)
    x8 = fill(x7, 8, x5)
    x9 = sizefilter(x1, 1)
    x10 = merge(x9)
    O = fill(x8, 2, x10)
    return O

def solve_e0fb7511():
    input_file = '../data/evaluation/e0fb7511.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = sizefilter(x1, 1)
    x3 = merge(x1)
    x4 = merge(x2)
    x5 = difference(x3, x4)
    O = fill(dt, 8 ,x5)
    return O

def solve_fc754716():
    input_file = '../data/evaluation/fc754716.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, F)
    x2 = colorfilter(x1, 0)
    x3 = merge(x2)
    x4 = astuple(height(dt), width(dt))
    x5 = canvas(0, x4)
    x6 = box(x3)
    x7 = sizefilter(x1 ,1)
    x8 = merge(x7)
    x9 = color(x8)
    O = fill(x5, x9, x6)
    return O


def solve_551d5bf1():
    input_file = '../data/evaluation/551d5bf1.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = apply(delta, x1)
    x3 = merge(x2)
    x4 = fill(dt, 8, x3)
    x5 = apply(box, x1)
    x6 = order(x5, uppermost)
    x7 = apply(toindices, x1)
    x8 = order(x7, uppermost)
    x9 = papply(difference, x6, x8)
    x10 = merge(x9)
    x6 = remove(first(x6), x6)
    x9 = remove(first(x9), x9)
    x11 = papply(arcposition, x6, x9)
    x12 = papply(shoot, x10, x11)
    x13 = merge(x12)
    O = fill(x4, 8, x13)
    # ans = [list(item) for item in O]
    # with open('output.txt','w') as f:
    #     f.write(str(dt))
    #     f.write('\n')
    #     f.write(str(ans))
    return O


# def solve_8a371977():
#     input_file = '../data/evaluation/8a371977.json'
#     with open(input_file, 'r') as f:
#         data=json.load(f)
#     test_inputs = [item['input'] for item in data.get('test')][0]
#     dt = tuple(map(tuple, test_inputs))
#     x1 = objects(dt, T, F, F)
#     x2 = colorfilter(x1, 0)
#     x3 = order(x2, ulcorner)
#     x4 = order(x2, lrcorner)
#     x5 = merge(x2)
#     x7 = lambda x: position(x5, first(x3))==(1, 0)
#     x8 = sfilter(x5, x7)
#     with open("result.txt","w") as f:
#         f.write(f"x2:{x2}\n")
#         f.write(f"x8:{x8}\n")


def solve_0e671a1a():
    input_file = '../data/evaluation/0e671a1a.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = ofcolor(dt, 2)
    x2 = ofcolor(dt, 3)
    x3 = ofcolor(dt, 4)
    x4 = first(x1)
    x5 = first(x2)
    x6 = first(x3)
    x7 = astuple(first(x4), last(x6))
    x8 = astuple(first(x6), last(x5))
    x9 = connect(x7, x4)
    x10 = connect(x7, x6)
    x11 = combine(x9, x10)
    x12 = connect(x8, x6)
    x13 = connect(x8, x5)
    x14 = combine(x12, x13)
    x15 = underfill(dt, 5 ,x11)
    O = underfill(x15, 5, x14)
    return O

def solve_4aab4007():
    input_file = '../data/evaluation/4aab4007.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    sp = astuple(height(dt) - 3, width(dt) - 3)
    ndt = crop(dt, (3, 3), sp)
    x1 = asindices(ndt)
    x2 = dmirror(ndt)
    x3 = invert(9)
    x4 = papply(pair, ndt, x2)
    x5 = lbind(apply, maximum)
    x6 = apply(x5, x4)
    x7 = ofcolor(x6, 0)
    x8 = difference(x1, x7)
    x9 = toobject(x8, x6)
    x10 = interval(x3, 9, 1)
    x11 = interval(9, x3, -1)
    x12 = pair(x10, x11)
    x13 = lbind(shift, x9)
    x14 = mapply(x13, x12)
    x15 = paint(x6, x14)
    x16 = asobject(x15)
    x17 = shift(x16, (3, 3))
    x18 = outbox(x17)
    x19 = canvas(1, shape(dt))
    x20 = fill(x19, 4, x18)
    O = paint(x20, x17)
    return O

def solve_3194b014():
    input_file = '../data/evaluation/3194b014.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = objects(dt, T, F, T)
    x2 = order(x1, size)
    x3 = last(x2)
    x4 = color(x3)
    O = canvas(x4, (3, 3))
    return O

def solve_f3cdc58f():
    input_file = '../data/evaluation/f3cdc58f.json'
    with open(input_file, 'r') as f:
        data=json.load(f)
    test_inputs = [item['input'] for item in data.get('test')][0]
    dt = tuple(map(tuple, test_inputs))
    x1 = numcolors(dt)
    x2 = palette(dt)
    x3 = objects(dt, T, F, T)
    x4 = lbind(colorfilter, x3)
    x5 = apply(x4, x2)
    x6 = apply(merge, x5)
    O = canvas(0, shape(dt))
    for item in x6:
        x8 = size(item)
        if (x8 == 0): continue
        x9 = first(item)[0]
        x10 = height(dt)
        x11 = subtract(x10, x8)
        x12 = shoot((x11, x9 - 1), DOWN)
        x7 = fill(x7, x9, x12)
    return O



