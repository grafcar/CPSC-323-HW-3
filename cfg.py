def S (value):
    if value[0] == "a":
        print(value)
        return S(value[1:])
    elif value[0] == "b":
        print(value)
        return B(value[1:])
    elif value[0] == "c":
        print(value)
        return C(value[1:])
    elif value[0] == "$":
        print("Accepted")
        return

def B (value):
    if value[0] == "b":
        print(value)
        return B(value[1:])
    elif value[0] == "a":
        print(value)
        return C(value[1:])
    elif value[0] == "c":
        print(value)
        return D(value[1:])
    else: 
        print("Ended B")
        return 

def C(value):
    if value[0] == "a":
        print(value)
        return S(value[1:])
    elif value[0] == "b":
        print(value)
        return D(value[1:])
    elif value[0] == "c":
        print(value)
        return D(value[1:])
    else:
        print("Ended C")
        return 

def D(value):
    if value[0] == "b":
        print(value)
        return D(value[1:])
    elif value[0] == "a":
        print(value)
        return B(value[1:])
    elif value[0] == "c":
        print(value)
        return C(value[1:])
    else:
        print("Ended D")
        return 

S("ccccbbb$")