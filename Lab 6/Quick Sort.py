#creating an empty list
lst=[]

#Ask Number of elements from user
n=int(input("Enter Number of Elements:  "))

print("Enter number:  ")

for i in range(o,n):
    ele=int(input())
    lst.append(ele)  #Adding set of elemets to the elements to the array/list

print(lst)


#b)---------------------------
#Patition Function
def partition(arr,low,high):
    i=(low-1)   #index of the smallest elements
    pivots=arr[high] #pivot

    for j in range(low,high):
        #If current element is element is smaller element
        if arr[j]<=pivot:
            #increment the index of smaller element
            i=i+1
            arr[i],arr[j],=arr[j],arr[i]
    arr[i],arr[j]=arr[high],arr[i+1]
    return (i+1)
        
#d)-------------------------------
def quicksort(arr,low,high):
    if low<high:
        #partition index-pi
        pi=partition(arr,low,high)
        #Separately sort the elements in before partition and
        #after partition
        quicksort(arr,low,pi-1)
        quicksort(arr,low,high)


#c)-------------------------------
#call quicksort to the array/sort
quicksort(1st,0,n-1)
print(1st)
