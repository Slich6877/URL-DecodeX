# URL-DecodeX

This Python script allows you to decode URL-encoded strings or access log files containing URL-encoded data. It offers two modes of operation:

URL Encoding Decoder: You can input a URL-encoded string, and it will decode it to its readable format.

Log File Decoder: You can input a path to an access log file, and the script will decode all URL-encoded components in the file and save the decoded content to a new file of your choosing.

Features:

 • Supports decoding of all URL-encoded characters since its now using the urllib.parse which is a submodule of urllib that deals with URL parsing and manipulation.

 • Option to decode both individual URL strings or entire log files.

 • The ability to specify a custom filename and path for the decoded output.

Usage:

Run the script, choose your mode (URL string or log file), and follow the prompts to input the URL string or file paths. 
The decoded result will be saved in the specified output file.

#Important:

  • Use the path where the file that you want to decode is located when the input asks you:

Example:

"Enter the path of the access log file to decode (dont forget the extension of the file):" C:\xxx\xxx\Test.txt

"Enter the path where the decoded log file should be saved (dont forget the extension of the file):" C\xxx\xxx\Test_decompiled.txt
