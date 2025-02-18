# URL-DecodeX

This Python script allows you to decode URL-encoded strings or access log files containing URL-encoded data. It offers two modes of operation:

URL Encoding Decoder: You can input a URL-encoded string, and it will decode it to its readable format.

Log File Decoder: You can input a path to an access log file, and the script will decode all URL-encoded components in the file and save the decoded content to a new file of your choosing.

Features:

 • Supports decoding of URL-encoded characters(UTF-8,Wins-1252) (such as:
%20
%21
%22
%23
%24
%25
%26
%27
%28
%29).

 • Option to decode both individual URL strings or entire log files.
 • The ability to specify a custom filename and path for the decoded output.

Usage:

Run the script, choose your mode (URL string or log file), and follow the prompts to input the URL string or file paths. 
The decoded result will be saved in the specified output file.
