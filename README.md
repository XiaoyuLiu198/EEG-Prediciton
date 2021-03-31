# EEG-Prediciton


1. Introduction

The general purpose of our task is to predict each participant’s age based on the brainwave data received. In this project, we perform an analysis on the data set of EEG signals which contains
brainwave data and age of 1283 participants. We preprocess the raw data in parallel jobs by using the fast Fourier transform method to convert the time series data into frequency domain data, and then
the power spectrum function is further used to obtain the power spectrum components, and the power density of the δ wave, θ wave, α wave, and β wave are obtained by integral calculation. Statistical
models including KNN Regressor, Random Forest Regressor, SVR, and XGBoost Regressor are used for predicting age. The minimum MSE of the best XGBoost Regressor model reaches 48.85.

2. Data

The data we use is EEG for Age Prediction from Kaggle. The data set contains brainwave data and age of 1297 participants which are all in CSV format. EEG is the recording of the electrical
activity of a person’s brain using a series of electrodes positioned strategically around a participant’s head. In this data set, the signals are sampled with the frequency of 250HZ.
We use 1283 files from the data set because the size of other files is larger than 100MB which is beyond the expected size of CHTC input files. The size of each file we used is between 55MB and
100MB.
The first line of each CSV file is the age of the participant. The second line is the names of brainwave signals and tracked data for signals. There are 36 kinds of brainwave signals (some participants have less than 36 signals, but they have at least 24 signals in the CSV files), and each signal is
followed by over 300,000 observations. In general, each column represents a different EEG channel, which can be divided into two types. The last four signals are PHOTIC-REF, IBI, BURSTS, and
SUPPR. They represent photic sneeze reflex, interburst interval, burst, and suppression respectively. The other columns can be classified as a type that is linked with a certain zone in the brain (as the
picture below shows). EEG features change as a function of age and health condition.

3. Extracting feature

We firstly use CHTC to do data pre-processing. The single job will use a CSV file so there are
1283 jobs. Each job requires 1.5 GB as the requested memory. Besides, we use 1 CPU and require
10 GB of disk space. Each job will read a single CSV file and return 6 CSV files as outputs. In this
processing, each job will also return the log files and the error files as the track of the transaction
log and the error if there exist errors in the processing. Each job will take about 20 seconds and the
submission takes about 19 minutes and 31 seconds.
What we want to do is to catch features in each signal channel, so for each sample, we have
24-36 “sub-features” to extract, we want to use the channels every sample has, which means we want
to find the 24 common“sub-features” in every sample, so that data set will not include missing values.
After this, we have 1283 samples(start with new ), each sample is a 24-36 dimensional vector in the
sample space. Then we do dimensionality reduction that we only retain the coordinates which have
the valid feature in all samples, in other words, not be implemented by us. The result should be a
24-dimensional space, which should be our feature space.
To find the feature of each participant, we read several papers about EEG signals. According to
Al Zoubi et al., 2018, EEG signals could be transformed into four types of waves.
Those waves can efficiently represent the activity and features of the brain, which indicates that
the percentage of certain types of waves consisted of all types of waves might reflects age.
