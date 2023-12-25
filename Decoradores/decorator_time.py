from time import time as __time

def count_elapsed_time(f):
    """
        Decorator.
        Execute the function and calculate the elapsed time.
        Print the result to the standard output.

        How to use:

        @count_elapsed_time
        def foo():
            pass
    """
    def wrapper(*args, **kwargs):
        # Start counting.
        start_time = __time()
        ret = f(*args, **kwargs)
        elapsed_time = __time() - start_time
        print('Elapsed time: %0.10f seconds' % elapsed_time)
        return ret
    
@count_elapsed_time
def contar(a):
    j = 0
    for i in range(1,a):
        if i % 2 == 0:
            j+=1
    return j

if __name__ == '__main__':
    contar(100)

