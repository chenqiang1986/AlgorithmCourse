# D05 - scikit-learn Feature Engineering
*ML / D05-ScikitLearn-FeatureEngineering*

This folder opens up the preprocessing tools used in [D02-ScikitLearn-LinearRegression](../D02-ScikitLearn-LinearRegression) and shows how to build your own.

## Course Goals

In this module, we will learn:

1. What every scikit-learn transformer has in common (`fit`, `transform`, `fit_transform`), demonstrated by calling `PolynomialFeatures` and `StandardScaler` directly instead of hiding them inside `ColumnTransformer`
2. How to write a custom feature transformer that follows the same contract, so it can drop into any `Pipeline` or `ColumnTransformer`
3. How `PolynomialFeatures` builds curve-fitting terms, and why forgetting to scale them becomes dangerous as the degree grows
4. How `FourierFeatures` (a custom transformer) captures periodic and quasi-periodic patterns, such as Walmart's yearly sales cycle, more effectively than raw polynomial terms
5. How `GroupInteraction` (a custom transformer) lets different slices of the data — such as different stores — learn their own coefficients for the same feature

## Lessons

1. [01-transformer-fit-transform.md](./01-transformer-fit-transform.md)
   Calling `fit`, `transform`, and `fit_transform` by hand on `StandardScaler` and `PolynomialFeatures`, and seeing that `ColumnTransformer` does the exact same thing internally
2. [02-writing-a-custom-transformer.md](./02-writing-a-custom-transformer.md)
   The minimum contract for a custom transformer, a small worked example, and a full read-through of the `FourierFeatures` class
3. [03-polynomial-features-and-scaling.md](./03-polynomial-features-and-scaling.md)
   What `PolynomialFeatures` builds, why unscaled high-order terms destabilize linear regression, and a hands-on experiment that breaks the model at degree 5
4. [04-fourier-features-for-periodicity.md](./04-fourier-features-for-periodicity.md)
   Why periodic data like Walmart's weekly sales needs a periodic basis, how `FourierFeatures` builds one from sine/cosine harmonics, and how it compares to the polynomial model
5. [05-group-interaction-features.md](./05-group-interaction-features.md)
   How `GroupInteraction` gives each group (store) its own coefficients via a one-hot-times-numeric outer product, and the sample-size trade-off that comes with it

More lessons can be added later as the course grows.
