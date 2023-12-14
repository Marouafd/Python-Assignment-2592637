import logging
import random
import re

def read_values(file_path):
    try:
        with open(file_path, 'r') as file:
            return {letter: int(score) for line in file for letter, score in [line.strip().split()]}
    except FileNotFoundError:
        logging.error(f"Error: FILE NOT FOUND AT {file_path}")
        return {}

def read_names(file_path):
    try:
        with open(file_path, 'r') as file:
            return [name.strip() for name in file.readlines()]
    except FileNotFoundError:
        logging.error(f"Error: FILE NOT FOUND AT {file_path}")
        return []

def generate_abbreviations_for_word(word, values):
    abbreviations = set()
    cleaned_word = re.sub(r'[^a-zA-Z ]', '', word).upper()  

    if len(cleaned_word) >= 3:
        first_letter = cleaned_word[0]
        random_letters = random.sample(cleaned_word[1:], min(2, len(cleaned_word) - 1))
        abbreviation = first_letter + ''.join(random_letters)

        if not any(char.isspace() for char in abbreviation): 
            score = calculate_score(abbreviation, cleaned_word, values)
            abbreviations.add((abbreviation, score))

    return abbreviations

def calculate_score(abbreviation, word, values):
    score = 0

    for i, letter in enumerate(abbreviation):
        if i == 0:
            continue   
        elif i == 1 and letter == word[-1]:
            score += 5 if letter != 'E' else 20
        else:
            position_value = 1 if i == 1 else 2 if i == 2 else 3
            score += position_value + values.get(letter, 0)

    return score

def main():
    logging.basicConfig(level=logging.INFO)

    file_path = "trees.txt"
    values_file_path = "values.txt"

    file_path = file_path.replace(" ", "")
    values_file_path = values_file_path.replace(" ", "")

    names = read_names(file_path)
    values = read_values(values_file_path)
    abbreviations = {}

    for name in names:
        word_abbreviations = generate_abbreviations_for_word(name, values)

        for abbreviation, score in word_abbreviations:
            if abbreviation not in abbreviations:
                abbreviations[abbreviation] = (name, score)

   
    for abbreviation, (name, score) in abbreviations.items():
        clean_abbreviation = abbreviation.replace("'", "")
        print(f"{clean_abbreviation}:{name} (Score: {score})")

if __name__ == "__main__":
    main()
