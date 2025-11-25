# Demonstration ONLY — not functional code

user_input = "example' OR '1'='1"

# Vulnerable pattern: direct string concatenation
query = "SELECT * FROM users WHERE username = '" + user_input + "';"

print("This is what a vulnerable SQL query looks like:")
print(query)
