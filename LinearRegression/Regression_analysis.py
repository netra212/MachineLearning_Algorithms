'''
# Why ML Problems are a statistical Inference Problem ?
Question Understanding: With the help of sample, we try to find the estimate value for the value <-- this is called statistical inference problem.
Ans:- lpa = f`(cgpa, iq) + reducible_error + irreducible_error

Reasons:
    1. ML Algorithms try to learn the parameters or relationships from data to make predictions or decisions. This is conceptually similar to what statistical models do: estimate parameters from data to explain or predict a phenomenon.

    2. Uncertainty & Probabilistic Thinking
    ML operates in environments full of noise and uncertainty, just like statistics:
        Data can be noisy or incomplete.
        Predictions are not always exact — they have confidence intervals, probability scores, etc.
        This requires a statistical framework to quantify uncertainty and make decisions under it.
    
    3. Model Training = Statistical Estimation
        Training an ML model is often about minimizing a loss function, which is analogous to maximum likelihood estimation (MLE) or Bayesian inference in statistics. 
        For example:
            -> Linear Regression: Minimizing squared error (MLE under Gaussian noise)
            -> Logistic Regression: MLE under a Bernoulli likelihood  

Machine Learning Concept	Statistical Equivalent
Training a model	        Estimating parameters
Loss function	            Likelihood/Cost of error
Generalization	            Statistical inference
Model evaluation	        Hypothesis testing / Metrics
Regularization	            Prior belief / Bayesian thinking
'''

'''
# Inference Vs Prediction

'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generating the data. 
x = 10 * np.random.rand(50)
y = 3 * x - 8 + np.random.randn(50) * 4 # y = 2x - 8 + some_randomness.

# Fit a linear regression model.
x = x.reshape(-1, 1)
model = LinearRegression()
mode.fit(x, y)

# Calculate the predicted values. 
y_pred = model.predict(x)
print(y_pred)

# Plot the scatter plot and regresssion lines. 
plt.scatter(x, y, label="Data Points")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Scatter plot with increased variability and regression lines")

# Plot the scatter plot and regression lines. 
x_line = np.linspace(0, 10, 100)
y_actual = 2 * x_line - 5
plt.plot(x_line, y_actual, 'r', label="Population line (m=3, b=-8)")

# Plot the estimated regression line. 
y_estimated = model.coef_[0] * x_line + model.intercept_
plt.plot(x_line, y_estimated, 'g', label=f"Estimated line (m={model.coef_[0]:.2f}, b={model.intercept_:.2f})")

# Add legend and show the plot
plt.legend()
plt.show()

'''
# Most Important Question.
Q. Why Regression Analysis is required ? or Inference Vs Predictions ?

## Inference: Study of the relationships between LPA --> (CGPA, IQ).
    -> Either LPA has a mathematical relationships with (CGPA, or IQ) or not. 
    -> Also, what is the relationships of LPA with CGPA & LPA with IQ. ?

    Examples:- 
    
    Ads Advertisment dataset. 
        
        TV   Internet   Newspaper   Sales
        Internet relationships with Sales
        Newspaper relationships with Sales

## Prediction: 
# For the feature selection, we use the inference. 
'''