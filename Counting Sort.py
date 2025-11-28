arr=[1,4,2,1,6,4,2,7,3,4]
max_number=arr[0]
for i in range(len(arr)):
    if(arr[i]>max_number):
        max_number=arr[i]
        
count = [0 for i in range(max_number+1)]
for i in range (len(arr)):
    count[arr[i]] = count[arr[i]]+1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i)