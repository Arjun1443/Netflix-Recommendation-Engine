# Netflix Ratings Recommendation Experiments

A recommendation notebook using Netflix ratings and Surprise's SVD model.

## Why this project matters

Recommendation systems turn user–item interactions into ranking and prediction problems. This project provides a practical setting for exploring sparse ratings data and matrix factorization.

## Technical focus

Python · pandas · NumPy · exploratory analysis · Surprise SVD · cross-validation

## Explore the implementation

Open [the notebook](<Netflix Recommendation Engine.ipynb>) to inspect preprocessing, implementation, and saved outputs.

## Run locally

```bash
git clone https://github.com/Arjun1443/Netflix-Recommendation-Engine.git
cd Netflix-Recommendation-Engine
python -m venv .venv
# Activate .venv before continuing.
python -m pip install numpy pandas matplotlib seaborn scikit-surprise jupyter
python -m jupyter notebook
```

Select `Netflix Recommendation Engine.ipynb` in Jupyter and review its configuration before executing cells in order.

## Reproducibility notes

`Copyofmovie_titles.csv` is included; the ratings file `combined_data_1.txt` is not. Obtain the appropriate ratings data under its terms and replace both Windows-specific input paths. Large ratings datasets can require substantial memory. The inspected notebook supports SVD-based collaborative filtering; content-based and hybrid systems should be treated as extensions unless separately implemented.

Saved notebook outputs describe a prior execution; they are not an independently reproduced benchmark. Dependency versions are not locked, so compatibility may require adjustment.


## Author

[Naga Anweesh Reddy](https://github.com/Arjun1443/Naga-Anweesh-Reddy) · AI development and technical training
