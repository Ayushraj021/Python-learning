# Global variables
child_ids = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    # Calculate and return the total number of chocolates
    return sum(chocolates_received)

def reward_child(child_id_rewarded, extra_chocolates):
    # Check if extra chocolates is less than 1
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return
    
    # Check if child_id_rewarded is valid
    if child_id_rewarded not in child_ids:
        print("Child id is invalid")
        return
    
    # Find the index of the child_id_rewarded
    index = child_ids.index(child_id_rewarded)
    
    # Add extra chocolates to the specified child
    chocolates_received[index] += extra_chocolates
    
    # Print the updated list of chocolates
    print(chocolates_received)

# Test the functions
print(calculate_total_chocolates())

# Test the reward_child function
reward_child(20, 2)  # Valid test case

# Additional test cases
reward_child(30, 0)  # Extra chocolates is less than 1
reward_child(99, 5)  # Child id is invalid
