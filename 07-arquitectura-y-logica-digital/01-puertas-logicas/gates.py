def check_values(*args):
    for val in args:
        if val!=0 and val!=1:
            raise ValueError("Not a valid value")

#gate and
def logic_and(val1, val2):
    check_values(val1, val2)
    return val1 and val2

#gate or
def logic_or(val1, val2):
    check_values(val1, val2)
    return val1 or val2
#gate not
def logic_not(val):
    check_values(val)
    return 1 if val == 0 else 0
#gate nand
def logic_nand(val1, val2):
    return logic_not(logic_and(val1, val2))
#gate nor
def logic_nor(val1, val2):
    return logic_not(logic_or(val1, val2))
#gate xor
def logic_xor(val1, val2):
    only_val1=logic_and(val1, logic_not(val2))
    only_val2=logic_and(logic_not(val1),val2)
    return logic_or(only_val1,only_val2)    
#gate xnor
def logic_xnor(val1, val2):
    #All 0 or All 1
    all_off=logic_nor(val1,val2)
    all_on=logic_and(val1,val2)
    return logic_or(all_off,all_on)

if __name__ == "__main__":
    #Test para logic_and logic
    assert logic_and(0,0)==0
    assert logic_and(0,1)==0
    assert logic_and(1,0)==0
    assert logic_and(1,1)==1

    #Test para logic_or logic
    assert logic_or(0,0)==0
    assert logic_or(0,1)==1
    assert logic_or(1,0)==1
    assert logic_or(1,1)==1

    #Test para logic_not logic
    assert logic_not(0)==1
    assert logic_not(1)==0

    #Test para logic_nand logic
    assert logic_nand(0,0)==1
    assert logic_nand(0,1)==1
    assert logic_nand(1,0)==1
    assert logic_nand(1,1)==0

    #Test para logic_nor logic
    assert logic_nor(0,0)==1
    assert logic_nor(0,1)==0
    assert logic_nor(1,0)==0
    assert logic_nor(1,1)==0

    #Test para logic_xor logic
    assert logic_xor(0,0)==0
    assert logic_xor(0,1)==1
    assert logic_xor(1,0)==1
    assert logic_xor(1,1)==0

    #Test para logic_xnor logic
    assert logic_xnor(0,0)==1
    assert logic_xnor(0,1)==0
    assert logic_xnor(1,0)==0
    assert logic_xnor(1,1)==1

    print("Test para logic: todos los gates han sido existosos")