import random
import time
import sys
import difflib
from textblob import TextBlob  
import sqlite3

database = 'writers.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()

# Writing prompts
writing_prompts = [
    "Set your story in a haunted school, however, it's not your typical haunting in which a former student is haunting the locker rooms or the gym or a professor in the library. The ghost that haunts your school is the ghost of a pigeon.",
    "Your character doesn't find it weird that they just met a talking crow. However, they find it weird that this talking crow is wearing a suit and tie and is carrying a pocket watch.",
    "The time has come. The world is ending. There's only one who can save the human race and that is... a cow????????",
    "You're staying in a hotel, but something feels off. You find that a strong energy is radiating from inside of a closet. You open the closet door to find....",
    "You're a runaway prince. Why are you running?",
    "You're a witch hunter hunting witches in your hometown, one witch in particular is very familiar",
    "On Halloween, weird things start happening all around you. Little did you know that it was your fault",
    "You're the captain of a pirate ship with an outrageous and a little bit of an unusual crew. Tell me about them?",
    "You are a shark who's about to start their first day of the new school year",
    "Tell me about your favorite book? Why is it the best? Or perhaps, a better question is to tell me why it clearly has to be better than your opponent's favorite book",
    "You're a shark whose best friend is a sea turtle",
    "You're an undercover witch posing as a witch hunter among the other hunters. Unfortunately, you've started having feelings for one of the hunters",
    "You're a houseplant who just got taken into a new home. Your owner, no matter how hard they try, has the worst green thumb you've ever seen",
    "You've just moved into a new neighborhood and your neighbors are… weird.",
    "You bought a used car and it's been making a bunch of weird noises ever since you got it home. When you check it out, you find that the noise is coming from an unusual source.",
    "Jamie Jones wrote crime novels. What she hadn't expected was for her partner to go missing, and for all eyes to be trained on her. With her career, she shouldn't have been too surprised. Her search history was concerning, to say the least. The most bizarre part of it all, was her considering the fact that maybe they were right.",
    "It was 1902, the sun was shining. The birds were chirping. I was writing silly little writing prompts for a silly little game. There was a pirate ship. There was a pirate. It was by far, a curious adventure that was being partaken. That''s all for this one. Please defeat the monster."
]



cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        writer_name TEXT,
        prompt TEXT,
        entry TEXT
    )
''')
conn.commit()
conn.close()



print("Oh no! You've come face to face with a giant, and he looks ready to attack.")
print("Read the writing prompt. Once you start typing, you'll only have 60 seconds to complete the task and take down the ogre.")
print("Careful. The more typos you make, the more damage YOU take. Don't let me down...")
print("What...? You didn't think I was going to help, did you? I don't get paid enough to take on a giant. Well- guess you're not being paid either.... anyways, good luck!")


#User introduction

# Randomly select a writing prompt
rand_prompt = random.choice(writing_prompts)

#spellcheck submission

def spellcheck(input_text, score):
    # Use TextBlob for spellchecking
    spell_check = TextBlob(input_text)
    corrected_words = spell_check.words
    original_words = input_text.split()
    num_misspelled = sum(1 for orig_word, corr_word in zip(original_words, corrected_words) if orig_word != corr_word)

    return score - num_misspelled

    def score_writing(entry, prompt):
    # Creativity score based on the length of the entry
        creativity_score = len(entry)

        # Grammar score based on the number of spelling and grammar errors (you may need a library like LanguageTool for this)
        # For this example, we'll just count the number of spaces as a simple grammar score
        grammar_score = entry.count(' ')

        # Similarity score between the entry and the prompt
        similarity_score = difflib.SequenceMatcher(None, entry, prompt).ratio()

        # Calculate the total score based on weights for each criterion
        total_score = (creativity_score * 0.4) + (grammar_score * 0.3) + (similarity_score * 0.3)

    return total_score


# Main function
def main():
    start_time = time.time()

    writer_health = 10
    monster_health = 50
    
    writer_one = input("Oh, before we get started... What's your name, again? You know, so I know what to put on your tombstone? ")
    print(f"Hello, {writer_one}!\n")
    time.sleep(1)

    while True:
        rand_prompt = random.choice(writing_prompts)

        print(rand_prompt + "\n")

        start_time = time.time()
        input_string = input("\nYou have 60 seconds. Begin!\n")

        elapsed_time = time.time() - start_time

        print("\nTime is up!\n")
        print(f"This is the text you submitted:\n{input_string}\n")
        time.sleep(3)

        print('\n\n\n')
        print("Welcome back.... guess you survived. Huh, waste of money on that tombstone then. Specialized and everything....")
        print("Welp, here's your money. Take it and get out of here. Come again! ")

if __name__ == "__main__":
    main()
