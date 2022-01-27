from glob import glob
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

directory_origin = 'sources'
directory_target = 'notes'
file_format_origin = '.pdf'
file_format_target = '.yml'

file_paths_origin = sorted(glob(f"{directory_origin}/*{file_format_origin}"))
file_paths_target = sorted(glob(f"{directory_target}/*{file_format_target}"))

def capitalize_words(words):
    return " ".join([word.capitalize() for word in words.split('-')])

quotes = []
for file_path_target in file_paths_target:
    title = file_path_target.split('/')[-1].split('.')[0]
    with open(file_path_target, 'r') as stream:
        data = load(stream, Loader=Loader)
        chapters = data.keys()
        for chapter in chapters:
            quotes_in_chapter = data[chapter]['quotes']
            for quote in quotes_in_chapter:
                if quote != "":
                    quotes.append({
                        "text": quote,
                        "title": capitalize_words(title),
                        "chapter": capitalize_words(chapter)
                    })

for i, quote in enumerate(quotes):
    print(f"\n{i + 1:02d}: \"{quote['text']}\" - {quote['title']}, {quote['chapter']}")
print()