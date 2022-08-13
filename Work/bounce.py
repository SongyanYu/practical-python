# bounce.py
#
# Exercise 1.5
bounce = 1
bounce_height = 100.0

while bounce <= 10:
    bounce_height = bounce_height * 3/5
    print(bounce, round(bounce_height, 4))
    bounce = bounce + 1
