import json
import sys
import random
import string
import os

def generate_random_string(length=10):
    """Generates a random alphanumeric string of a specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def calculate_required_pairs(target_size_bytes, avg_pair_size=30):
    """Calculates the approximate number of pairs needed to reach the target file size."""
    return target_size_bytes // avg_pair_size

def write_json_to_size(megabytes, filename="generated_file.json"):
    # Convert target size to bytes (1 MB = 1,048,576 bytes)
    target_size = megabytes * 1024 * 1024
    
    # Average size estimation for each key-value pair
    avg_key_length = 8
    avg_value_length = 100
    avg_pair_size = avg_key_length + avg_value_length + 10  # Extra for JSON formatting
    
    # Estimate number of pairs required
    required_pairs = calculate_required_pairs(target_size, avg_pair_size)
    
    # Generate the JSON data
    data = {}

    for number in range(required_pairs): 
      data[f"{generate_random_string(avg_key_length)}_{number}"] = generate_random_string(avg_value_length)
      print(f"Writing... Actual {number}/{required_pairs}")
    
    # Write to file and check final size
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    # Verify and pad if necessary
    final_size = os.path.getsize(filename)
    if final_size < target_size:
        padding_needed = target_size - final_size
        data["padding"] = "x" * padding_needed
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    print(f"Generated {filename} with size approximately {megabytes} MB")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_megabytes>")
    else:
        try:
            megabytes = int(sys.argv[1])
            write_json_to_size(megabytes)
        except ValueError:
            print("Please provide a valid integer for the number of megabytes.")

        