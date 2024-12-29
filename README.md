# Aura Points Tracker - README

## Overview
The Aura Points Tracker is a Python script that gamifies user interactions by assigning and managing "aura points" based on reported events. Points range from -1000 (cringe energy) to 1000 (positive vibes) and are influenced by event descriptions, audience size, and AI-generated roasts.

---

## Features
1. **Aura Points Management**:
   - Tracks aura points for users.
   - Points are clamped between -1000 and 1000.

2. **Custom Rules**:
   - Positive actions like "hitting the gym" or "volunteering" increase points.
   - Negative actions like "procrastinating" or "messy dorm" decrease points.

3. **Savage Roasts**:
   - Integrates OpenAI's GPT-3.5 to deliver humorous and savage feedback for reported events.

4. **Audience Impact**:
   - Points deduction scales with the size of the audience witnessing the event.

5. **Interactive Options**:
   - Report an event and update aura points.
   - View the current aura points for a specific person.

---

## Prerequisites
1. **Python 3.x** installed on your machine.
2. An OpenAI API key. Replace `'YOUR_API_KEY_HERE'` in the script with your API key.

---

## Installation
1. Clone the repository or download the script file.
2. Install required dependencies:
   ```bash
   pip install openai
   ```
3. Replace `'YOUR_API_KEY_HERE'` in the script with your OpenAI API key.

---

## Usage

### 1. Run the Script
Execute the script using Python:
```bash
python aura_tracker.py
```

### 2. Choose an Option
- **Option 1**: Report an event and update aura points.
  - Provide a description of what happened.
  - Enter the name of the person involved.
  - Specify the audience size (number of witnesses).
- **Option 2**: View someone's current aura points by entering their name.

---

## Example Interaction
### Reporting an Event
```plaintext
Options: 
1. Report an event and update aura points
2. View someone's aura points
Choose an option (1 or 2): 1
Describe what happened: Forgot to clean the dorm for a week
Enter the name of the person this happened to: John
How many people witnessed it? 3
Damn, John... -180 points. Bro, that's straight-up cringe. “Forgetting to clean for a week? Bruh, even raccoons have higher standards.”
```

### Viewing Aura Points
```plaintext
Options: 
1. Report an event and update aura points
2. View someone's aura points
Choose an option (1 or 2): 2
Enter the name of the person whose aura points you want to view: John
John's current aura points: -180
```

---

## Features in Detail

### **Positive Vibes**:
Actions like:
- Staying on top of assignments
- Hitting the gym
- Helping a friend

### **Negative Vibes**:
Actions like:
- Procrastinating
- Ignoring group work
- Leaving dishes unwashed

### **Audience Impact**:
Each witness adds a multiplier to the aura points deduction, up to a maximum of 1000.

---

## Limitations
1. **Mock Database**: Currently uses an in-memory dictionary for storing aura points. Replace with a persistent database for production use.
2. **Audience Size**: Large audience sizes can heavily influence deductions, so use realistic numbers.
3. **API Costs**: Using OpenAI's API may incur costs based on usage.

---

## Future Enhancements
- Implement a persistent database.
- Add a web or mobile interface.
- Expand custom rules for more detailed scenarios.
- Enhance feedback with multimedia support (e.g., images or sound bites).

---

## License
This script is provided for personal and educational use. Ensure compliance with OpenAI's API terms of service when using this code.
