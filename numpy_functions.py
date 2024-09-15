import numpy as np

def function1():
    a1 = np.array([1,2,3])
    a2 = np.array([3,2,1])
    res = a1 + a2
    print(res)
    res = a1 - a2
    print(res)
    res = a1 * a2
    print(res)
    res = a1/a2
    print(res)
    res = a1// a2
    print(res)
    res = a1 % a2
    print(res)
    res = a1 ** a2
    print(res)
    res = a1 == a2
    print(res)
function1()

def function2():
    arr = np.array([1,2,3])
    res = arr + 10
    print(res)
    res = arr <= 2
    print(res)
    res = arr1 = 2
    print(res)
function2()

def function3():
    arr = np.array([11,22,33,44,55])
    print(arr[1])
    print(arr[-3])
    for i in arr:
        print(i)
    for i in range(arr.size):
        print(f"arr[{i}] = {arr[i]}")
function3()

def function4():
    arr = np.array([11,22,33,44,55])
    print(arr[1:4])
    print(arr[::-1])
function4()

def function5():
    arr = np.array([11,22,33,44,55,66,77])
    indexes = [1,2,4,6]
    print(f"arr[{indexes}] = ",arr[indexes])
    selected = [True,False,True,False,False,True,False]
    print(f"arr [{selected}]", arr[selected])
function5()

def function6():
    # filtering function
    arr = np.array([11,22,33,44,55,66,77,88])
    selected = arr % 2 == 0
    print("even selected: ",selected)
    evens = arr[selected]
    print("even nums: ",evens)
    odds = arr[arr%2!=0]
    print(odds)
    more_than_50 = arr[arr>50]
    print(more_than_50)
function6()

def function7():
    arr = np.array([11,22,33,44,55,66,77,88,99])
    print("Even and Div by 3 numbers: ",arr[(arr%2 == 0)|(arr%3 == 0)])
function7()
