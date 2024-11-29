time = .1
mass = 1
x_pos = 0
y_pos = 0

y = int(input("What position would you like to drop the ball from"))

while y>0:
    time +=.1
    y -= (y * .1)

print(time)