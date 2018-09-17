from base import A

class C(A):

  def __init__(self, x, y, z):
    A.__init__(self,7,8)
    self.z = z
  def override2(self):
    print("from C")
    print(self.x)
    print(self.y)
    print(self.z)