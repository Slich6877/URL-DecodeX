import os
import urllib.parse # Importing urllib.parse to decode URL-encoded strings

# Function to decode a URL-encoded string
def decode_url(encoded_str):
    return urllib.parse.unquote(encoded_str)

def log_decoder():
    action = input("Press (U) to decode a URL string or (L) to decode a log file: ").strip().lower()
    
    if action == 'u':
        encoded_url = input("Enter the URL-encoded string: ")
        print("Decoded URL:", decode_url(encoded_url))
    
    elif action == 'l':
        log_file_path = input("Enter the path of the access log file: ").strip()
        output_log_path = input("Enter the path where the decoded log file should be saved: ").strip()
        
        try:
            with open(log_file_path, 'r', encoding='utf-8') as log_file:
                log_content = log_file.read()
            
            decoded_log_content = decode_url(log_content)

            # Ensure the output directory exists and if it doesnt, create it (including any necessary parent directories)
            os.makedirs(os.path.dirname(output_log_path), exist_ok=True)
            
            with open(output_log_path, 'w', encoding='utf-8') as output_file:
                output_file.write(decoded_log_content)
            
            print(f"Decoded log content saved to {output_log_path}")
        
        except FileNotFoundError:
            print("Error: The specified log file was not found. Please check the file path and try again.")
        except Exception as error:
            print(f"An error occurred: {error}")
    
    else:
        print("Invalid input. Please choose either 'U' for URL string or 'L' for log file.")

# Run the script only if executed directly (not imported as a module)
if __name__ == "__main__":
    log_decoder()
