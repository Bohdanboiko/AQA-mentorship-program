num_fib = int(input("Скільки чисел потрібно "))

fib_nums = [1, 1]


for i in range(2, num_fib):
    next_num = fib_nums[i - 1] + fib_nums[i - 2]
    fib_nums.append(next_num)


print("Перше число", num_fib, fib_nums)
