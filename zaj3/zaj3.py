a, b = 1 / 3, '1/3'
print('a=%f, b=%s' % (a, b))
print('a=%.3f, b=%s' % (a, b))

print('a={}, b={}'.format(a, b))
print('a={:.3f}, b={}'.format(a, b))

print(f'a={a}, b= {b}')
print(f'a={a:.3f}, b={b}')

print(f'{a=}, {b=}')
print(f'{a=:.3f}, {b=}')

# Potrojny cudzyslow zachowuje formatowanie
print(f"""{f'''{f"{1 + 1}"}'''}""")

print('{0}abcdefgh{0}'.format('*'))
print('{1}abcdefgh{0}'.format('*', '**'))
print('{s}abcdefg{0}'.format('*', s='**'))

print('abcd   EfGh'.capitalize())
print('abcd   efGh'.title())

print('abcdEFGH'.lower())
print('abcdEFGH'.swapcase())
print('abcdEFGH'.upper())

print('abcdEFGH'.center(20))
print('abcdEFGH'.center(20, '*'))

print('abcdEFGH'.ljust(20))
print('abcdEFGH'.ljust(20, '*'))

print('abcdEFGH'.rjust(20))
print('abcdEFGH'.rjust(20, '*'))

print('abcdefgh'.removeprefix('ab'))
print('abcdefgh'.removeprefix('gh'))

print('abcdefgh'.zfill(20))

print('    abcdefgh    '.lstrip() + '*')
print('    abcdefgh    '.rstrip() + '*')
print('    abcdefgh    '.strip() + '*')

print('abcd       efgh'.count(' '))
print('abcd       efgh      '.expandtabs().count(' '))

print('abrkakadabra')
print('abrkakadabra'.count('a'))
print('abrkakadabra'.startswith('ab'))
print('abrkakadabra'.endswith('a'))
print('abrkakadabra'.find('a', 4))
print('abrkakadabra'.find('x'))
print('abrkakadabra'.index('a'))
# print('abrkakadabra'.index('x'))

print('abra kadabra'.split())
print('abra kadabra sasasas'.rsplit(' ', 1))

import re

# Tam gdzie wystepuje r obok b (lub na odwrot)
print(re.split('[rb]', 'abra kadabra'))

print('abra\nkadabra'.splitlines())
print('abrakadabra'.partition('br'))

print(''.join(('a', 'b', 'c')))
print('*'.join(('a', 'b', 'c')))

print('abrakadabra'.replace('a', 'A'))

tr = str.maketrans('abc', 'ABC')
print(tr)
print('abrakadabra'.translate(tr))

k = [5, 2, 1, 3, 6]
# k.sort(reverse=true) - blad true z malej nie dziala
print(k)
