import random
total=0
def h_or_t():
    num = random.randint(0, 1)
    if num == 0:
        return "tails"
    if num == 1:
        return "heads"

def sort(arr,total):
    while True:
        #global total
        total+=1
        sorted_ = True
        x = 0
        while x < len(arr) - 1:
            currentval = arr[x]
            currentval2 = arr[x-1]
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
                    arr.insert(y, currentval2)
                    print(arr)
            
            for i in range (len(arr)-1):
                if arr[i] > arr[i + 1]:
                    sorted_ = False
                    print(arr)
                    break
                
            x += 1
            
        if sorted_:
            print("Sorted result:", arr)
            return total
#Change this to your own number
num = [5,2]
total=sort(num,total)
print("Total Moves were:",total)