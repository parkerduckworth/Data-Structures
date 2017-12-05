
def quickSort(list_):
   quickSortHelper(list_,0,len(list_)-1)

def quickSortHelper(list_,first,last):
   if first<last:

       splitpoint = partition(list_,first,last)

       quickSortHelper(list_,first,splitpoint-1)
       quickSortHelper(list_,splitpoint+1,last)


def partition(list_,first,last):
   pivotvalue = list_[first]

   left_pointer = first+1
   right_pointer = last

   done = False
   while not done:

       while left_pointer <= right_pointer and list_[left_pointer] <= pivotvalue:
           left_pointer = left_pointer + 1

       while list_[right_pointer] >= pivotvalue and right_pointer >= left_pointer:
           right_pointer = right_pointer -1

       if right_pointer < left_pointer:
           done = True
       else:
           temp = list_[left_pointer]
           list_[left_pointer] = list_[right_pointer]
           list_[right_pointer] = temp

   temp = list_[first]
   list_[first] = list_[right_pointer]
   list_[right_pointer] = temp


   return right_pointer