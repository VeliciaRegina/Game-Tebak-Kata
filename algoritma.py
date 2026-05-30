def merge_sort(arr):
   '''Mengurutkan data dari yang terkecil ke terbesar.'''
   if len(arr) <= 1:
      return arr
   
   mid = len(arr) // 2
   leftHalf = arr[:mid]
   rightHalf = arr[mid:]
   sortedLeft = merge_sort(leftHalf)
   sortedRight = merge_sort(rightHalf)
   return merge(sortedLeft, sortedRight)

def merge(left, right):
   hasil = []
   i = j = 0

   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         hasil.append(left[i])
         i += 1
      else:
         hasil.append(right[j])
         j += 1
   
   hasil.extend(left[i:])
   hasil.extend(right[j:])
   return hasil

def binary_search(arr, target):
   '''Mencari sebuah data dan mengembalikan indeksnya'''
   left = 0
   right = len(arr) -1

   while left <= right:
      mid = (left + right) // 2

      if arr[mid] == target:
         return mid
      if arr[mid] < target:
         left = mid + 1
      else:
         right = mid - 1
   return False

