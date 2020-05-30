candies = 500
people = 4
output = [0] * people
distributed = 0
next_count = 0
total_iterations = 0
while candies > 0:
    for i in range(people):
        total_iterations = total_iterations + 1
        next_count = next_count + 1
        remaining_candies = candies - next_count
        if remaining_candies <= 0:
            output[i] += candies
            print(output)
            print(total_iterations)
            exit()
            candies = candies - next_count
            output[i] += next_count

print(output)
print(total_iterations)