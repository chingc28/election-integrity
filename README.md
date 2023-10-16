# Election Integrity

## Purpose

Fair election for all eligible citizens of voting age is the most integral part of a democratic society, it is the foundation in which democracy is bulit on. When the integrity of an election is threatened, including tactics such as:
- voter suppression
- falsifying voter ballots
- tempering voter ballots
- additional methods of election manipulation to prevent a fair and just result,

the foundation of our democracy becomes at risk. The purpose of this project is to address one area of election fraud, which is falsifying voter ballots to influence electoral outcomes. This can be through increasing votes of a favored candidate, decreasing votes of an opposing candidate, or falsely reporting the results. Though not a perfect solution due to the complexity of the problem, the hope is that this method provides additional insights to help maintain the trust and confidence of voters on the democratic system 

## Code 

This project is coded in Python with matplotlib for graphical generation.
Input should be in CSV format

## Method 

Some people may be familiar with Benford's law being used to prove or disprove whether an election is tempered. Infamously, Benford's law was used to undermine the integrity of the 2020 Presidential Election in the United States. It is a mathematical law that describes the phenomenon of naturally occurring set of numbers: The first digit of these numbers are not evenly distributed and follows a pattern where '1' is the first digit 30% of the time, '2' appears 17.6% of the time, and so on. It's commonly used in the finance sphere to detect if something doesn't seem right. It has since been [disproved](https://www.reuters.com/article/uk-factcheck-benford/fact-check-deviation-from-benfords-law-does-not-prove-election-fraud-idUSKBN27Q3AI) by various scholars and mathematicians that deviation from Benford's law in election results meant fraudulent election activities.

This project's method will not be applying Benford's law to detect numerical anomalies. Instead, mean-squared-error analysis will be used in conjunction with patterns of random numbers within a dataset.

In a set of randomly generated numbers, the digits in the one's and ten's place of the dataset have a uniform distribution. Meaning, each number (0-9) have equal chances of appearing in the one's or ten's place. So ideally, each number constitutes 10% of the one's/ten's in the entire dataset. Humans aren't very good at generating random numbers because of our ability to follow/create patterns either consciously or unconsciously. More information on this can be found [here](https://www.random.org/analysis/). Using this reasoning, several steps would be used to analyze the likelihood of fraudulent election results.

- Creation of histogram to showcase frequencies of each digit within the dataset in comparison to ideal graph (horizontal line, each digit is at 10%). It should show frequencies of separate datasets containing 10 to 10,000 random numbers. Dataset with 10,000 random numbers should most closely resemble the ideal graph.
- 10,000 datasets would have randomly generated numbers matching the number of datapoints in the input data.
- Mean-squared-error (MSE) of these 10,000 datasets would be calculated against the uniform distribution created AND against MSE of input data.
- Calculate the number of datapoints greater than MSE of input data and outputs confidence level of fraudulent election data

## Example 

The 2009 election in the country of Iran is used as an example input. This can be changed by simply changing the name of the input csv name into the desired csv. 

## How to use 

Clone the repository into a folder with the desired csv file.
