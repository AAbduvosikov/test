nums = [8,1,2,2,3]
rezult = []
a = min (nums)
print (a)
con = 0
for i in nums:
    if (a<i):
        con += 1
    rezult.append(con)
print (rezult)
    
