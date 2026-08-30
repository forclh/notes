# 作业一答案：作用域判断

x = 1

def func_a():
    x = 2
    
    def func_b():
        print(x)      # 2 —— 按 LEGB 查找，Enclosing 作用域的 x=2
    
    func_b()
    print(x)          # 2 —— Local 作用域的 x=2

func_a()
print(x)              # 1 —— Global 作用域的 x=1
