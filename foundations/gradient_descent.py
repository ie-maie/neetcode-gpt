class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations==0 : return init
        x=init
        for i in range (0,   iterations):
            fx= 2*x
            x= x - learning_rate*fx
                
        x = round(x,5)
        return x
