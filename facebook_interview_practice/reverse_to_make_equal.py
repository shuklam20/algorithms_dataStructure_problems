def are_they_equal(array_a, array_b):
  '''
  Given two arrays A and B of length N, determine if there 
  is a way to make A equal to B by reversing any subarrays 
  from array B any number of times.
  '''
  track_dict = {}
  for i in array_a:
    if i in track_dict:
      track_dict[i] += 1
    else:
      track_dict[i] = 1
      
  for j in array_b:
    if j not in track_dict:
      return False
    else:
      track_dict[j] -= 1
    
  return not any(track_dict.values())


a = [1, 1, 3, 4, 5, 8]
b = [8, 3, 4, 1, 5, 1]  
expected_3 = are_they_equal(a, b) # should get True