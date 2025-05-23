def calculate_bmi(weight, height_cm):
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def get_plan(bmi):
    if bmi < 18.5:
        return "Underweight", "30 mins light exercise\nHigh-protein diet"
    elif bmi < 25:
        return "Normal", "45 mins moderate workout\nBalanced diet"
    elif bmi < 30:
        return "Overweight", "60 mins cardio\nLow-carb diet"
    else:
        return "Obese", "75 mins cardio + strength\nCalorie deficit diet"

def gym_or_home(bmi):
    return "Home" if bmi < 25 else "Gym"

def main():
    try:
        weight = float(input("Weight (kg): "))
        height = float(input("Height (cm): "))
        bmi = calculate_bmi(weight, height)
        category, plan = get_plan(bmi)
        place = gym_or_home(bmi)
        print(f"\nBMI: {bmi} ({category})\n{plan}\nWorkout Location: {place}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
