import random

with open("cars_url.txt", "r", encoding='utf-8') as f:
    # Read the lines of the file and store them in a list
    car_urls = f.readlines()

# Strip newline characters from each line
car_urls = [line.strip() for line in car_urls]

whatsapp_nums = []
tel_nums = []
len = len(car_urls)
tel_1 = [52]
for i in range(len):
    first = random.choice(tel_1)
    second = random.choice(range(100, 999))
    number = f"Cel.({first}) {second}-{random.choice(range(10, 99))}.{random.choice(range(10, 99))}.{random.choice(range(10))}.{random.choice(range(10, 99))}, Cel.({first}) {second}-{random.choice(range(10, 99))}.{random.choice(range(10, 99))}.{random.choice(range(10))}.{random.choice(range(10, 99))}"
    tel_nums.append(number)
    whatsapp_number = f"+({first}) {random.choice(range(100, 999))} {random.choice(range(100, 999))} {random.choice(range(1000, 9999))}"
    whatsapp_nums.append(whatsapp_number)
    #print(number)

with open("tel_dataset.txt", "w", encoding='utf-8') as f:
    # Write each item in the list to a new line in the file
    for item in tel_nums:
        f.write("%s\n" % item)

with open("whatsapp_dataset.txt", "w", encoding='utf-8') as f:
    # Write each item in the list to a new line in the file
    for item in whatsapp_nums:
        f.write("%s\n" % item)
#print(random.choice(range(100, 999)))
