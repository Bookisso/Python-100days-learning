'''
F = float(input('请输入华氏温度:'))
C = (F - 32) / 1.8
print('摄氏温度是:', C)

r = float(input('请输入半径:'))
S = 3.14 * r *r 
C = 2 * 3.14 * r
print(f'面积是:{S:.1f}, 周长是:{C:.1f}')
'''

'''
# 直接版
year = int(input('请输入年份:'))
if ( year % 100 == 0) :
	if ( year % 400 == 0) :
		print('是闰年')
	else :
		print('不是闰年')
else :
	if ( year % 4 == 0) :
		print('是闰年')
	else :
		print('不是闰年')
'''

# 优化版
year = int(input('请输入年份:'))
is_leap = (year % 400 == 0) or ( (year % 100 != 0) and (year % 4 == 0) )
print(is_leap)