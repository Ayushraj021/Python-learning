#Creating a dictionary
crew_details={
            "Pilot":"Kumar",
            "Co-Pilot":"Raghav",
            "Head-Strewardess":"Malini",
            "Stewardess":"Mala"
}
print(crew_details["Pilot"])

print("\nIterating the dictionary using items function")
for key,value in crew_details.items():
    print(key,":",value)


#Usually while working with dictionary, you will be interested in specific values. 
#Let’s find the value of all pilots from crew_details.
print("\nIterating the dictionary using keyword 'in'")
for key in crew_details:
    if(key=="Pilot" or key=="Co-Pilot"):
        print(crew_details[key])
#Note: Dictionary being unordered, the order of the values being displayed may vary during each execution of the above for loop.

#Dictionaries are mutable
crew_details["Pilot"]="James" # Here the value for key "Pilot" is being updated to "James"
print("\nAfter modifying the value of Pilot:", crew_details["Pilot"])

print("------------------------------------------------------------------")
print("Before update:")
# Usage of get method()
print("Co-pilot:",crew_details.get("Co-Pilot"))

#Usage of update method()
crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})

print("\nAfter update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
print("Flight Attendant:",crew_details["Flight Attendant"])
