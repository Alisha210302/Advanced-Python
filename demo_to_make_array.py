import numpy as np
from numpy.ma.core import reshape


def print_array_info(arr):
    print("arr = ",arr)
    print("arr dtype = ",arr.dtype)
    print("arr itemsize = ",arr.itemsize)
    print("no of items = ",arr.size)
    print("total size = ",arr.nbytes)
    print("arr dimensions = ",arr.ndim)
    print("arr shape  = ",arr.shape)
    print("arr flags = ",arr.flags)


def function2():
    arr1 = np.array([11,22,33,44,55])
    print_array_info(arr1)
    arr2 = np.array([11,22,33,44,55],dtype=np.int8)
    print_array_info(arr2)
    arr3 = np.array([11,22,33,44,55],dtype=np.uint8)
    print_array_info(arr3)
    arr4 = np.array([1.1,2.2,3.3,4.4,5.5],dtype=np.float16)
    print_array_info(arr4)
    arr5 = np.array([1.1,11,67,True],dtype=np.int8)
    print_array_info(arr5)
function2()

# to create arrays in different ways

def function3():
    # numpy array of from list collection
    arr1 = np.array([11,22,33])
    print_array_info(arr1)
    # numpy array from tuple collection
    arr2 = np.array((11,22,33,44))
    print_array_info(arr2)
    # numpy array from list of lists
    arr3 = np.array([[10,20,30],[40,50,60]])
    print_array_info(arr3)
function3()

def function4():
    # array from range of elements
    arr1 = np.arange(1,5)
    print_array_info(arr1)
    # array of all 1s
    arr2 = np.ones(5,dtype=np.int8)
    print_array_info(arr2)
    arr3 = np.ones((3,4),dtype=np.int8)
    print_array_info(arr3)
    # array of zeros
    arr4 = np.zeros(5)
    print(arr4)
    arr5 = np.zeros((3,4),dtype=np.int8)
    print_array_info(arr5)
    # array of random numbers
    arr6 = np.random.randint(10,50,size=5)
    print_array_info(arr6)
function4()

def function5():
    arr1 = np.array([[1,2,3,4],[5,6,7,8]])
    print_array_info(arr1)
    arr2 = arr1.reshape((4,2))
    print_array_info(arr2)
    arr3 = arr1.reshape((8,))
    print_array_info(arr3)
function5()

def function6():
    arr1 = np.array([[10,20,30],[40,50,60]])
    print_array_info(arr1)

    arr2 =arr1.flatten()
    print_array_info(arr2)
function6()

def function7():
    arr1 = np.array([11,22,33,44,55])
    arr1[1] = 1
    arr1[2] = 2
    print_array_info(arr1)
    print(arr1)            #[11  1  2 44 55]
    arr2 = arr1.copy()
    arr2[3] = 3
    print(arr2)       # [11  1  2  3 55]
    print(arr1)       #[11  1  2 44 55]
function7()

def function8():
    arr1 = np.array([11,22,33,44,55])
    arr2 = arr1.view()
    arr1[0] = 0
    arr1[1] = 1
    arr2[2] = 2
    arr2[3] = 3
    print("\n\n\n\n",arr1)   #[ 0  1  2  3 55]
    print(arr2)           #[ 0  1  2  3 55]
function8()

def function9():
    arr1 = np.array([[10,20,30],[40,50,60]])
    print_array_info(arr1)
    arr1.resize([3,2])
    print_array_info(arr1)
function9()
