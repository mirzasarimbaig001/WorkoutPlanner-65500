def calculate_bmi(weight, height_cm):
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

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
    if bmi < 25:
        return "Home"
    else:
        return "Gym"

def main():
    print("Welcome to the Workout Time Planner!")
    try:
        weight_input = input("Enter your weight in kg: ").strip()
        height_input = input("Enter your height in cm: ").strip()
        
        if not weight_input or not height_input:
            raise ValueError("Weight and height cannot be empty.")
        
        weight = float(weight_input)
        height = float(height_input)
        
        bmi = calculate_bmi(weight, height)
        category, plan = get_plan(bmi)
        place = gym_or_home(bmi)
        
        print(f"\nYour BMI is: {bmi} ({category})")
        print(f"Recommended daily workout:\n{plan}")
        print(f"Recommended workout location: {place}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
