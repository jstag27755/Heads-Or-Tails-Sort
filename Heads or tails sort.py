import random
global total
total=0
def h_or_t():
    num = random.randint(0, 1)
    if num == 0:
        return "tails"
    if num == 1:
        return "heads"

def sort(arr,total):
    while True:
        total+=1
        sorted_ = True
        x = 0
        while x < len(arr) - 1:
            currentval = arr[x]
            htval = h_or_t()
            
            if htval == "heads":
                arr.pop(x)
                y = x + 1
                arr.insert(y, currentval)
                print(arr)
            
            elif htval == "tails":
                if x > 0:
                    arr.pop(x - 1)
                    y = x
                    arr.insert(y, currentval)
                    print(arr)
            
            if x + 1 < len(arr) and arr[x] > arr[x + 1]:
                sorted_ = False
                print(arr)
                break
                
            x += 1
            
        if sorted_:
            print("Sorted result:", arr)
            break

num = [8,3,6,1,10,9,4,2,5,7]
sort(num,total)
print(total)