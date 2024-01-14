import turtle
daire_yaricap = 10
yatay_mesafe = 10
turtle.setup(width=1000, height=1000)
turtle.speed(10)
# l harfini çizelim
# Dikey daireleri çizelim
for i in range(8):
    turtle.penup()
    turtle.goto(-450, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# Yatay daireleri çizelim
for i in range(5):
    turtle.penup()
    turtle.goto(-450 + 10*i, -7 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
#U harfini çizelim
# Dikey daireleri çizelim
for i in range(8):
    turtle.penup()
    turtle.goto(-350, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# Yatay daireleri çizelim
for i in range(5):
    turtle.penup()
    turtle.goto(-350 + 10*i, -7 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(8):
    turtle.penup()
    turtle.goto(-300, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(1):
    turtle.penup()
    turtle.goto(-350, 35)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(1):
    turtle.penup()
    turtle.goto(-300, 35)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# T harfini çizelim
# Dikey daireleri çizelim
for i in range(8):
    turtle.penup()
    turtle.goto(-200, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# Yatay daireleri çizelim
for i in range(5):
    turtle.penup()
    turtle.goto(-200 + 10*i, 0 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(5):
    turtle.penup()
    turtle.goto(-200 - 10*i, 0 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# F harfini çizelim
# Dikey daireleri çizelim
for i in range(8):
    turtle.penup()
    turtle.goto(-100, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# Yatay daireleri çizelim
for i in range(5):
    turtle.penup()
    turtle.goto(-100 + 10*i, 0 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(5):
    turtle.penup()
    turtle.goto(-100 + 10*i, -3.5 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# U harfini çizelim
# Dikey daireleri çizelim
for i in range(8):
    turtle.penup()
    turtle.goto(0, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
# Yatay daireleri çizelim
for i in range(5):
    turtle.penup()
    turtle.goto(0 + 10*i, -7 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(8):
    turtle.penup()
    turtle.goto(50, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(1):
    turtle.penup()
    turtle.goto(0, 35)
    turtle.pendown()
    turtle.circle(daire_yaricap)
for i in range(1):
    turtle.penup()
    turtle.goto(50, 35)
    turtle.pendown()
    turtle.circle(daire_yaricap)
turtle.done()