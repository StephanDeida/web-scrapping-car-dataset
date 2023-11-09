import random

with open("cars_url.txt", "r", encoding='utf-8') as f:
    # Read the lines of the file and store them in a list
    car_urls = f.readlines()

# Strip newline characters from each line
car_urls = [line.strip() for line in car_urls]

emails = []
len = len(car_urls)
suffix_emails = ["@hotmail.com", "@gmail.com", "@proton.me", "@outlook.com", "@yahoo.com", "@outlook.de", "@gmx-topmail.de", "@arnoudkrell.com"]
first_names = ['Peter', 'Jhon', 'Michael', 'Felix', 'Dirk', 'Ulrich', 'Erik', 'FrankSchultheiss','Stephan', 'Adelhard', 'Wilmer', 'Luitpold', 'Ralph', 'Bodo', 'Thomas']
second_names = ['Hobbs', 'Purro', 'Meister', 'Meier', 'Hoch', 'Neustadt', 'Wechsler', 'Schultheiss', 'Roth', 'Wu', 'Gu', 'Du', 'June']
for i in range(len):
    first = random.choice(first_names)
    second = random.choice(second_names)
    suffix = random.choice(suffix_emails)
    email = first + "-" + second + suffix
    emails.append(email)
    #print(number)

with open("email_dataset.txt", "w", encoding='utf-8') as f:
    # Write each item in the list to a new line in the file
    for item in emails:
        f.write("%s\n" % item)
