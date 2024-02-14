#sort

# prices={'Appple':1.99,'Banana': 0.99,'orange':1.49,'cantaloup':3.99,'grapes':0.39}
# # # print(prices)                                             #{'Appple': 1.99, 'Banana': 0.99, 'orange': 1.49, 'cantaloup': 3.99, 'Grapes': 0.39} ..... here item as dictinory
# print(sorted(prices))                                     #['Appple', 'Banana', 'Grapes', 'cantaloup', 'orange']
# print(sorted(prices.values()))                            #[0.39, 0.99, 1.49, 1.99, 3.99]
# print(sorted(prices.keys()))                              #['Appple', 'Banana', 'Grapes', 'cantaloup', 'orange']
# print(sorted(prices.items()))                             #[('Appple', 1.99), ('Banana', 0.99), ('Grapes', 0.39), ('cantaloup', 3.99), ('orange', 1.49)] ....... here items as list
# print(sorted(prices.values(),reverse=True))               #[3.99, 1.99, 1.49, 0.99, 0.39] ..... reverse orderr              


# # a=[1,2,3,4,5]
# b=[100,200,300,400,500]
# c={}
# for i in range (5):
#     c[a[i]]=b[i]
# print(c)                            #{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
  
#........................  Q*0...........................


# a=int(input('enetr a number: '))
# b={}
# for i in range(1,a+1):                #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#     b[i]=i*i
# print(b)