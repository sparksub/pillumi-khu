# **Hierarchical Image classification Model for Pillumi**

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
## Model Train Work Flow
<img width="600" alt="model-workflow" src="https://user-images.githubusercontent.com/50730365/209358357-925d65d4-afbd-4288-9109-1449172a434b.png">

<br/>

## Preprocessing
<img width="600" alt="model-preprocessing" src="https://user-images.githubusercontent.com/50730365/209358813-6e00c18c-66db-4edf-9f35-9b0ab2eb5996.png">

<br/>

## Model - Shape Classification
<img width="600" alt="model-shape" src="https://user-images.githubusercontent.com/50730365/209358825-572eddab-ffbc-4241-b7cb-857f4a554bff.png">  

<br/>

## Model - Color Identifier
<img width="600" alt="model-color" src="https://user-images.githubusercontent.com/50730365/209358826-de2d6eef-3843-4e8b-84f7-b2f2d4df12cc.png">

<br/>

## Model - Imprint Classification
<img width="600" alt="model-imprint" src="https://user-images.githubusercontent.com/50730365/209358824-a994cb16-7106-46e9-a82c-2e8a9e02fb27.png">


<br/><br/>


## Getting Started
---
### Environment Requirements

First, please make sure you have installed Conda. Then, our environment can be installed by:

```bash
conda create -n pill_identifier python=3.7.3
conda activate pill_identifier
pip install -r requirements.txt
``` 