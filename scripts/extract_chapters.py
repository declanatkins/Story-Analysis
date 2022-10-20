import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('book_file_path', type=str, help='The path to the book to parse.')
parser.add_argument('chapters_directory', type=str, help='The path to directory where chapters should be outputted')
parser.add_argument('--first-chapter-name', type=str, default='', help='The name of the first chapter to extract')
parser.add_argument('--last-chapter-name', type=str, default='', help='The name of the last chapter to extract')
parser.add_argument('--chapter-delimiter', type=str, default='\n\n\n\n', help='The delimiter on which to split chapters')
args = parser.parse_args()


with open(args.book_file_path) as book_f:
    full_text = book_f.read()

chapters = full_text.split(args.chapter_delimiter)

while args.first_chapter_name and chapters and not chapters[0].strip().startswith(args.first_chapter_name):
    del chapters[0]

if not chapters:
    raise ValueError(f'Chapter: {args.first_chapter_name} was not found')

while args.last_chapter_name and chapters and not chapters[-1].strip().startswith(args.last_chapter_name):
    del chapters[-1]

if not chapters:
    raise ValueError(f'Chapter: {args.last_chapter_name} was not found')

for i, chapter in enumerate(chapters):
    with open(os.path.join(args.chapters_directory, f'{i}.txt'), 'w') as chapter_f:
        chapter_f.write(chapter.strip())