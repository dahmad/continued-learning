from glob import glob
from shared import file_paths_target
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from termcolor import colored


def capitalize_words(words):
    return " ".join([word.capitalize() for word in words.split('-')])

quotes = []
for file_path_target in file_paths_target:
    title = file_path_target.split('/')[-1].split('.')[0]
    with open(file_path_target, 'r') as stream:
        try:
            data = load(stream, Loader=Loader)
            chapters = data.keys()
            for chapter in chapters:
                quotes_in_chapter = data[chapter]['quotes']
                for quote in quotes_in_chapter:
                    if quote != "":
                        quotes.append({
                            "text": quote,
                            "title": capitalize_words(title),
                            "chapter": chapter
                        })
        except:
            pass

for i, quote in enumerate(quotes):
    attribution = f"\n- {quote['title']}, {quote['chapter']}"
    print(f"\n{i + 1:02d}: {colored(quote['text'], 'grey', 'on_white')}{attribution}")
print()