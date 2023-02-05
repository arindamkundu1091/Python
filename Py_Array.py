import array

class Py_Array:
    arr = array.array('i',[])
    print()
    for i in range (0,5,+1):
        arr.append(i)

    for i in range (0,len(arr),+1):
        print(arr[i],end=" ")
