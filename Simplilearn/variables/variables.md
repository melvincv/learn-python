## Data Types

Type of value stored in a variable.

- integer
- float
- string
- list
- tuple
- file pointers

## Code

### Integer

```
x=100
type(x)
int
```
```
x=245+60
type(x)
int

print(x)
```

### Float

```
x=3.14
type(x)
float
print(x)
3.14
```

### String

Collection of characters. Enclose them within single or double quotes.

```
x= "Simpllearn"
x= 'Simpllearn'
print(x)
Simpllearn
type(x)
str
```

### List

Assign multiple values to a variable.

```
x= [14,57,9]
print(x)

type(x)
list
```

Each value in a list has an index that starts from 0.
Here, value of 0 is 14.

```
print(x[0])
14
```

#### Change a value in a list

```
x[2]=22
```

### Tuple

Multiple values n a single variable.
Tuples are immutable - cannot change the values in a tuple.


### File Pointers

Assign the name of a file to a variable.

```
x=open('variable.ipynb','r')
type(x)
```

- Assign Values to Multiple variables in one line

```
(x,y,z)=5,10,7

print(x)
print(y)
print(z)
```

- Assign the same value to multiple variables in one line

```
x=y=z=1
print(x,y,z)
```

## Rules for naming variables

1. Variable name must begin with an alphabet or underscore.
2. The first character can be followed by alphabets, numbers or underscore.
3. Variable names are case sensitive.
4. Reserved words canoot be used as variable names. (break, class, try, continue)

## Arithmetic Operations

```
x=20
y=10

result= x+y
print(result)

result= x-y
result= x*y
result= x/y
```

This will give the result in float type. To make it integer type:

```
result= x//y
print(result)
```

Modulus operator gives the remainder after division:
x mod y

```
result= x%y
print(result)
```

## String Operations

Every character in a string value has an index, which starts at 0

```
var= "Simplilearn"
print(var[0])
S
```

- Print multiple characters. Here the last index is ignored, so we need to give one higher index.

```
print(var[0:3])
Sim
```

- Start from the first character

```
print(var[:3])
Sim
```

- End with the last character

```
print(var[5:])
ilearn

print(var[0:20])
```

- This works and prints the entire string, even though the string does not contain 21 characters.

- Print the length of a string

```
len(var)
11
```