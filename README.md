# Sea Level Predictor

This project involves using Python to analyze and visualize historical sea level data and make predictions about future sea levels using linear regression.

## Project Overview

The project aims to:
1. Use historical sea level data to create a scatter plot.
2. Fit a linear regression model to the entire dataset.
3. Fit a linear regression model to the data from the year 2000 onwards.
4. Extend the models to make predictions about future sea levels.

## Requirements

- Python 3
- pandas
- matplotlib
- scipy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sea-level-predictor.git
    cd sea-level-predictor
    ```

2. Install the required libraries:
    ```bash
    pip install pandas matplotlib scipy
    ```

## Usage

1. Make sure you have the data file `epa-sea-level.csv` in the project directory.

2. Run the script `sea_level_predictor.py`:
    ```bash
    python sea_level_predictor.py
    ```

3. The script will generate a plot `sea_level_plot.png` that includes:
    - A scatter plot of the historical sea level data.
    - A linear regression line fitted to the entire dataset.
    - A linear regression line fitted to the data from 2000 onwards.

## Code Explanation

### Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

