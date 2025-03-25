#Descriptive statistics for the data set it summerize the data set and provide the following information:
#mean, median, mode, variance, standard deviation, range, minimum, maximum, skewness, kurtosis, percentiles, interquartile range, covariance, correlation, outliers, missing values, frequency distribution, and the central limit theorem
#load library
import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt

data = np.array([12,15,14,10,10,18,21,13,10,16,17,19,20,13
                 ,14,15,10,10,10,10,10,10,10,10,10,10,10,10,10
                 ,])

#mean is the average of a data set
mean = np.mean(data)
print(f"mean: {mean}")

#median is the middle number in a sorted, ascending or descending, list of numbers and can be more descriptive of that data set than the average
median = np.median(data)
print(f"median:{median}")

#mode is the number that appears most frequently in a data set
mode = np.argmax(np.bincount(data))
print(f"Mode:{mode}")

#variance measure of the spread of numbers in a data set
variance = np.var(data)
print(f"variance:{variance}")

#standard deviation is the square root of the variance
standard_deviation = np.std(data)
print(f"standard deviation:{standard_deviation}")

#range is the difference between the maximum and minimum values in a data set
range_data = np.ptp(data)
print(f"range:{range_data}")

#minimum value is the smallest number in a data set
minimum = np.min(data)
print(f"minimum:{minimum}")

#maximum value is the largest number in a data set
maximum = np.max(data)
print(f"maximum:{maximum}")

#skewness is a measure of the asymmetry of the data around the sample mean
skewness = skew(data)
print(f"skewness:{skewness}")

#kurtosis is a measure of the shape of the distribution of data
kurtosis = kurtosis(data)
print(f"kurtosis:{kurtosis}")

#percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than
percentiles = np.percentile(data, 75)
print(f"percentiles:{percentiles}")

#interquartile range is a measure of statistical dispersion, or how scattered, spread out the values in a data set are
interquartile_range = np.percentile(data, 75) - np.percentile(data, 25)
print(f"interquartile range:{interquartile_range}")

#covariance is a measure of the relationship between two sets of data
data_2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
covariance = np.cov(data, data_2)[0][1]
print(f"covariance:{covariance}")

#correlation is a measure of the relationship between two sets of data
correlation = np.corrcoef(data, data_2)
print(f"correlation:{correlation}")

#outliers are numbers in a data set that are significantly higher or lower than the other numbers
outliers = []
for i in data:
    z = (i - mean)/standard_deviation
    if np.abs(z) > 3:
        outliers.append(i)
print(f"outliers:{outliers}")

#missing values are values that are not present in a data set
missing_values = np.isnan(data)
print(f"missing values:{missing_values}")

#frequency distribution is a summary of counting how often values occur within a data set
frequency_distribution = np.bincount(data)
print(f"frequency distribution:{frequency_distribution}")

#centeral limit Theorem
#The central limit theorem states that the distribution of sample averages approaches a normal distribution as the sample size gets larger

sample_means = [np.mean(np.random.randint(1,7,1000)) for _ in range(1000)]
plt.hist(sample_means, bins=11, color='black')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()

#Law of Large numbers
#The law of large numbers states that as a sample size grows, its mean gets closer to the average of the whole population

sample_means = [np.mean(np.random.choice(data,size =i, replace=True)) for i in range(1,1000)]
plt.plot(sample_means)
plt.xlabel('Sample Size')
plt.ylabel('Sample Mean')
plt.show()

#z-score is a measure of how many standard deviations an element is from the mean
z = (data - mean)/standard_deviation
print(f"z-score:{z}")

