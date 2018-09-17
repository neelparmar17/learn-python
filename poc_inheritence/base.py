class A:
  def __init__(self, x,y):
    self.x = x
    self.y = y

  def run(self):
    print("base")
    print(self.x)
    print(self.y)
    self.override1()
    self.override2()
    self.override3()

  def override1(self):
    pass

  def override2(self):
    pass

  def override3(self):
    pass