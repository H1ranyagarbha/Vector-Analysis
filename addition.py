import numpy as n

def addition():
  print()
  print("The resultant of Vector A and Vector B is equal to this vector:")

  s_1=[]
  for i in range(0,3):
     l=int(input("List out the coordinates of the first vector one at a time (this will repeat thrice):"))
     s_1.append(l)
  print("Vector A's Components are:")
  print(s_1)

  s_2=[]
  for i in range(0,3):
     k=int(input("List out the coordinates of the second vector one at a time (this will repeat thrice):"))
     s_2.append(k)
  print("Vector B's components are:")
  print(s_2)

  vectorAbar = np.array(s_1)
  vectorBbar = np.array(s_2)

  print("The resultant of Vector A and Vector B is equal to:")

  print(); print(np.add(vectorAbar, vectorBbar))


addition()
