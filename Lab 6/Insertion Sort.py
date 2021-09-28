#Insertion Sort Algorithm  #asending order

#creating an empty list
lst=[]

#Ask Number of elements from user
n=int(input("Enter Number of Elemnts: "))

print("Enter numbers:   ")

for i in range(0,n):
      ele=int(input())
      lst.append(ele)   #Adding set of elements to the array/list

print(lst)




#Function to do insertion sort

def insertionSort(arr):

    #Traverse through 1 to len(arr)
    for i in range(1,len(arr)):
        key=arr[i]
        #Move elements of arr[0..i-1], that are
        #greater than key, to one postition ahead
        #of their  current posstion ahead
        #of their current position
        j=1-1
        while j>1 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1] = key



#calling to the function

insertionSort(1st)
#printing the sorting array
print("Sorted array is:  ")
#for i in range (len(1st));
#print("%d" $lst[1])
print(1st)


    
