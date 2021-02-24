class CustomError(TypeError):
    def __init__(self,message,code):
        super().__init__(f'{code}: {message}')
        self.code = code
    
#    def __str__(self):
#        return f'CustomError {self.code}'

def count_from_zero(n:int):
    if not isinstance(n,int):
        raise CustomError("Incorrect type entered",403)
    if n < 0:
        raise ValueError(f"{n} cannot be less than zero")
    for i in range(0,n+1):
        print(i)

count_from_zero(5)
count_from_zero("Flag")


