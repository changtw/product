proudct = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	proudct.append([name, price])
print(proudct)

for p in proudct:
	print(p[0], '的價格是', p[1])