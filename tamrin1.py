# tamrin1.py

# دریافت سن از کاربر
age_years = int(input("سن خود را به سال وارد کنید: "))

# تبدیل به واحدهای مختلف
age_days = age_years * 365
age_hours = age_days * 24
age_minutes = age_hours * 60
age_seconds = age_minutes * 60

# نمایش خروجی
print(f"سن شما به ساعت: {age_hours:,}")
print(f"سن شما به دقیقه: {age_minutes:,}")
print(f"سن شما به ثانیه: {age_seconds:,}")
