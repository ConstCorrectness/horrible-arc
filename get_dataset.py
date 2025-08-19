import kagglehub
import pathlib

data_dir = pathlib.Path('data', 'arc')
data_dir.mkdir(parents=True, exist_ok=True)

path = kagglehub.dataset_download('thedevastator/arc-grade-school-science-questions')
p = pathlib.Path(path)


for csv_file in p.iterdir():
  # Copy the ~/.cache/.../*.csv files to data/arc/*.csv
  file_path = data_dir / csv_file.name
  with open(csv_file, 'r', encoding='utf_8') as f1:
    with open(file_path, 'w', encoding='utf_8') as f2:
      f2.write(f1.read()) 
  
