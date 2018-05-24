import os
#讀取檔案
product = []
if os.path.isfile('product.csv'): #檢察檔案在不在
	print('yeah! 找到檔案了')
	with open('product.csv', 'r', encoding='utf-8')as f:
		for line in f:
			if '品項,價錢' in line:
				continue #跳過 繼續
			name, price =line.strip().split(',')
			product.append([name,price])
	print(product)

else:
	print('找不到檔案')


#使用者輸入 
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	product.append([name, price])
print(product)

for p in product:
	print(p[0], '的價格是', p[1])

#儲存檔案
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('品項,價錢\n' )
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')