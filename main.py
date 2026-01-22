def step(x):
    return 1 if x>0 else 0  ##this is a step function.

def perceptron(x1, x2, w1, w2, b): ##This is how one single neuron will work.
    y = x1*w1 + x2*w2 + b
    return step(y) #here step is called activation function. 

print(perceptron(0,0,1,1,-1.5))
print(perceptron(0,1,1,1,-1.5))
print(perceptron(1,0,1,1,-1.5))
print(perceptron(1,1,1,1,-1.5))