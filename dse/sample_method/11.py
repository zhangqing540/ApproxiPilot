import random
def getneighbour(start_set):
    neighbour=[]
    for idx in range(0,16):
        if idx<=8:
            single_uint_lib=[single for single in mul_name if single != start_set[idx]]
            for uint in single_uint_lib:
                start_set[idx]=uint
                neighbour.append(start_set)
        else:
            single_uint_lib=[single for single in add16_name if single != start_set[idx]]
            for uint in single_uint_lib:
                start_set[idx]=uint
                neighbour.append(start_set)
    return neighbour
mul_name=["mul8u_17R6", "mul8u_17C8", "mul8u_R36", "mul8u_T83","mul8u_874","mul8u_197B", "mul8u_2NDH", "mul8u_Z9D", "mul8u_L93","mul8u_17MJ", "mul8u_4X5", "mul8u_12KA", "mul8u_18UH","mul8u_19XF", "mul8u_ZDF", "mul8u_GTR", "mul8u_1JJQ","mul8u_1A0M", "mul8u_8U3", "mul8u_ZB3"]
add16_name=["add16u_0U8", "add16u_0KU", "add16u_0GX", "add16u_0PT", "add16u_0K3","add16u_0HK", "add16u_0EZ", "add16u_08V", "add16u_1A5", "add16u_126","add16u_0SL", "add16u_0J3", "add16u_162", "add16u_110", "add16u_15Q","add16u_067", "add16u_0SD", "add16u_0KG", "add16u_0RJ", "add16u_0NL"]
init_set=random.sample(mul_name,9)+random.sample(add16_name,8)
neighbor=getneighbour(init_set)
next_design = random.choices(neighbor)
print(next_design[0])
