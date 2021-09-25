def set_register(s):
    if ' ' in s:
        return s.upper()
    else:
        return s.lower()
print(set_register('hello world'))
print(set_register('hello,world'))

def get_sum(a, b, c, d):
    return a + b + c + d

print(get_sum(1, 2, 5, 7))