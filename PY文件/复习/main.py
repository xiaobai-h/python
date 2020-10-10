# 加上下面代码解决相对路径问题
import xdlj
# 然后就可以愉快使用相对路径了

filename = 'test.txt'
with open(filename) as file_object:
    # file_object.write("I love programming.\n")
    # file_object.write("I love creating new games.\n")
    for line in file_object:
        print(line)
