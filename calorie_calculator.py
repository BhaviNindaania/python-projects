# calorie_calculator.py
# Calorie Needs Calculator (Harris-Benedict)
# Handles bad inputs and re-prompts the user.

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt).strip())
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Please enter a number between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid whole number.")

def input_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = float(input(prompt).strip())
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Please enter a number between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number (e.g. 70 or 70.5).")

def input_gender(prompt):
    while True:
        g = input(prompt).strip().lower()
        if g in ('m', 'male'):
            return 'male'
        if g in ('f', 'female'):
            return 'female'
        print("Please enter 'male' or 'female' (or 'm' / 'f').")

def calculate_bmr(gender, weight_kg, height_cm, age_years):
    if gender == 'male':
        return 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age_years)
    else:
        return 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age_years)

def activity_factor_menu():
    print("\nActivity level (choose number):")
    print("1 - Sedentary (little or no exercise)")
    print("2 - Lightly active (light exercise 1-3 days/week)")
    print("3 - Moderately active (moderate exercise 3-5 days/week)")
    print("4 - Very active (hard exercise 6-7 days/week)")
    print("5 - Extra active (very hard exercise / physical job)")
    return input_int("Enter activity level (1-5): ", 1, 5)

def main():
    print("\n🔥 Calorie Needs Calculator (Harris-Benedict) 🔥\n")
    age = input_int("Enter your age (years): ", min_val=5, max_val=120)
    gender = input_gender("Enter your gender (male/female or m/f): ")
    weight = input_float("Enter your weight (kg): ", min_val=10, max_val=500)
    height = input_float("Enter your height (cm): ", min_val=50, max_val=300)
    activity_level = activity_factor_menu()

    bmr = calculate_bmr(gender, weight, height, age)
    factors = {1:1.2, 2:1.375, 3:1.55, 4:1.725, 5:1.9}
    daily_cal = bmr * factors[activity_level]

    print("\n--- Results ---")
    print(f"Your BMR (Basal Metabolic Rate) is: {bmr:.0f} kcal/day")
    print(f"Estimated daily calories for current activity: {daily_cal:.0f} kcal/day")

    # Simple recommendation (customize thresholds if you like)
    if daily_cal < 1800:
        print("Recommendation: You may need more daily calories for energy—consult a nutrition guide.")
    elif 1800 <= daily_cal <= 2500:
        print("Recommendation: Maintain your current balanced diet.")
    else:
        print("Recommendation: High energy needs — ensure sufficient nutrition and match with exercise.")
    print("----------------\n")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
