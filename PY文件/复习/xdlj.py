# 加上下面代码解决相对路径问题
import os
import sys
os.chdir(sys.path[0])
