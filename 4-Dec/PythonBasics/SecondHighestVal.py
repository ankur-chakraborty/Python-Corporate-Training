def second_highest(numbers):
    highest = second = float('-inf')
    for num in numbers:
        if num > highest:
            second = highest
            highest = num
        elif num > second and num != highest:
            second = num
    return second if second != float('-inf') else None

n = int(input("Enter N: "))
nums = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
print("Second highest:", second_highest(nums))
