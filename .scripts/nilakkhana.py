import pathlib
import json
from typing import Dict

from fast_nilakkhana import process_file

SUPPORTED_FILE_TYPES = ['comment', 'root', 'translation']

repo_dir = pathlib.Path(__file__).absolute().parent.parent

filtered_root_files = [x for x in repo_dir.glob('root/**/*.json') if x.name.find(
    'site') == -1 and x.name.find('blurb') == -1 and x.name.find('name') == -1]

filtered_translation_files = [x for x in repo_dir.glob('translation/**/*.json') if x.name.find(
    'site') == -1 and x.name.find('blurb') == -1 and x.name.find('name') == -1]

comment_files = [x for x in repo_dir.glob('comment/**/*.json')]

print('Processing root text files[%d].'%(len(filtered_root_files)))
for file in filtered_root_files:
    process_file(file)
print('Root text files processed.')


print('Processing translation text files[%d].'%(len(filtered_translation_files)))
for file in filtered_translation_files:
    process_file(file)
print('translation text files processed.')


print('Processing variant text files[%d].'%(len(variant_files)))
for file in variant_files:
    process_file(file)
print('variant text files processed.')


print('Processing comment text files[%d].'%(len(comment_files)))
for file in comment_files:
    process_file(file)
print('comment text files processed.')
