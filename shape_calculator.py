from typing import Self


class Rectangle:
  def __init__(self,width:int, height:int):
    self.set_width(width)
    self.set_height(height)

  def set_width(self, width):
    if width < 0:
      raise Exception("width must be positive")
    self.width=width
    
  def set_height(self,height):
    if height < 0:
      raise Exception("height must be positive")
    self.height=height

  def get_area(self):
    return self.height*self.width

  def get_perimeter(self):
    return (self.height)*2+(self.width)*2

  def get_diagonal(self):
    return (self.width**2+self.height**2)**0.5

  def get_picture(self):
    out_str:str=""
    fill=" *"

    for i in range(0,self.height):
      out_str=out_str+fill*(self.width)+"\n"
    return out_str

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  def __init__(self, side:int):
    super().__init__(side,side)

  def set_side(self,side:int):
    super().set_height(side)
    super().set_width(side)
  
  pass