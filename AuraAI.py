import openai
import random

# Initialize the OpenAI API key
openai.api_key = 'YOUR_API_KEY_HERE'

# Aura points database (can be replaced with a real database in the future)
aura_database = {}

# Function to get the current aura points for a user
def get_aura_points(name):
    return aura_database.get(name.lower(), 0)  # Lowercase to handle case-insensitivity

# Function to update the aura points for a user
def update_aura_points(name, points):
    current_points = get_aura_points(name)
    new_points = current_points + points
    # Ensure the points stay within the -1000 to 1000 range
    aura_database[name.lower()] = max(min(new_points, 1000), -1000)

# Function to apply custom aura rules based on the description
def apply_custom_aura_rules(user_input):
    positive_vibes = ["staying on top of assignments", "mewing", "gym regularly", "acing a test",
                      "internship", "job offer", "helping a friend", "meal prep", "volunteering", 
                      "clean dorm", "networking", "hydrated"]
    negative_vibes = ["procrastinating", "skipping class", "messy dorm", "unwashed clothes", 
                      "ignoring group work", "unprepared", "late assignments", "complaining"]

    # Bias towards aura point deduction
    if any(word in user_input.lower() for word in negative_vibes):
        return random.randint(-150, -100), "Bro, that's straight-up cringe."
    elif any(word in user_input.lower() for word in positive_vibes):
        return random.randint(0, 50), "Alright, you might get a pass here."

    # Default to random deduction if no specific rule applies
    return random.randint(-200, -50), "Yeah, this is mid at best."

# Function to generate aura points based on user input and audience size
def generate_aura_points_with_audience(user_input, audience_size, person_name):
    try:
        base_score, custom_message = apply_custom_aura_rules(user_input)
        prompt = f"Roast this situation: '{user_input}'. Be savage and roast it hard."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a savage AI that loves to roast people hard."},
                {"role": "user", "content": prompt}
            ]
        )
        ai_response = response['choices'][0]['message']['content'].strip()
        aura_score = base_score - min(audience_size * 10, 1000) if base_score < 0 else base_score
        update_aura_points(person_name, aura_score)

        if aura_score > 0:
            feedback = f"{person_name}, you barely scraped by with {aura_score} points. {custom_message} {ai_response}"
        else:
            feedback = f"Damn, {person_name}... -{abs(aura_score)} points. {custom_message} {ai_response}"
        return feedback, aura_score
    except Exception as e:
        return f"Error: {e}", 0

def analyze_user_input_with_audience_and_person(user_input, audience_size, person_name):
    feedback, score = generate_aura_points_with_audience(user_input, audience_size, person_name)
    return feedback, score

def view_aura_points(name):
    aura_points = get_aura_points(name)
    return f"{name.capitalize()}'s current aura points: {aura_points}"

# Test the system
if __name__ == "__main__":
    while True:
        print("Options: ")
        print("1. Report an event and update aura points")
        print("2. View someone's aura points")
        choice = input("Choose an option (1 or 2): ")

        if choice == "1":
            user_input = input("Describe what happened: ")
            person_name = input("Enter the name of the person this happened to: ")
            audience_size = int(input("How many people witnessed it? "))
            feedback, score = analyze_user_input_with_audience_and_person(user_input, audience_size, person_name)
            print(feedback)
        elif choice == "2":
            person_name = input("Enter the name of the person whose aura points you want to view: ")
            print(view_aura_points(person_name))
        else:
            print("Invalid option. Please choose 1 or 2.")

