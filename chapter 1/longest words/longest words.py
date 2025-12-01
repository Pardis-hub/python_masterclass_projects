#Take a sentence from user
def take_sentence():
    return input("Enter your sentence: ")

#Detect longestest word(s)
def longest_words(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key = len, reverse = True)
    print("Longest word(s): ")
    print(f"{sorted_words[0]} ({len(sorted_words[0])} letters)")
    for i in range(len(sorted_words)-1):
        if len(sorted_words[i+1]) == len(sorted_words[i]):
            print(f"{sorted_words[i+1]} ({len(sorted_words[i+1])} letters)")
        else:
            break

#Create main
def main():
    longest_words(take_sentence())

#Run the program
main()