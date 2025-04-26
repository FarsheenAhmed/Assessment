def max_sum(arr):
    if len(arr) < 2:
        return 0
    else:
        arr.sort(reverse = True)
        return arr[1]+arr[2] 
        
    
arr = [6,7,1,3,8,2,5]
print(max_sum(arr))
        

