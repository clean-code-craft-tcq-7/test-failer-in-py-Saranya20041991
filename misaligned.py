def color_index_to_pair_num(major_index,minor_index):
    return major_index * 5 + minor_index +1
 
def color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_list = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            index = color_index_to_pair_num(i,j)
            color_pair = f"{index:^2} | {major:>6} | {minor}"
            color_list.append(color_pair)
    return color_list
 
result = color_map()
for line in result:
    print(line)
assert(result[0] == '1  |  White | Blue')
assert(result[6] == '7  |    Red | Orange')
assert(result[13] == '14 |  Black | Brown')
assert(result[17] == '18 | Yellow | Green')
assert(result[24] == '25 | Violet | Slate')
assert(color_index_to_pair_num(0,0) == 1 )
assert(color_index_to_pair_num(3,4) == 20 )
print("All is well (maybe!)")