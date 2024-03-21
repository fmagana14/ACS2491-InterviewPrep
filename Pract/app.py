# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]

# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# solution

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            new_add = ""
            div_three = i % 3 == 0. 
            div_five = i % 5 == 0 
            # displays Fizz if divisible by 3
            if div_three:
                new_add += "Fizz"
            # displays Buzz if divisible by 5
            if div_five:
                new_add += "Buzz"
            if not div_three and not div_five:
                new_add += f'{i}'
            answer.append(new_add)
        return answer
         