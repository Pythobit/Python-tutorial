from addition import Addition
 
class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from Addition module
 
    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)     # turn subtraction to adding a negative num2
 
    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for x in range(0, num2):
            res = cls.add(res, num1)    # add num1 for num2 times
        return res
 
    @classmethod
    def divide(cls, num1, num2):
        res = 0
        while num1 >= num2:
            num1 = cls.subtract(num1, num2)  # subtract num2 from num1 until its remainder is smaller than num2
            res = cls.add(res, 1)   # count the times of subtraction as the result
        return res
        
