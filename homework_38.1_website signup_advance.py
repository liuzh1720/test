name = input('请输入用户名')
password = ''
d = {'popcorn':1,'sniper':9}

if name in d.keys():
    print('该用户已经注册')
    name = input('请重新输入用户名')
else:
    password = input('请输入密码:')
    d[name] = password

print('-'*10)
print('目前已经注册的用户有：',*d.keys(),sep = '\n')

