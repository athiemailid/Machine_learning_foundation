import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from scipy.stats import poisson

#Normal Distribution
#Normal distribution is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean.

sns.histplot(np.random.normal(0, 1, 1000), kde=True)
plt.title('Normal Distribution')
plt.show()

#Binomial Distribution
#Binomial distribution is a probability distribution that summarizes the likelihood that a value will take one of two independent values under a given set of parameters or assumptions.
n,p = 10, 0.5
binom_dist = binom.pmf(np.arange(0, 11), n, p)
plt.bar(np.arange(n+1), binom_dist)
plt.title('Binomial Distribution')
plt.show()

#Poisson Distribution
#Poisson distribution is a probability distribution that shows how many times an event is likely to occur within a specified period of time.

lambda_ = 2
poisson_dist = poisson.pmf(np.arange(0, 10), lambda_)
plt.bar(np.arange(10), poisson_dist)
plt.title('Poisson Distribution')
plt.show()

#Uniform Distribution
#Uniform distribution is a probability distribution that has constant probability.
sns.histplot(np.random.uniform(0, 1, 1000), kde=True)
plt.title('Uniform Distribution')
plt.show()

#Exponential Distribution
#Exponential distribution is a probability distribution that describes the time between events in a Poisson process.
sns.histplot(np.random.exponential(1, 1000), kde=True)
plt.title('Exponential Distribution')
plt.show()

#Log-Normal Distribution
#Log-normal distribution is a probability distribution of a random variable whose logarithm is normally distributed.
sns.histplot(np.random.lognormal(0, 1, 1000), kde=True)
plt.title('Log-Normal Distribution')
plt.show()

#Gamma Distribution
#Gamma distribution is a two-parameter family of continuous probability distributions.
sns.histplot(np.random.gamma(1, 1, 1000), kde=True)
plt.title('Gamma Distribution')
plt.show()

#Beta Distribution
#Beta distribution is a family of continuous probability distributions defined on the interval [0, 1] parameterized by two positive shape parameters.
sns.histplot(np.random.beta(1, 1, 1000), kde=True)
plt.title('Beta Distribution')
plt.show()

#Chi-Square Distribution
#Chi-square distribution is a continuous probability distribution that is widely used in statistics.
sns.histplot(np.random.chisquare(1, 1000), kde=True)
plt.title('Chi-Square Distribution')
plt.show()

#F Distribution
#F distribution is a probability distribution that arises frequently as the null distribution of a test statistic, most notably in the analysis of variance (ANOVA).
sns.histplot(np.random.f(1, 1, 1000), kde=True)
plt.title('F Distribution')
plt.show()

#T Distribution
#T distribution is a probability distribution that is used to estimate population parameters when the sample size is small and/or when the population variance is unknown.
sns.histplot(np.random.standard_t(1, 1000), kde=True)
plt.title('T Distribution')
plt.show()

#Weibull Distribution
#Weibull distribution is a continuous probability distribution named after Waloddi Weibull.
sns.histplot(np.random.weibull(1, 1000), kde=True)
plt.title('Weibull Distribution')
plt.show()

#Cauchy Distribution
#Cauchy distribution is a continuous probability distribution that is used in statistics as the Student's t-distribution.
sns.histplot(np.random.standard_cauchy(1000), kde=True)
plt.title('Cauchy Distribution')
plt.show()

#Laplace Distribution
#Laplace distribution is a continuous probability distribution named after Pierre-Simon Laplace.
sns.histplot(np.random.laplace(0, 1, 1000), kde=True)
plt.title('Laplace Distribution')
plt.show()

#bernoulli Distribution
#Bernoulli distribution is a discrete probability distribution for a random variable that takes the value 1 with probability p and the value 0 with probability q=1-p.
sns.histplot(np.random.binomial(1, 0.5, 1000), kde=True)
plt.title('Bernoulli Distribution')
plt.show()

#Geometric Distribution
#Geometric distribution is a probability distribution that describes the number of trials needed to get the first success in repeated Bernoulli trials.
sns.histplot(np.random.geometric(0.5, 1000), kde=True)
plt.title('Geometric Distribution')
plt.show()

#Hypergeometric Distribution
#Hypergeometric distribution is a discrete probability distribution that describes the number of successes in a sequence of n draws from a finite population without replacement.
sns.histplot(np.random.hypergeometric(10, 5, 3, 1000), kde=True)
plt.title('Hypergeometric Distribution')
plt.show()

#Negative Binomial Distribution
#Negative binomial distribution is a discrete probability distribution that models the number of successes in a sequence of independent and identically distributed Bernoulli trials before a specified (non-random) number of failures occurs.
sns.histplot(np.random.negative_binomial(1, 0.5, 1000), kde=True)
plt.title('Negative Binomial Distribution') 
plt.show()

#Pareto Distribution
#Pareto distribution is a power-law probability distribution that is used in description of social, scientific, geophysical, actuarial, and many other types of observable phenomena.
sns.histplot(np.random.pareto(1, 1000), kde=True)
plt.title('Pareto Distribution')
plt.show()

#Rayleigh Distribution
#Rayleigh distribution is a continuous probability distribution for non-negative-valued random variables.
sns.histplot(np.random.rayleigh(1, 1000), kde=True)
plt.title('Rayleigh Distribution')
plt.show()

#Triangular Distribution
#Triangular distribution is a continuous probability distribution with lower limit a, upper limit b, and mode c, where a ≤ c ≤ b.
sns.histplot(np.random.triangular(0, 0.5, 1, 1000), kde=True)
plt.title('Triangular Distribution')
plt.show()

#Von Mises Distribution
#Von Mises distribution is a continuous probability distribution on the circle.
sns.histplot(np.random.vonmises(0, 1, 1000), kde=True)
plt.title('Von Mises Distribution')
plt.show()

#Wald Distribution
#Wald distribution is a continuous probability distribution that describes the distribution of the time between events in a Poisson process.
sns.histplot(np.random.wald(1, 1, 1000), kde=True)
plt.title('Wald Distribution')
plt.show()

#Zipf Distribution
#Zipf distribution is a discrete probability distribution that is related to the zeta distribution.
sns.histplot(np.random.zipf(1, 1000), kde=True)
plt.title('Zipf Distribution')
plt.show()

#Gumbel Distribution
#Gumbel distribution is a type of probability distribution that is used to model the distribution of the maximum (or the minimum) of a number of samples of various distributions.
sns.histplot(np.random.gumbel(0, 1, 1000), kde=True)
plt.title('Gumbel Distribution')
plt.show()

#Logistic Distribution
#Logistic distribution is a continuous probability distribution that is used to describe growth.
sns.histplot(np.random.logistic(0, 1, 1000), kde=True)
plt.title('Logistic Distribution')
plt.show()

