
import random
import string


def generate_otp(length=6):
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for i in range(length))
    return otp


def send_otp_via_email(email, otp):
    print(f"Sending OTP {otp} to {email}...")


def verify_otp(entered_otp, generated_otp):
    return entered_otp == generated_otp

if __name__ == "__main__":
    
    user_email = 'cbmokshagna@gmail.com'

    
    otp = generate_otp()

    
    send_otp_via_email(user_email, otp)

    
    entered_otp = input("Enter the OTP you received: ")

    
    if verify_otp(entered_otp, otp):
        print("OTP verification successful!")
    else:
        print("OTP verification failed!")
