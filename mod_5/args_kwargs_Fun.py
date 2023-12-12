"""
* и ** в def используются для создания функций-оберток,
которые передают аргументы другой функции и возвращают
возвращаемое значение этой функции

Функция print_title() (здесь является оберткой для встроенной функции print())
использует синтаксис * для получения переменного количества позиционных аргументов в кортеже,
присвоенном параметру args,
синтаксис ** присваивает все ключевые аргументы словарю из параметра kwargs"""
  
def print_title(*args, **kwargs):
    '''обертка переводит строковые аргументы в регистр Title
    '''
    args = list(args)
    for i, value in enumerate(args):
        args[i] = str(value).title()
    return print(*args, **kwargs)
  

 
name = 'ivan'
print_title('Hello,', name) # hello, Ivan
print_title('dog', 'cat', 'moose', sep=', ') # Dog, Cat, Moose
