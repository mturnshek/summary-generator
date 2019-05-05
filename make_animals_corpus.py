import wikipediaapi
import os


if not os.path.isdir("downloaded_animal_summaries"):
  os.mkdir("downloaded_animal_summaries")

wiki = wikipediaapi.Wikipedia('en')

downloaded_animal_summaries = os.listdir("downloaded_animal_summaries")

shortest_allowed = 280

animals = [
  "Zebra",
  "Crocodile",
  "Rat",
  "Orca",
  "Mosquito",
  "Jaguar",
  "Leopard",
  "Skink",
  "Skunk",
  "Mite",
  "Honey bee",
  "Dog",
  "Wolf",
  "Mammoth",
  "Giraffe",
  "Blue whale",
  "Mako shark",
  "Frog",
  "Earthworm",
  "Dolphin",
  "Sea lion",
]


def get_summary(animal):
  if animal in downloaded_animal_summaries:
    f = open("downloaded_animal_summaries/" + animal, 'r')
    summary = f.read()
    f.close()
    return summary
  else:
    try:
      summary = wiki.page(animal).summary
      f = open("downloaded_animal_summaries/" + animal, "w+")
      f.write(summary)
      f.close()
      return summary
    except:
      pass
    return ""


corpus = ""
for animal in animals:
  summary = get_summary(animal)
  if len(summary) > shortest_allowed:
    corpus += "\n####\n" + animal + "\n::::\n"
    corpus += summary

print(corpus)
f = open("animal_summaries_corpus.txt", 'w+')
f.write(corpus)
f.close()
