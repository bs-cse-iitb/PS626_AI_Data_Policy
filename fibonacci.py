# exponential time complexity
def fibonacci1(n):
    if n <= 1:
        return 1   
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n, intermediate_dict={}):
    #print(intermediate_dict)
    if n <= 1:
        return 1 #n if start with zero
    if n not in intermediate_dict:
        intermediate_dict[n] = fibonacci(n-1, intermediate_dict) + fibonacci(n-2,intermediate_dict)
    return intermediate_dict[n]

no_of_elements = 50
# generally fibonacci number start with 0 1 1 2, but in questions it start with 1 1 2  
print("Fibonacci series:")
for i in range(no_of_elements):
    print("Element",i+1,"--------------",fibonacci(i))