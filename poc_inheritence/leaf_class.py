from sub_class1 import B
from sub_class2 import C

class D(B, C):
  def __init__(self, x, y, a, z):
    C.__init__(self,x,y,z)
    B.__init__(self,x,y,a)
    
  
  def override3(self):
    print("from D")
    print(self.x)
    print(self.y)