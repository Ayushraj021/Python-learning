def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # Initialize a dictionary to count visits for each specialty code
    visit_count = {code: 0 for code in medical_speciality}

    # Iterate over the list and count visits for each specialty code
    for i in range(1, len(patient_medical_speciality_list), 2):
        specialty_code = patient_medical_speciality_list[i]
        if specialty_code in visit_count:
            visit_count[specialty_code] += 1

    # Find the specialty code with the maximum number of visits
    max_visits_code = max(visit_count, key=visit_count.get)
    
    # Return the name of the specialty with the maximum visits
    return medical_speciality[max_visits_code]

# Test the function with different values
patient_medical_speciality_list = [301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)  # Expected Output: Pediatrics

# Additional test cases
print(max_visited_speciality([101, 'O', 102, 'O', 302, 'P', 305, 'E', 401, 'O', 656, 'O'], medical_speciality))  # Expected Output: Orthopedics
print(max_visited_speciality([101, 'O', 102, 'E', 302, 'P', 305, 'P', 401, 'E', 656, 'O', 987, 'E'], medical_speciality))  # Expected Output: ENT
