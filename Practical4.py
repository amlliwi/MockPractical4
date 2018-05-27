'''Question 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 6 marks
Given a list of unique numbers, swap the minimal and maximal elements of this
list, printing the resulting list'''

def swap(m):
    ma=m.index(max(m))
    mi=m.index(min(m))
    m[ma],m[mi]=m[mi],m[ma]
    return m

l=[1,2,3,4]
print(swap(l))
