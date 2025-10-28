# tamrin3.py

number = int(input("یک عدد دو رقمی وارد کنید: "))

# جدا کردن ارقام
tens = number // 10
ones = number % 10

# محاسبه توان‌ها
result1 = tens ** ones
result2 = ones ** tens

print(f"{tens} به توان {ones} = {result1}")
print(f"{ones} به توان {tens} = {result2}")
