import os

def process_dictionary_files(input_path, output_path):
    # Initialize dictionaries in the heap
    raw_data = {}
    inverted_data = {}

    try:
        # 1. Parsing text to Dictionary
        # Using a context manager ensures the file descriptor is released
        with open(input_path, 'r') as reader:
            for line in reader:
                if ':' in line:
                    key, value = line.strip().split(':')
                    raw_data[key.strip()] = value.strip()

        # 2. Inversion Logic
        # Values in raw_data become keys in inverted_data
        for key, value in raw_data.items():
            # If the value exists, append the new key to the existing list
            if value not in inverted_data:
                inverted_data[value] = [key]
            else:
                inverted_data[value].append(key)

        # 3. Writing persistent output
        with open(output_path, 'w') as writer:
            for val, keys in inverted_data.items():
                # String interpolation using f-strings for efficiency
                formatted_line = f"{val}: {', '.join(keys)}\n"
                writer.write(formatted_line)
        
        print(f"I/O Operation Successful: {output_path} generated.")

    except FileNotFoundError:
        print(f"Error: The system cannot find the file specified: {input_path}")
    except PermissionError:
        print("Security Error: Access to write to the storage medium was denied.")
    except Exception as error:
        print(f"Runtime Exception: {error}")

# Execution
process_dictionary_files('original_dict.txt', 'inverted_dict.txt')
