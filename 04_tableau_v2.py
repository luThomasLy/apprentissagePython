width =  int(input("Please enter width : "))

price_width = 10
item_width = width - price_width

header_fmt = '{{var3:{var1}}}{{var4:>{var2}}}'.format(var1=item_width, var2=price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)
#print("Header format : ")
#print(header_fmt)
print(header_fmt.format(var3='Article', var4='Prix'))

print('-' * width)
print(fmt.format('Pommes', 0.4))
print(fmt.format('Poires', 0.7))
print(fmt.format('Clémentines', 1.12))
print(fmt.format('Bananes', 0.787))
print(fmt.format('Abricots', 12.4))

print('=' * width)

print("{:5.2f}".format(33333.141414))