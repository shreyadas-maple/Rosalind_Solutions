

def FibonacciNumber(termIndex):
   if (termIndex == 0):
      return 0
   elif (termIndex == 1):
      return 1
   else:
      return FibonacciNumber(termIndex - 1) + FibonacciNumber(termIndex - 2)

print(FibonacciNumber(8))
