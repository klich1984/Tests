#!/usr/bin/python3
try:
    raise Exception('klich', '84')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x = ', x)
    print('y = ', y)
