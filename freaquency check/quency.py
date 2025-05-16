test_dict = {'Codingal' : 2, 'is' : 2, 'best': 2, 'for': 2, 'Coding': 1}
print("The original dictionary :" + str(test_dict))
k =2
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res += 1
    
print("The frequency of " + str(k) + " is : " + str(res))