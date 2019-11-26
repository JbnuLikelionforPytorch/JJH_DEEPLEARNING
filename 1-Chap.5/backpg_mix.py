class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def foward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout):
        dx = self.y * dout
        dy = self.x * dout

        return dx, dy


class AddLayer:
    def __init__(self):
        pass

    def foward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = dout
        dy = dout

        return dx, dy


apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_price_layer = AddLayer()
mul_tax_layer = MulLayer()

# 순전파
apple_price = mul_apple_layer.foward(apple_num, apple)
orange_price = mul_orange_layer.foward(orange, orange_num)
fruit_price = add_price_layer.foward(apple_price, orange_price)
add_tax = mul_tax_layer.foward(fruit_price, tax)

# 역전파
dout = 1
dfruit_price, dtax = mul_tax_layer.backward(dout)
dapple_price, dorange_price = add_price_layer.backward(dfruit_price)
dapple_num, dapple = mul_apple_layer.backward(dapple_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)

print(add_tax)
print(dapple_num, dapple, dorange, dorange_num, dtax)
