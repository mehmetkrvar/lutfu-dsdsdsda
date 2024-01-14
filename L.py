import turtle

# L harfini çizmek için gerekli değişkenleri tanımlayalım
daire_yaricap = 10
yatay_mesafe = 10

# Turtle modülünü başlatalım
turtle.setup(width=600, height=400)

# Dikey daireleri çizelim
for i in range(8):
    turtle.penup()
    turtle.goto(0, -i * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)

# Yatay daireleri çizelim
for i in range(5):
    turtle.penup()
    turtle.goto(i * yatay_mesafe, -7 * yatay_mesafe)
    turtle.pendown()
    turtle.circle(daire_yaricap)


# Turtle modülünü kapatalım
turtle.done()
