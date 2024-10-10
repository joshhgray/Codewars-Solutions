def solution(number):
    return sum([num for num in range(number) if num % 5 == 0 or num % 3 == 0])  
