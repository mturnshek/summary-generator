import wikipediaapi


wiki = wikipediaapi.Wikipedia('en')

animals = [
  "Zebra",
  "Crocodile",
  "Rat",
  "Orca",
  "Mosquito",
  "Jaguar",
  "Leopard",
  "Archer's buzzard",
  "Skink",
  "Skunk",
  "Mite",
  "Honey bee",
  "Dog",
  "Wolf",
  "Mammoth"
]


def get_summary(page):
  try:
    return wiki.page(animal).summary
  except:
    return ""


corpus = ""
for animal in animals:
  corpus += "\n####\n" + animal + "\n::::\n"
  corpus += get_summary(wiki.page(animal))

print(corpus)
