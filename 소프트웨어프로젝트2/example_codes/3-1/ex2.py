# 재귀 알고리즘
upper = int(input("Enter a number: "))
sumval = 0
# 1. for문을 사용한 숫자 더하기
for i in range(1, upper + 1):
    sumval += i
print("Sum of 1 to", upper, "=", sumval)

# 2. 재귀를 이용한 숫자 더하기
def RecursiveSum(n):
    return 1 if n == 1 else RecursiveSum(n - 1) + n
print("Recursive Sum of 1 to", upper, "=", RecursiveSum(upper))

# 3. 배열의 숫자의 합 구하기
data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]

def RecursiveArraySum(nbrs, k):
    if k == 0:
        return nbrs[0]
    return RecursiveArraySum(nbrs, k - 1) + nbrs[k]

print("Recursive Array Sum:", RecursiveArraySum(numbers, len(numbers) - 1))
# len(numbers - 1)에 주의! 길이는 1부터 count하지만 인덱스 값은 0부터 시작하기 때문이다.
