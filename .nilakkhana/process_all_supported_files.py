import pathlib
import json
from typing import Dict

from fast_nilakkhana import process_file

repo_dir = pathlib.Path(__file__).absolute().parent.parent

filtered_root_files = [x for x in repo_dir.glob('root/**/*.json') if x.name.find(
    'site') == -1 and x.name.find('blurb') == -1 and x.name.find('name') == -1]

filtered_translation_files = [x for x in repo_dir.glob('translation/**/*.json') if x.name.find(
    'site') == -1 and x.name.find('blurb') == -1 and x.name.find('name') == -1]

comment_files = [x for x in repo_dir.glob('comment/**/*.json')]

print('Processing root text files[%d].'%(len(filtered_root_files)))
for file in filtered_root_files:
    process_file(file)
print('Root text files transformed.')

print('Processing translation text files[%d].'%(len(filtered_translation_files)))
for file in filtered_translation_files:
    process_file(file)
print('translation text files transformed.')

print('Processing comment text files[%d].'%(len(comment_files)))
for file in comment_files:
    process_file(file)
print('comment text files transformed.')
