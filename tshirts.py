
def size(cms):
    if cms > 35 and cms < 38:
        return 'S'
    elif cms > 37 and cms < 42:
        return 'M'
    elif cms > 41 and cms < 45:
        return 'L'
   
assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(37) == 'S')
assert(size(38) == 'S')
assert(size(36) == 'M')
assert(size(38) == 'M')
assert(size(42) == 'M')
assert(size(40) == 'L')
assert(size(42) == 'L')
 
print("All is well (maybe!)")
