data = [
    [0, 0],
    [1, 2],
    [2, 4],
    [4, 8],
    [8, 16]
]

x = 5
h = 0.01
rate = 0.01
def cost(param):
    error = 0
    for i in data:
        actual = i[0]*param
        expected = i[1]
        error += (actual-expected)**2
    return error/len(data)

for i in range(40):
    dcost = (cost(x + h) - cost(x))/h
    x -= rate*dcost

def predict(input):
    model = input*x
    return model

print(predict(100))