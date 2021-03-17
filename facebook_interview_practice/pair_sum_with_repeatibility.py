
def sum_till_num(num):
  total = 0
  for i in range(num):
    total += i
  return total


def numberOfWays(arr, k):
 	'''Given a list of n integers arr[0..(n-1)], 
  determine the number of different pairs of elements within it which sum to k.'''
  result = 0
  track_occurances = {}
  for arr_element in arr:
    track_occurances[arr_element] = arr.count(arr_element)
    
  for item in track_occurances:
    if item == k / 2:
      result += sum_till_num(track_occurances[item]) * 2
    else:
      if (k - item) in track_occurances:
        result += track_occurances[item] * track_occurances[k - item]
  return result//2



k = 6
arr1 = [1, 5, 3, 3, 3, 3, 5, 5]
out1 = numberOfWays(arr1, k)  # should return 9
arr2 = [1, 5, 3, 3, 3, 3, 1, 5]
out2 = numberOfWays(arr2, k)  # should return 10
