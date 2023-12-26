question_data = question_data = [
    {'text': 'Bananas are berries.', 'answer': 'True'},
    {'text': 'Mount Everest is the tallest mountain in the world.', 'answer': 'True'},
    {'text': 'The Great Wall of China is visible from space.', 'answer': 'False'},
    {'text': 'Cats can swim naturally.', 'answer': 'False'},
    {'text': 'Honey never spoils.', 'answer': 'True'},
    {'text': 'The Eiffel Tower was originally intended for Barcelona.', 'answer': 'False'},
    {'text': "A group of flamingos is called a 'flamboyance'.", 'answer': 'True'},
    {'text': 'Venus is the hottest planet in our solar system.', 'answer': 'True'},
    {'text': 'Penguins are mammals.', 'answer': 'False'},
    {'text': 'The capital of Canada is Toronto.', 'answer': 'False'},
    {'text': 'Ostriches can fly.', 'answer': 'False'},
    {'text': 'The human brain stops growing after the age of 18.', 'answer': 'False'},
    {'text': 'Ants can sleep.', 'answer': 'False'},
    {'text': 'The longest river in the world is the Nile.', 'answer': 'True'},
    {'text': 'Spiders have six legs.', 'answer': 'False'},
    {'text': 'The Pacific Ocean is the largest ocean on Earth.', 'answer': 'True'},
    {'text': 'Octopuses have three hearts.', 'answer': 'True'},
    {'text': 'Cows have four stomachs.', 'answer': 'True'},
    {'text': 'The moon is larger than Pluto.', 'answer': 'True'},
    {'text': 'The Statue of Liberty was a gift from France.', 'answer': 'True'},
    {'text': 'Kangaroos can only jump forward, not backward.', 'answer': 'True'},
    {'text': 'Apples float in water.', 'answer': 'False'},
    {'text': "A group of owls is called a 'parliament'.", 'answer': 'True'},
    {'text': 'There are five rings on the Olympic flag.', 'answer': 'True'},
    {'text': 'Goldfish have a three-second memory.', 'answer': 'False'},
    {'text': 'The sun is a planet.', 'answer': 'False'},
    {'text': "A 'jiffy' is an actual unit of time.", 'answer': 'True'},
    {'text': 'Humans can regrow limbs like some animals.', 'answer': 'False'},
    {'text': 'All snowflakes have six sides.', 'answer': 'True'},
    {'text': 'Venus is the only planet that rotates clockwise.', 'answer': 'False'},
    {'text': 'The longest word in the English language has 45 letters.', 'answer': 'True'},
    {'text': 'A day on Mars is longer than a day on Earth.', 'answer': 'True'},
    {'text': 'Elephants are afraid of mice.', 'answer': 'False'},
    {'text': 'The shortest war in history lasted only 38 minutes.', 'answer': 'True'},
    {'text': 'Hippopotamus milk is pink.', 'answer': 'True'},
    {'text': 'Cats have five toes on their front paws.', 'answer': 'False'},
    {'text': 'The Great Barrier Reef is the largest living structure on Earth.', 'answer': 'True'},
    {'text': "A 'googol' is the number 1 followed by 100 zeros.", 'answer': 'True'},
    {'text': 'The Earth is flat.', 'answer': 'False'},
    {'text': 'A snail can sleep for three years.', 'answer': 'True'},
    {'text': 'Polar bears are left-handed.', 'answer': 'False'},
    {'text': 'The human heart pumps approximately 2,000 gallons of blood per day.', 'answer': 'False'},
    {'text': 'All snowflakes are unique.', 'answer': 'True'},
    {'text': 'The speed of light is faster than the speed of sound.', 'answer': 'True'},
    {'text': "A 'fortnight' is equal to 100 years.", 'answer': 'False'},
    {'text': 'The Sahara Desert is the largest desert in the world.', 'answer': 'False'},
    {'text': 'The first computer mouse was made of wood.', 'answer': 'True'},
    {'text': 'The sun sets in the west.', 'answer': 'True'},
    {'text': 'Bees can recognize human faces.', 'answer': 'True'},
    {'text': 'A tomato is a fruit.', 'answer': 'True'},
    {'text': 'Sharks are mammals.', 'answer': 'False'},
    {'text': 'The Amazon River is the longest river in the world.', 'answer': 'False'},
    {'text': 'Olympic gold medals are made of pure gold.', 'answer': 'False'},
    {'text': "A 'decade' is equivalent to 15 years.", 'answer': 'False'},
    {'text': 'The Earth is approximately 4.5 billion years old.', 'answer': 'True'},
    {'text': "A 'quasar' is a type of dinosaur.", 'answer': 'False'},
    {'text': 'The Great Wall of China is visible from the moon.', 'answer': 'False'},
    {'text': 'Humans can breathe and swallow at the same time.', 'answer': 'False'}
]



def remove_duplicate_questions(question_list):
    unique_questions = []
    seen_questions = set()

    for question in question_list:
        question_text = question["text"]
        if question_text not in seen_questions:
            unique_questions.append(question)
            seen_questions.add(question_text)

    return unique_questions

# Example usage:
unique_question_data = remove_duplicate_questions(question_data)
