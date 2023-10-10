class OwnIterator:
 
  """Class to implement iterator protocol"""
 
  def __init__(self, num=0):
    self.num = num
 
  def __iter__(self):
 
    self.x = 1
 
    return self
 
  def __next__(self):
 
    own_iterator = self.x
 
    self.x += 1
 
    return own_iterator
 
for x in OwnIterator():
 
  if x < 5:
 
    print ("Num is:",x)
 
  else:
 
    break
