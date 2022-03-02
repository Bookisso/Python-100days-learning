'''
身份验证
'''

username = input('请输入用户名：')
password = input('请输入口令：')

if username == 'admin' and password == '123456' :
	print('验证成功！')
else :
	print('验证失败！')