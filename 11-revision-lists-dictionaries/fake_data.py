import faker
import random

categories = ["junior", "senior", "retired", "trainee"]

f = faker.Faker()

for i in range(10):
    r = random.randint(0, 3)
    print(f.last_name(), f.first_name(), f.email(), f.job(),
          f.credit_card_number(), categories[r], f.date())
    
for i in range(10):
    print(f.isbn10(), f.sentence(), f.last_name(), f.first_name())