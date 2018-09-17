from base import A
class B(A):
  def __init__(self, x, y, a):
    A.__init__(self,5,6)
    self.a = a
  
  def override1(self):
    print("from B")
    print(self.a)
    print(self.x)
    print(self.y)