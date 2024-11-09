import copy
import random
import itertools

a = [i for i in range(10)]

def op_2_exp(n, op, type, equal, x, y, z):
  if equal == 1:
    if type == 0:
      return f'{n}. {x} {op} {y} = {z}'
    elif type == 1:
      return f'{n}. {x} {op} {y} = (  )'
    elif type == 2:
      return f'{n}. (  ) {op} {y} = {z}'
    elif type == 3:
      return f'{n}. {x} {op} (  ) = {z}'
  else:
    if type == 0:
      return f'{n}. {z} = {x} {op} {y}'
    elif type == 1:
      return f'{n}. (  ) = {x} {op} {y}'
    elif type == 2:
      return f'{n}. {z} = (  ) {op} {y}'
    elif type == 3:
      return f'{n}. {z} = {x} {op} (  )'

'''
equal 参数表示等号的位置, 1 表示 value 在等号的左侧, 0 表示在右侧。
type 参数表示 (  ) 占位符的不同位置：
type = 0: 没有占位符。
type = 1: 等号一侧为 (  ) = 表达式。
type = 2: x 后插入 (  )。
type = 3: y 后插入 (  )。
type = 4: z 后插入 (  )。
'''
def op_3_exp(n, type, equal, value, x, op1, y, op2, z):
    """
    打印三元运算表达式。
    :param n: 表达式的编号
    :param type: 占位符类型
    :param equal: 等号的位置（左或右）
    :param value: 等式的值
    :param x: 第一个操作数
    :param op1: 第一个操作符（+ 或 -)
    :param y: 第二个操作数
    :param op2: 第二个操作符（+ 或 -)
    :param z: 第三个操作数
    """
    if equal == 1:  # 等号在左侧
        if type == 0:
            return f"{n}. {value} = {x} {op1} {y} {op2} {z}"
        elif type == 1:
            return f"{n}. (  ) = {x} {op1} {y} {op2} {z}"
        elif type == 2:
            return f"{n}. {value} = (  ) {op1} {y} {op2} {z}"
        elif type == 3:
            return f"{n}. {value} = {x} {op1} (  ) {op2} {z}"
        elif type == 4:
            return f"{n}. {value} = {x} {op1} {y} {op2} (  )"
    else:  # 等号在右侧
        if type == 0:
            return f"{n}. {x} {op1} {y} {op2} {z} = {value}"
        elif type == 1:
            return f"{n}. (  ) {op1} {y} {op2} {z} = {value}"
        elif type == 2:
            return f"{n}. {x} {op1} (  ) {op2} {z} = {value}"
        elif type == 3:
            return f"{n}. {x} {op1} {y} {op2} (  ) = {value}"
        elif type == 4:
            return f"{n}. {x} {op1} {y} {op2} {z} = (  )"


def l_r_equal_exp(n, op1, op2, type, a, b, c, d):
  if type == 0:
    return f'{n}. {a} {op1} {b} = {c} {op2} {d}'
  elif type == 1:
    return f'{n}. (  ) {op1} {b} = {c} {op2} {d}'
  elif type == 2:
    return f'{n}. {a} {op1} (  ) = {c} {op2} {d}'
  elif type == 3:
    return f'{n}. {a} {op1} {b} = (  ) {op2} {d}'
  elif type == 4:
    return f'{n}. {a} {op1} {b} = {c} {op2} (  )'
  elif type == 5:
    return f'{n}. (  ) {op1} (  ) = {c} {op2} {d}'
  elif type == 6:
    return f'{n}. {a} {op1} {b} = (  ) {op2} (  )' 
  elif type == 7:
    return f'{n}. (  ) {op1} {b} = (  ) {op2} {d}'
  elif type == 8:
    return f'{n}. {a} {op1} (  ) = {c} {op2} (  )'
  elif type == 9:
    return f'{n}. (  ) {op1} {b} = {c} {op2} (  )' 
  elif type == 10:
     return f'{n}. {a} {op1} (  ) = (  ) {op2} {d}'
  assert 0, f'unknow type: {type}'
   

def add_10(n, type, sample=0):
  combinations = []
  for x in a:
    for y in a:
      z = x + y
      if z > 10:
        continue
      exp = op_2_exp(n, '+', type, 1, x, y, z)
      combinations.append(exp)
      n += 1
      exp = op_2_exp(n, '+', type, 2, x, y, z)
      combinations.append(exp)
      n +=1
  return n, combinations if sample < 1 else random.sample(combinations, sample)


def sub_10(n, type, sample=0):
  combinations = []
  b = copy.deepcopy(a)
  b.reverse()
  for x in b:
    for y in a:
      z = x - y
      if (z) < 0:
        continue
      exp = op_2_exp(n, '-', type, 1, x, y, z)
      combinations.append(exp)
      n += 1
      op_2_exp(n, '-', type, 2, x, y, z)
      combinations.append(exp)
      n += 1
  return n, combinations if sample < 1 else random.sample(combinations, sample)


