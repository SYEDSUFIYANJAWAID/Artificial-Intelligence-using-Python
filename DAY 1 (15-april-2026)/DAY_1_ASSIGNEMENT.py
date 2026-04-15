# User se 5 inputs lo:
# Name (string)
# Age (should be int)
# Salary (should be float)
# Experience in years (int)
# City (string)

# Conditions:
# Step 1: Validation 
# Agar age, salary, experience wrong datatype ho → "Invalid Input"
# Agar:
# age ≤ 0 OR age > 100
# salary < 0
# experience < 0
# "Invalid Data"

# Step 2: Eligibility Logic

# Agar sab valid ho to:
# Rule 1:
# age < 18 → "Not Eligible"
# Rule 2:
# age ≥ 18 AND experience < 1 → "Fresher"
# Rule 3:
# experience ≥ 1:
# salary ≥ 100000 → "Senior Level"
# salary ≥ 50000 → "Mid Level"
# otherwise → "Junior Level"


