class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + " - " + self.meaning


flashcards = []

print("Welcome to the Flashcard App!")

while True:
    word = input("Enter a word (or 'exit' to quit): ")
    if word.lower() == 'exit':
        break
    meaning = input("Enter the meaning of the word: ")
    flashcards.append(Flashcard(word, meaning))
    print("Flashcard added successfully!")
    print("Current flashcards:")
    for card in flashcards:
        print(f" - {card}")

print("Thank you for using the Flashcard App!")
