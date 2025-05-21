call_counter = 0
def fib(a):
    #======= подсчёт ========
    global call_counter
    call_counter += 1
    print(f"call f({a})")
    #===== код рекурсии ====
    if a < 2: return 1
    else: return fib(a-1) + fib(a-2)

print(fib(11))
print(f"number of function calls {call_counter}")
