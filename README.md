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
followed by over 300,000 observations.

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
After this, we have 1283 samples, each sample is a 24-36 dimensional vector in the
sample space. Then we do dimensionality reduction that we only retain the coordinates which have
the valid feature in all samples, in other words, not be implemented by us. The result should be a
24-dimensional space, which should be our feature space.

4. Machine Learning

To choose proper features among the features we extracted as mentioned above, we calculated the
Pearson correlation of Features and drew the scatter plots of the data set. From the Pearson correlation
between alpha wave and age, we notice that more than 4 signal channels’ correlation coefficients
between age are larger than 0.1.We also noticed that the wave index from signal channels
are very likely to be linearly related, which indicates that we need to solve the linearity between
variables.
Among those features, we chose the power density of θ wave, the power density of α wave, and
entropy for further research according to the plots and research from Kanokwan.etl, 2019.
We applied PCA to eliminate the linearity between explanatory variables(namely the value in
different signal channels). Then we tried five types of models to predict the age of a participant this
time. To obtain optimal hyperparameter, we use the grid-search method to calculate the accuracy
of a different combination of hyperparameters on split sets.The metric we chose is mean
squared error(denoted as MSE), which can reflect the difference between our prediction and the true
value.