def generate_combinations_3(n, numbers, ops, sample=0):
    # 生成三元运算组合
    ternary_combinations = []
    for a, b, c in itertools.permutations(numbers, 3):
        for op1 in ops:
            for op2 in ops:
                exp = f"{a} {op1} {b}"
                value = eval(exp)
                if value < 0 or value > 10:
                  continue
                exp = f"{a} {op1} {b} {op2} {c}"
                value = eval(exp)
                if value < 0 or value > 10:
                  continue
                for type in range(0, 5):
                  exp = op_3_exp(n, type, 1, value, a, op1, b, op2, c)
                  ternary_combinations.append(exp)
                  n += 1
                  exp = op_3_exp(n, type, 2, value, a, op1, b, op2, c)
                  ternary_combinations.append(exp)
                  n += 1
    
    return n, ternary_combinations if sample < 1 else random.sample(ternary_combinations, sample)

def generate_combinations_4(n, numbers, ops, sample=0):
    # 生成四元运算组合
    combinations = []
    for a, b, c, d in itertools.permutations(numbers, 4):
        for op1 in ops:
            for op2 in ops:
                left = f"{a} {op1} {b}"
                right = f"{c} {op2} {d}"
                left_value = eval(left)
                right_value = eval(right)
                if left_value < 0 or left_value > 10 or left_value != right_value:
                  continue
                for type in range(0, 11):
                  exp = l_r_equal_exp(n, op1, op2, type, a, b, c, d)
                  combinations.append(exp)
                  n += 1
    return n, combinations if sample < 1 else random.sample(combinations, sample)

def generate_comparison_expressions(n, numbers, sample=0, show_answer=False):
    """
    生成比较运算表达式。
    :param n: 表达式的编号
    :param numbers: 可用的数字列表
    :param sample: 采样数量
    :param show_answer: 是否显示标准答案
    :return: 更新后的编号和生成的表达式列表
    """
    comparisons = []
    operators = ['>', '<']
    
    for op in operators:
        for a in numbers:
            # ( ) > a
            if op == '>':
                answer = a + 1
            else:
                answer = a - 1
            if 0 <= answer < 10:
                exp = f"{n}. (  ) {op} {a}"
                if show_answer:
                    exp += f"  # ({answer}) {op} {a}"
                comparisons.append(exp)
                n += 1
            
            # a > ( )
            if op == '>':
                answer = a - 1
            else:
                answer = a + 1
            if 0 <= answer < 10:
                exp = f"{n}. {a} {op} (  )"
                if show_answer:
                    exp += f"  # {a} {op} ({answer})"
                comparisons.append(exp)
                n += 1
            
            for b in numbers:
                # ( ) + a > b + ( )
                if op == '>':
                    answer_left = b + 1
                    answer_right = a - 1
                else:
                    answer_left = b - 1
                    answer_right = a + 1
                if 0 <= answer_left < 10 and 0 <= answer_right < 10 and (answer_left + a) <= 10:
                    exp = f"{n}. (  ) + {a} {op} {b} + (  )"
                    if show_answer:
                        exp += f"  # ({answer_left}) + {a} {op} {b} + ({answer_right})"
                    comparisons.append(exp)
                    n += 1
                
                # a + b < ( ) - ( )
                if op == '>':
                    answer = a + b + 1
                else:
                    answer = a + b - 1
                if 0 <= answer < 10 and (a + b) < 10:
                    exp = f"{n}. {a} + {b} {op} (  ) - (  )"
                    if show_answer:
                        exp += f"  # {a} + {b} {op} ({answer}) - ( )"
                    comparisons.append(exp)
                    n += 1

                # a + b < ( ) - ( ) with answer
                if op == '>':
                    answer = a + b + 1
                else:
                    answer = a + b - 1
                if 0 <= answer < 10 and (a + b) < 10:
                    exp = f"{n}. {a} + {b} {op} (  ) - (  )"
                    if show_answer:
                        exp += f"  # {a} + {b} {op} ({answer}) - ( )"
                    comparisons.append(exp)
                    n += 1

    return n, comparisons if sample < 1 else random.sample(comparisons, sample)

all = []

n = 0
n, r = add_10(n, 0)
all += r
n, r = sub_10(n, 0)
all += r

n, r = add_10(0, 1)
all += r
n, r = add_10(n, 2)
all += r
n, r = add_10(n, 3)
all += r

n, r = sub_10(n, 1)
all += r
n, r = sub_10(n, 2)
all += r
n, r = sub_10(n, 3)
all += r

all = random.sample(all, 160)

print('-'*10)

numbers = a + [10]
ops = ['+', '-']

n, combinations_3 = generate_combinations_3(n, numbers, ops, 20)
all += combinations_3

n, combinations_4 = generate_combinations_4(n, numbers, ops, 20)
all += combinations_4

n, comparison_expressions = generate_comparison_expressions(n, numbers, 5, show_answer=True)
exp_comparison = map(lambda x: x.split('#')[0], comparison_expressions)
all += exp_comparison

all = map(lambda x: x.split('. ')[1], all)
all = list(filter(lambda x: '(' in x, all))
all = list(filter(lambda x: '0' not in x, all))
random.shuffle(all)
all = all[0:100]

print("\n运算组合:")
for idx, combo in enumerate(all):
    print(f'{idx+1}. {combo}')
