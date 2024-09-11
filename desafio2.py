def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    
   
    while fib_sequence[-1] < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

def check_fibonacci(num):
    fib_sequence = fibonacci_sequence(num)
    
    
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

def main():
    while True:
        try:
            numero = int(input("Informe um número (ou digite 'sair' para encerrar): "))
            resultado = check_fibonacci(numero)
            print(resultado)
        except ValueError:
            print("Saindo do programa. Até mais!")
            break

main()
