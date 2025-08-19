from zipfile import ZipFile
import pathlib

import requests

arc_corpus_url = 'https://s3-us-west-2.amazonaws.com/ai2-website/data/ARC-V1-Feb2018.zip'

data_dir = pathlib.Path('data', 'corpus')
data_dir.mkdir(exist_ok=True, parents=True)

corpus_filename = pathlib.Path(arc_corpus_url).name

if not pathlib.Path(data_dir / corpus_filename).exists():
  res = requests.get(arc_corpus_url)
  if res.ok:
    with open(data_dir / corpus_filename, 'wb') as f:
      f.write(res.content)
  else:
    raise RuntimeError("[ERROR]: cannot get ARC Corpus")
else:
  print(f'{corpus_filename} already cached in {data_dir}')

