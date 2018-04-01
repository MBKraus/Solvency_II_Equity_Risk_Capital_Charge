
# Python script for calculating the (type I) equity risk solvency capital charge ("SCR") under Solvency II

Python script which sources price data from Yahoo Finance for each of the OECD / EEA indices in the global index as stipulated by EOIPA. In turn, this script calculates the global index (along pre-defined weights) and the corresponding symmetric adjustment under Solvency II.
This symmetric adjustment has been put in place by EOIPA in order to mitigate pro-cyclical market effects in equity market risks.
This adjustment is applied to the standard solvency II charge for Type I equities (39%) - whilst keeping in mind the upper and lower limit of the SCR for Type I equities (i.e. 29% and 49%).

NB

- The Polish WIG30 index has not been included in the global index as Yahoo Finance does not offer historic data series for this index
- Please refer to the following [link](https://eiopa.europa.eu/regulation-supervision/insurance/solvency-ii-technical-information/symmetric-adjustment-of-the-equity-capital-charge) for additional background on the symmetric adjustment of the Solvency II equity capital charge

Please note - this script requires the following packages / modules in order to function properly:

- [Python 3.5.1](https://www.python.org/downloads/release/python-351/)
- [Matplotlib](https://matplotlib.org/)
- [Pandas](https://pandas.pydata.org/)

#### Type I Equity Risk Solvency Capital Charge ("SCR")
![alt text](https://github.com/Weesper1985/Solvency_II_Equity_Risk_Capital_Charge/blob/master/scr.png)


#### Price - Global Index
![alt text](https://github.com/Weesper1985/Solvency_II_Equity_Risk_Capital_Charge/blob/master/globalindex.png)

