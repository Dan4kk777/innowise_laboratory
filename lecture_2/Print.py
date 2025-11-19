def print_summary(profile: dict):
    
    print("\n" + "---")
    print("Profile Summary:")
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Life Stage: {profile['life_stage']}")

    if not profile['hobbies']:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(profile['hobbies'])}):")
        for hobby in profile['hobbies']:
            print(f"- {hobby}")
    print("---")