def solution(numbers):
    
    a = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in range(10):
        numbers = numbers.replace(a[i], b[i])
        
    return int(numbers)