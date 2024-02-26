def decor(function):
    def init(*args):
        mylist = [*args]
        summ, ints, strs, floats = 0, 0, 0, 0
        for x in mylist:
            summ += 1
            if type(x) is int:
                ints += 1
            elif type(x) is int:
                strs += 1
            elif type(x) is int:
                floats += 1
            print(f'Hammasi {summ}')
            print(f'Int {ints}')
            print(f'Str {strs}')
            print(f'Float {floats}')
            svg = function(*args)
            return svg
        return init

@decor
def Hammasi_info(*args):
    mylist = [*args]
    ints, strs, floats = [], [], []
    for i in mylist:
        if type(i) is int:
            ints.append(i)
        elif type(i) is str:
            strs.append(i)
        elif type(i) is float:
            floats.append(i)
        print(f"""
Int: {ints}
Str: {strs}
Float: {floats}""")

Hammasi_info(1,2,3,4342342, 1.3, 3.5,'Umar')
