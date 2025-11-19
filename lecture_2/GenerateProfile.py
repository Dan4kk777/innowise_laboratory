from dotenv import load_dotenv
import os

def generate_profile(age: int) -> str:

    load_dotenv()
    ZERO = int(os.getenv('ZERO'))
    THRESHOLD_CHILD = int(os.getenv('THRESHOLD_CHILD'))
    THRESHOLD_TEENAGER = int(os.getenv('THRESHOLD_TEENAGER'))

    if age < ZERO:
        raise ValueError("Age cannot be negative.")
    elif ZERO <= age <= THRESHOLD_CHILD:
        return "Child"
    elif THRESHOLD_CHILD < age <= THRESHOLD_TEENAGER:
        return "Teenager"
    else:
        return "Adult"
