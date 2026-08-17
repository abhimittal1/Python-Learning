"""
Array is a data structure that stores a fixed number of values of the same type. It is a collection of elements identified by index, where each element can be accessed directly using its index. Arrays are commonly used in programming to store and manipulate data efficiently.

Types of Arrays : 
Static Arrays: These arrays have a fixed size that is determined at the time of declaration. Once the size is set, it cannot be changed. They are typically implemented using contiguous memory allocation.

Dynamic Arrays: These arrays can grow or shrink in size during runtime. They are implemented using a dynamic memory allocation technique, where the array is resized as needed. Dynamic arrays provide more flexibility compared to static arrays.

How is Array in Python different from other programming languages?
In Python, arrays are implemented as lists, which are dynamic and can hold elements of different types. Python lists are more flexible than traditional arrays in other programming languages, as they can grow and shrink in size, and they can contain elements of different types. However, if you need a more efficient array-like structure that can hold only elements of the same type, you can use the 'array' module in Python, which provides a more compact and efficient way to store homogeneous data.

Note :- In Python we have only the Dynamic Array, which is implemented as a list. The 'array' module provides a more efficient way to store homogeneous data, but it is not commonly used in everyday programming.

Working of Array in Python how it is handling the Size and Memory Allocation?
In Python, lists (which are dynamic arrays) handle size and memory allocation automatically. When you create a list, Python allocates a certain amount of memory for it. As you add elements to the list, Python may need to resize the list to accommodate the new elements. When resizing occurs, Python typically allocates a new block of memory that is larger than the current size of the list (often doubling the size), copies the existing elements to the new block, and then adds the new element. This process allows lists to grow dynamically while maintaining efficient memory usage.

"""