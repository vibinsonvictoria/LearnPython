
class Executor(object):
    def __init__(self,stop=0):
        self.stop=stop

    def execute(self,fun):
        for i in range(0,self.stop):
            fun()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('stopped')


def print_call():
    print('Hello')


with Executor(10) as executor:
    executor.execute(print_call)


