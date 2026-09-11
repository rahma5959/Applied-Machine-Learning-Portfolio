# Comparative Study of Clustering Algorithms

## Overview

This project compares three clustering algorithms:

- K-Means
- DBSCAN
- Agglomerative Clustering

on a non-linear dataset (Moons dataset).

The goal is to demonstrate the limitations of centroid-based clustering
and highlight the strengths of density-based methods.

## Key Insights

- K-Means fails on non-spherical clusters.
- DBSCAN correctly identifies curved structures.
- Agglomerative clustering performs well but depends on linkage criteria.

## Evaluation Metric

Silhouette Score is used to evaluate cluster cohesion and separation.

## Technologies

- Python
- Scikit-learn
- NumPy
- Matplotlib
