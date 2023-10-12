import random

# Function to calculate CGPA based on marks
def calculate_cgpa(marks):
    total_marks = sum(marks)
    cgpa = total_marks / (5 * 10)  # Assuming a maximum of 10 marks per subject
    return cgpa

# Generate random marks for 5 subjects (0 to 100)
marks = [random.randint(0, 100) for _ in range(5)]

# Calculate the CGPA
cgpa = calculate_cgpa(marks)

# Determine the peer group
peer_group = ""
if cgpa > 9:
    peer_group = "Peer 1 (Above 9 CGPA)"
elif cgpa > 8:
    peer_group = "Peer 2 (Above 8 CGPA)"
elif cgpa > 5:
    peer_group = "Peer 3 (Above 5 CGPA)"
else:
    peer_group = "Peer 4 (Lower than 4 CGPA)"

# Display the results
print("Subject Marks:", marks)
print("CGPA:", cgpa)
print("Peer Group:", peer_group)
