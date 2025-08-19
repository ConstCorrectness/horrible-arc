# Horrible ARC 
AI2 Reasoning


![Kaggle Hub](https://img.shields.io/badge/kaggle-hub-blue?logo=kaggle)
![GitHub](https://img.shields.io/github/license/ConstCorrectness/horrible-arc?logo=github)
![License](https://img.shields.io/badge/license-GNU%20GPLv3-blue)


## Getting the ARC (_AI2 Reasoning Challenge_) Dataset:
- Dataset can be downloaded from:
  - [Kagglehub](https://www.kaggle.com/datasets/thedevastator/arc-grade-school-science-questions/data?select=ARC-Challenge_test.csv)
  - [Allen AI Hugging Face 🤗](https://allenai.org/data/arc)

## Dataset Files:
- The dataset consists of three main .csv files:
  - `ARC-Challenge_test.csv` (for testing)
  - `ARC-Challenge_train.csv` (for training)
  - `ARC-Challenge_validation.csv` (for validation)
 
Each file contains the following columns:
  - `id` - ID.
  - `question` - Question text.
  - `choices` - JSON object containing the answer choices.
  - `answerKey` - The correct answer.


## Original Paper:
- The original paper describing the challenge can be found: 
    - [Website](https://arxiv.org/abs/1803.05457)
    - [Copy of PDF](original_paper.pdf)

## Citations:

```
@article{clark2018think,
  title={Think you have solved question answering? Try ARC, the AI2 Reasoning Challenge},
  author={Clark, Peter and Gardner, Matt and Khot, Tushar and Sabharwal, Ashish},
  journal={arXiv preprint arXiv:1803.05457},
  year={2018}
}
```

## License:
- The dataset is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).


