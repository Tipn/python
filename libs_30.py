def get_count(string, symbol):
    cnt = 0
    for i in string:
        if i == symbol:
            cnt += 1
    return cnt

def get_len(string):
    cnt = 0
    for i in string:
        cnt += 1
    return cnt

print(__name__)     # возвращает имя подключенной libs(текущего файла) тоесть libs_30
print('Hello, I am libs.py') 