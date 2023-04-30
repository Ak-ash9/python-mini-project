import random
def generate_otp():
    """Generates a 6-digit OTP"""
    digits = "0123456789"
    otp = ""
    for i in range(6):
        otp += random.choice(digits)
    return otp
otp = generate_otp()
print(f"6-digit OTP: {otp}")