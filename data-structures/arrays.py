from array import array

# check the bytecodes here 
# https://docs.python.org/3/library/array.html
int_array = array('b', [0] * 4)
print(int_array)
print(int_array[0])
print(len(int_array))
int_array[0] = 127 # since signed byte uses last bit 0--- ---- as the sign the max value is 2^7 or 127
print(int_array[0])

for arr in int_array:
    print(arr)
