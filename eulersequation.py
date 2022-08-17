# Dewil Lucas,22/10/2021
# I was chilling on Youtube and then sudenly I saw a video : https://www.youtube.com/watch?v=IUTGFQpKaPU
# This video was talking about the most beatiful equation in mathematics.
# The mathematician who explained the equation
import math

# Initializing real numbers
x = -1.0
y = 0.0

# converting x and y into complex number
i = complex(x, y)

# Complex numbers involve a lot of calculation with the square root from -1.
# This is also called the number i.
# But, if i is the root from -1, then the square of i will equal -1.

# Pi
PI = math.pi
# making e
E = math.e
calc = E**(PI*i)
calc2 = calc + 1
print(calc2.imag)
# Result should be 0
