# FruitClassifierDT

## Objective
Classify fruits into Apple, Orange, or Lemon based on their physical characteristics.

## Problem Type
Multi-class classification (Apple / Orange / Lemon).

## Dataset
Synthetic structured tabular data with 10 samples.

### Input features
- color_intensity  
- texture_score  
- shape_compactness  
- area  

### Output
- fruit (Apple / Orange / Lemon)

## Model
Decision Tree Classifier

### Why Decision Tree?
- Suitable for small structured datasets  
- Handles non-linear relationships between features  
- Provides interpretability (visual tree and rules)  
- No feature scaling required  
- Easy to explain to non-technical stakeholders

## Training
- Train/Test split: 80% / 20%  
- Criterion: Gini  
- Max depth: 3  
- Min samples split: 2  

## Evaluation
- Classification report (precision, recall, F1-score)  
- Confusion matrix printed in console  
- Tree rules printed for interpretation  

## How to run
```bash
python Decision_Tree_Fruit_Classification.py
