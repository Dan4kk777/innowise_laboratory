from dotenv import load_dotenv
import os

class InputValidator:

    @staticmethod
    def validate_year(year_str: str, CURRENT_YEAR: int) -> int:

        load_dotenv()
        MIN_YEAR = int(os.getenv('MIN_YEAR'))

        if not year_str.isdigit():
            raise ValueError(F"Invalid input. Please enter a numeric year ({MIN_YEAR} or more).")
        
        year = int(year_str)
        if not (MIN_YEAR <= year <= CURRENT_YEAR):
            raise ValueError(f"Please enter a valid year between 1925 and {CURRENT_YEAR}.")
        return year

    @staticmethod
    def validate_name(name: str) -> str:
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        return name.strip()