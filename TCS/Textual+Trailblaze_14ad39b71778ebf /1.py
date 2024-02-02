def extract_last_character(ip_list):
    last_characters = []
    for ip in ip_list:
        last_character = ip[-1]
        last_characters.append(last_character)
    return last_characters

# Example list of IP addresses
ip_list = [
    "2610:a1:5cec:2571:7722:d57e",
    "2610:a1:e44e:e2cc:f6e6:43f8",
    "2610:a1:64e4:0eea:c937:ac3b",
    "2610:a1:0a8e:4e16:4e18:95a3"
]

# Extract the last character from each IP
last_characters = extract_last_character(ip_list)

# Print the extracted last characters
print("Last characters from each IP:")
for char in last_characters:
    print(char)
