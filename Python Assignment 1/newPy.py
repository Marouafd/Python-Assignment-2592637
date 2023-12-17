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

    if len(cleaned_word) > 3:
        first_letter = cleaned_word[0]
        remaining_letters = cleaned_word[1:]

        random_indices = random.sample(range(len(remaining_letters)), min(2, len(remaining_letters)))
        random_indices.sort()
        random_letters = [remaining_letters[i] for i in random_indices]

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

def is_abbreviation_from_multiple_names(abbreviation, abbreviations):
    return sum(1 for _, (name, _) in abbreviations.items() if abbreviation in name) > 1

def main():
    logging.basicConfig(level=logging.INFO)

    input_file = input("Enter the name of the input file (e.g., trees.txt): ")

    surname = input("Enter your surname: ").lower()
    output_file = f"{surname}_{input_file[:-4]}_abbrevs.txt"

    names = read_names(input_file)
    values = read_values("values.txt")  

    abbreviations = {}
    for name in names:
        word_abbreviations = generate_abbreviations_for_word(name, values)
        for abbreviation, score in word_abbreviations:
            if abbreviation not in abbreviations:
                abbreviations[abbreviation] = [(name, score)]
            else:
                abbreviations[abbreviation].append((name, score))

  
    with open(output_file, 'w') as file:
        for abbreviation, name_score_list in abbreviations.items():
            clean_abbreviation = abbreviation.replace("'", "")
            names_scores_str = " ".join([f"{name} (Score: {score})" for name, score in name_score_list])
            file.write(f"{clean_abbreviation}:{names_scores_str}\n")

if __name__ == "__main__":
    main()
