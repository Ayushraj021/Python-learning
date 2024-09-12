import os

def list_files_and_sizes(directory):
    """List files and their sizes from a directory."""
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if it's a file
        if os.path.isfile(filepath):
            # Get the size of the file
            size = os.path.getsize(filepath)
            # Print filename and size
            print(f"File: {filename}, Size: {size} bytes")

# Example usage
directory_path = "E:\Abhinav"
list_files_and_sizes(directory_path)
