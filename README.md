
# **Polygon Area Calculator**

# Original Git Repo 
 https://github.com/freeCodeCamp/boilerplate-polygon-area-calculator

# My git repo
https://github.com/SpinFabio/py_exe_04-polygon_area


# Original Assignement: 


#### **Rectangle class** 
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

* __set_width__
* __set_height__
* __get_area__: Returns area (width * height)
* __get_perimeter__: Returns perimeter (2 * width + 2 * height)
* __get_diagonal__: Returns diagonal ((width ** 2 + height ** 2) ** .5)
* __get_picture__: Returns a string that represents the shape using lines of "\*". The number of lines should be equal to the height and the number of "\*" in each line should be equal to the width.
    *  There should be a new line (\n) at the end of each line.
    * If the <u>width or height is larger than 50</u>, this should return the string: "Too big for picture.".
* __get_amount_inside__: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
    * Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

---

#### __Square class__
The Square class should be a __subclass of Rectangle__. When a Square object is created: 
* a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: Square(side=9)

Additionally, the set_width and set_height methods on the Square class should set both the width and height.

Usage example
~~~
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
~~~

That code should return:
~~~
50
26
Rectangle(width=10, height=3)
**********
**********
**********


81
5.656854249492381
Square(side=4)
****
****
****
****
~~~

