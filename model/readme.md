# **Hierarchical Image classification Model** for Pillumi

알약 식별 모델에 관한 문서입니다.

## Directory Tree
```bash
.
├── data
├── src
├── Test
├── Train
│   ├── Data
│   ├── Util
│   └── Model
│       ├── Color
│       ├── Imprint
│       └── Shape
├── requirements.txt
├── .gitignore`
``` 


## Getting Started

### Environment Requirements

First, please make sure you have installed Conda. Then, our environment can be installed by:

```bash
conda create -n pill_identifier python=3.7.3
conda activate pill_identifier
pip install -r requirements.txt
``` 