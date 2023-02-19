monkeys = {}

x = [line.strip() for line in open(0)]

for a in x :    
   name, expr = a.split(": ")
   if expr.isdigit() :
       monkeys[name] = int(expr)
   else :
       left, op, right = expr.split()
       if left in monkeys and right in monkeys :
           monkeys[name] = eval(f"{monkeys[left]} {op} {monkeys[right]}")
       else :
           x.append(a)

print(monkeys["root"])

import sympy

monkeys = { "humn" : sympy.Symbol("x") }
x = [line.strip() for line in open(0)]

ops = {
   "+": lambda x, y: x + y,
   "-": lambda x, y: x - y,
   "*": lambda x, y: x * y,
   "/": lambda x, y: x / y,
}


for a in x :    
   name, expr = a.split(": ")
   if name in monkeys : continue
   if expr.isdigit() :
       monkeys[name] = sympy.Integer(expr)
   else :
       left, op, right = expr.split()
       if left in monkeys and right in monkeys :
           if name == "root" :
               print(sympy.solve(monkeys[left] - monkeys[right])[0])
               break
           monkeys[name] = ops[op](monkeys[left], monkeys[right])
       else :
           x.append(a)

# import functools, operator, re, z3
# L = list(map(functools.partial(re.findall, r'[^: \n]+'), open(0).readlines()))
# V = {x: z3.Int(x) for x in set(map(operator.itemgetter(0), L))}
# def solve(target):
#   s = z3.Solver()
#   for line in L:
#     match line:
#       case ['humn', v] if target != 'humn': s.add(V['humn'] == int(v))
#       case [n, v] if n != 'humn': s.add(V[n] == int(v))
#       case ['root', l, _, r] if target != 'root': s.add(V[l] == V[r])
#       case [n, l, '+', r]: s.add(V[n] == V[l] + V[r])
#       case [n, l, '-', r]: s.add(V[l] == V[n] + V[r])
#       case [n, l, '*', r]: s.add(V[n] == V[l] * V[r])
#       case [n, l, '/', r]: s.add(V[l] == V[n] * V[r])
#   s.check()
#   print("{}: {}".format(target, s.model().eval(V[target])))
# solve('root')
# solve('humn')
