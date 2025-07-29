# 🧪 Python Lesson Code Snippets

## 1. 99 Bottles of Beer Program

```python
for i in range(99, 0, -1):
    print(f"{i} bottle{'tests' if i != 1 else ''} of beer on the wall, {i} bottle{'tests' if i != 1 else ''} of beer.")
    print(f"Take one down and pass it around, {i-1 if i > 1 else 'no more'} bottle{'tests' if i-1 != 1 else ''} of beer on the wall.\n")
```

---

## 2. Pass-by-Object Reference

### Immutable example
```python
def update_number(x):
    x += 1
    print("Inside function:", x)

num = 5
update_number(num)
print("Outside function:", num)
```

### Mutable example
```python
def append_item(my_list):
    my_list.append(4)
    print("Inside function:", my_list)

lst = [1, 2, 3]
append_item(lst)
print("Outside function:", lst)
```

---

## 3. Imports and Modules

### Using a built-in module
```python
import math

print(math.sqrt(16))
```

### Custom module (math_utils.py)
```python
# math_utils.py
def add(a, b):
    return a + b

def square(n):
    return n * n
```

### Using the custom module
```python
from math_utils import add, square

print(add(2, 3))
print(square(4))
```

---

## 4. Classes and Objects

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Creating and using objects
my_dog = Dog("Rex", "Labrador")
print(my_dog.bark())
```

---

## 5. Type Hinting

### Function without type hints
```python
def greet(name):
    return "Hello " + name
```

### Function with type hints
```python
def greet(name: str) -> str:
    return "Hello " + name
```

### Variables with type hints
```python
age: int = 25
scores: list[int] = [88, 76, 92]
```

---

## 6. Python `unittest` Module

### Function to test
```python
# calculator.py
def add(a: int, b: int) -> int:
    return a + b
```

### Unit test
```python
# test_calculator.py
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

---

## 7. Take-home Challenge Sample Structure

```python
# models/user.py
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
```

```python
# main.py
from models.user import User

u = User("Alice", 30)
print(u.greet())
```

```python
# test_user.py
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_greet(self):
        user = User("Bob", 25)
        self.assertEqual(user.greet(), "Hi, I'm Bob and I'm 25 years old.")

if __name__ == "__main__":
    unittest.main()
```
