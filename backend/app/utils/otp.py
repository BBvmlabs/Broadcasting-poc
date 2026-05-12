import random
import asyncio
from datetime import datetime, timedelta
import pytz

# Simulating the stored OTP data
otp_cache = {}

# Function to generate OTP
async def generate_otp(email: str) -> dict:
    """
    Generate and send an OTP via email.
    """
    otp_code = random.randint(100000, 999999)
    otp_id = f"{email}-{random.randint(1000, 9999)}"  # Generate a unique OTP ID

    expires_at = datetime.now(pytz.utc) + timedelta(minutes=10)

    otp_cache[email] = {"code": otp_code, "expires_at": expires_at}

    # await send_email(email, "Your OTP Code", f"Your Mail id: {email} \n Your OTP is: {otp_code}")

    # print(f"\n[DEBUG] OTP generated for {email}: {otp_cache[email]}\n")

    return {"otp_id": otp_id, "otp_code": otp_code}

async def verify_otp(email: str, otp_code: str) -> bool:
    """
    Verify the OTP using cache or database.
    """
    otp_details = otp_cache.get(email)  # Lookup by email
    if not otp_details:
        print(f"[DEBUG] OTP not found for {email}")
        return False

    print(f"[DEBUG] OTP details for {email}: {otp_details}")

    if otp_details["code"] != int(otp_code):  # Ensure OTP code is an integer
        print(f"[DEBUG] OTP code does not match for {email}. Expected: {otp_details['code']}, Provided: {otp_code}")
        return False

    current_time = datetime.now(pytz.utc)
    print(f"[DEBUG] Current time: {current_time}")
    print(f"[DEBUG] OTP expiration time: {otp_details['expires_at']}")

    if otp_details["expires_at"] < current_time:
        print(f"[DEBUG] OTP expired for {email}. Expiration time: {otp_details['expires_at']}, Current time: {current_time}")
        return False

    print(f"[DEBUG] OTP verified successfully for {email}")
    return True

# # Function to test OTP generation and verification for 10 emails
# async def test_multiple_emails():
#     emails = [
#         "testuser1@example.com",
#         "testuser2@example.com",
#         "testuser3@example.com",
#         "testuser4@example.com",
#         "testuser5@example.com",
#         "testuser6@example.com",
#         "testuser7@example.com",
#         "testuser8@example.com",
#         "testuser9@example.com",
#         "testuser10@example.com"
#     ]
    
#     # Generate OTPs for all emails
#     otp_results = {}
#     for email in emails:
#         otp_results[email] = await generate_otp(email)

#     # Shuffle the email list to verify OTPs in random order
#     shuffled_emails = random.sample(emails, len(emails))
    
#     # Verify OTP for emails in shuffled order
#     for email in shuffled_emails:
#         otp_code = otp_results[email]["otp_code"]
#         print(f"Verifying OTP for {email} with correct OTP:")
#         verification_result = await verify_otp(email, otp_code)
#         print(f"Verification with correct OTP for {email}: {'Success' if verification_result else 'Failed'}")
        
#         # Now, test verification with an incorrect OTP
#         incorrect_otp = random.randint(100000, 999999)
#         print(f"Verifying OTP for {email} with incorrect OTP:")
#         verification_result = await verify_otp(email, incorrect_otp)
#         print(f"Verification with incorrect OTP for {email}: {'Success' if verification_result else 'Failed'}")

# # Run the test
# if __name__ == "__main__":
#     asyncio.run(test_multiple_emails())
