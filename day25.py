# get the key of a min value from the given dict
d={'b':8,'a':10}  
# print(min (d))
min_key=None
min_value=None
for key,value in d.items():
    if min_value is None or value<min_value:
        min_value=value
        min_key=key
print('min value',min_value)





# data={'item1':45.5,'item2':2.35,'item3':41.30,'item4':.55,'item5':.24}




# calculate the sum and average of the  digits present in a string(already done)

