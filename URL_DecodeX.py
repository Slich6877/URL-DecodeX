import os
import re

# Custom mapping of URL-encoded characters to their decoded equivalents
url_encoding_map = {
    "%20": " ",
    "%21": "!",
    "%22": '"',
    "%23": "#",
    "%24": "$",
    "%25": "%",
    "%26": "&",
    "%27": "'",
    "%28": "(",
    "%29": ")",
}

# Regex pattern to match encoded URL components
url_pattern = re.compile('|'.join(re.escape(key) for key in url_encoding_map.keys()), re.IGNORECASE)

# Function to decode URL-encoded string
def decode_url(encoded_str):
    return url_pattern.sub(lambda match: url_encoding_map[match.group(0).upper()], encoded_str)

# Main function to handle user interaction
def log_decoder():
    action = input("Press (U) for decode a URL string or Press (F) for decode a Log file? ").strip().lower()

    if action == 'u':
        encoded_url = input("Enter the URL-encoded string: ")
        decoded_url = decode_url(encoded_url)
        print("Decoded URL:", decoded_url)

    elif action == 'l':
        log_file_path = input("Enter the path of the access log file to decode: ").strip()
        output_log_path = input("Enter the path where the decoded log file should be saved: ").strip()

        try:
            # Read the log file content
            with open(log_file_path, 'r', encoding='utf-8') as log_file:
                log_content = log_file.read()

            # Decode the log content
            decoded_log_content = decode_url(log_content)

            # Ensure the output directory exists
            output_dir = os.path.dirname(output_log_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Write the decoded content to the output file
            with open(output_log_path, 'w', encoding='utf-8') as output_file:
                output_file.write(decoded_log_content)

            print(f"Decoded log content saved to {output_log_path}")

        except FileNotFoundError:
            print("The specified log file was not found. Please verify the file path and try again.")
        except Exception as error:
            print(f"An error occurred: {error}")

    else:
        print("Invalid input. Please choose either 'U' for URL or 'L' for log file.")

if __name__ == "__main__":
    log_decoder()
