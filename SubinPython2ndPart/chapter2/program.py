import fibo
import trial

x = int(input("Fib of? "))

n = fibo.find_fibo(x)

print("\nThe {} fibonacci number is {}\n".format(str(x)+"th",n))


# print("Hello, I am inside program.py")
# print(trial.__name__)