arr = [5, 5, 0, 4, 1, 4, 5, 5, 3, 2  ]; 
destination = len(arr) 

def min_no_of_airport(arr, n): 
    jump_to_other_airport = [0 for i in range(n)] 
  
    if (n == 0) or (arr[0] == 0): 
        return float('inf') 
  
    jump_to_other_airport[0] = 0
  
    for i in range(1, n): 
        jump_to_other_airport[i] = float('inf') 
        for j in range(i): 
            if (i <= j + arr[j]) and (jump_to_other_airport[j] != float('inf')): 
                jump_to_other_airport[i] = min(jump_to_other_airport[i], jump_to_other_airport[j] + 1) 
                break
    return jump_to_other_airport[n-1] 
  
print('Minimum number of jumps to reach last destination is except first airport', min_no_of_airport(arr, destination))