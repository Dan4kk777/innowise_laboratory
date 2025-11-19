from InputValidator import InputValidator
from GenerateProfile import generate_profile
from Print import print_summary
from typing import List, Dict, Union
from dotenv import load_dotenv
import os



def profile_builder():
    
    load_dotenv()
    CURRENT_YEAR = int(os.getenv('CURRENT_YEAR'))
    STOP_WORD = os.getenv('STOP_WORD')
    MIN_YEAR = int(os.getenv('MIN_YEAR'))
    ZERO = int(os.getenv('ZERO'))

    # 2. Get User Input 
    user_name: str = ""
    while not user_name:
        try:
            raw_input = input("Welcome!\n Enter your full name: ")
            user_name = InputValidator.validate_name(raw_input)
        except ValueError as e:
            print(e)

    
    birth_year: int = ZERO
    BOOLEAN = True
    
    while BOOLEAN:
        try:
            birth_year_str = input("Enter your birth year: ")
            birth_year = InputValidator.validate_year(birth_year_str, CURRENT_YEAR)
            BOOLEAN = False
        except ValueError as e:
            print(e)

    BOOLEAN = True
    current_age = CURRENT_YEAR - birth_year

    # 3. Gather Hobbies
    hobbies: List[str] = []
    
    while BOOLEAN:
        hobby_input = input(f"Enter a favorite hobby or type '{STOP_WORD}' to finish: ").strip()
        if hobby_input.lower() == STOP_WORD:
            BOOLEAN = False
            continue
        if hobby_input:
            hobbies.append(hobby_input)

    # 3. Process Profile 
    life_stage = generate_profile(current_age)

    user_profile: Dict[str, Union[str, int, List[str]]] = {
        "name": user_name,
        "age": current_age,
        "life_stage": life_stage,
        "hobbies": hobbies
    }

    # 4. Display Output
    print_summary(user_profile)