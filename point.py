
#hidden constructor

# class Point:
#      def __new__(cls, *args, **kwargs):
#             print("Creating a new Point instance")
#             return super(Point,cls).__new__(cls)

# class Point:
#      def __init__(self,x=0, y=0):
#          self.x= x
#          self.y=y
#          print(f"Point created at ({self.x}, {self.y})")

# hidden constructor end


#Private Functions & Private Attributes


# class Point:

#     def __init__(self, x=0 , y=0):
#         self.__x=x
#         self.__y=y

#     def __private_method(self):
#         print(f"private_method called :({self.__x}, {self.__y})")

#     def display(self):
#         print(f"Point Coordinates: ({self.__x}, {self.__y})")
#         self.__private_method()

        #Private Functions & Private Attributes end


# copy constructor

# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
        
#     def copy(self):
#             return Point(self.x, self.y)
        
#copy constructor end

#Print Object using Built-in Print() & Operator Overloading

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"point({self.x},{self.y})"

#Print Object using Built-in Print() & Operator Overloading end
