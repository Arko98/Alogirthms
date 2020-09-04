def distance(p,q):
  '''
  Utility Functio  to find Eucledian Distance of two points
  '''
  dist = ((p[0]-q[0])**2+(p[1]-q[1])**2)**(1/2)
  return dist

def brute_find(Points):
  '''
  A Brute-Force algorithm to find minimum distance in Points array
  '''
  min_dist = 10000
  for i in range(len(Points)):
    for j in range(i+1,len(Points)):
      if (distance(Points[i],Points[j])<min_dist):
        min_dist = distance(Points[i],Points[j])
  return min_dist

def strip_closest_dist(Strip, Min_Distance):
  '''
  Function to find closest distance within the Strip
  '''
  min_val = Min_Distance
  for i in range(len(Strip)):
    j = i+1
    # Check if inside the strip, distance between two points is less than 'Minimum-Distance'
    while (j<len(Strip) and (Strip[j][1]-Strip[i][1])<min_val):
      # Update Minimum-Distance
      min_val = distance(Strip[i],Strip[j])
      j += 1
  return min_val

def closest_find(Points):
  '''
  Function to find the Actual Minimum Distance
  '''
  if len(Points)<=3:
    return brute_find(Points)
  else:
    # Indicate the mid point of Points Array and choose mid-point
    mid = len(Points)//2
    mid_point = Points[mid] 
    # Recursive Calls to closest_find for sub-arrays
    left_dist = closest_find(Points[:mid])     #Left Sub-Array Call
    right_dist = closest_find(Points[mid+1:])  #Right Sub-Array Call
    dist = min(left_dist,right_dist)
    # strip create for points at distance less than 'dist' from mid-point by comparing x coordinates of points with mid point
    strip = []
    for i in range(len(Points)):
      # checking if distance of Point from mid-point is less than 'dist' (using X Coordinates)
      if (abs(Points[i][0]-mid_point[0])<dist):
        # Add the point in the strip about mid-point within distance 'dist'
        strip.append(Points[i])
    # Finally return minimum of 'dist' and minimum distance of points in strip
    final_min_dist = min(dist,strip_closest_dist(strip,dist))
    return final_min_dist

def closest(Points):
  '''
  Function to sort the Point array according to X coordinates
  '''
  Points.sort(key = lambda P: P[0])
  return closest_find(Points)

# Driver code 
P = [(2, 3),(12, 30),(40, 50),(5, 1),(12, 10),(3, 4)] 
print("The smallest distance is",  closest(P)) 
