import random

def get_nvowels(s):
    n = 0
    for c in s:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            n += 1
    return n

def one_match(s, charlist):
    for c in charlist:
        if c in s:
            return True

    return False

def all_match(s, charlist):
    for c in charlist:
        if c not in s:
            return False

    return True

def indices_match(s, pairlist):
    for (c, idx) in pairlist:
        if s[idx - 1] != c:
            return False

    return True

def filter_words(wordlist, information):
    filtered = []
    for word in wordlist:
        if not one_match(word, information["wrong"]) and indices_match(word, information["correct"]):
            if not information["elsewhere"] or one_match(word, information["elsewhere"]):
                filtered.append(word)

    return filtered

def choose_based_on(wordlist, information):
    word = random.choice(wordlist)
    if information["elsewhere"]:
        while not all_match(word, information["elsewhere"]):
            word = random.choice(wordlist)

    return word

def main():
    words = open("dictionary.txt", "r")
    wordlist = [word.strip() for word in words]
    words.close()

    word = random.choice(wordlist)
    information = {"wrong": [], "elsewhere": [], "correct": set()}

    while True:
        print(f"try {word}")

        # Get information about word inserted
        print("which characters are incorrect?")
        wrong_input = input("> ")
        if wrong_input == "i win":
            print("awesome!")
            break

        if wrong_input != "all":
            information["wrong"] += wrong_input.split()
        else:
            information["wrong"] += [c for c in word]

        print("which characters are somewhere else?")
        elsewhere_input = input("> ")
        if elsewhere_input != "none":
            information["elsewhere"] += elsewhere_input.split()

        print("which characters are correct and in which positions?")
        correct_input = input("> ")
        correct = []
        if correct_input != "none":
            for position in correct_input.split():
                split = position.split(',')
                information["correct"].add((split[0], int(split[1])))

        wordlist = filter_words(wordlist, information)
        word = choose_based_on(wordlist, information)

if __name__ == "__main__":
    main()
