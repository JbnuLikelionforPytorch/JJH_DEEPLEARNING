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


apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

apple_price = mul_apple_layer.foward(apple, apple_num)
total_price = mul_tax_layer.foward(apple_price, tax)

print(total_price)

# backpropagation
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num, dtax)
