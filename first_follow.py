# Follow Only HALF Done

non_terminals = []
terminals = []
grammar = dict()

def find_first(nt):
   temp_first = []
   if nt == '@' or nt in terminals:
      temp_first.extend(nt)
   else:
      for prod in grammar[nt]:
         temp_first.extend(find_first(prod[0]))
   return temp_first

def find_follow(nt):
   temp_follow = []
   if nt == start_symbol:
      temp_follow.extend('$')
   for prod in prods:
      l = len(prod)
      for i in range(l):
         if prod[i] != nt:
            continue

         if i == l - 1:
            temp_follow.extend(follow(nt))
         elif prod[i+1] in terminals:
            temp_follow.extend(prod[i+1])
         elif prod[i+1] in non_terminals:
            temp_follow.extend(first[non_terminals.index(prod[i+1])])
   return temp_follow

non_terminals = ['S', 'A', 'B']
terminals = ['a', 'b', 'c']
start_symbol = 'S'
grammar = {
   'S': ['AaAb', 'bBAa'],
   'A': ['c', '@'],
   'B': ['c']
}

first = []
for nt in non_terminals:
   first.append(find_first(nt))
print("First: ", first)


prods = []
for v in grammar.values():
   for prod in v:
      prods.append(prod)
follow = []
for nt in non_terminals:
   follow.append(find_follow(nt))
   print(nt, follow)
print("Follow: ", follow)
