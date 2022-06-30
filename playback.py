#Playback Speed
#prompts the user for input and then output that same input, replacing each space with ... (i.e., three periods)

def main():
    userinput = input("Please enter a string: ")
    print(userinput.replace(" ","..."))

main()
    