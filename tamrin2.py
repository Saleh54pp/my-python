# tamrin2.py

number = int(input("یک عدد دو رقمی وارد کنید: "))

# جدا کردن ارقام
tens = number // 10
ones = number % 10

# ساخت مقلوب
reverse = ones * 10 + tens

print(f"مقلوب عدد {number} برابر است با {reverse}")
