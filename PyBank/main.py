#import modules
import pandas as pd
from pathlib import Path

#set path for file
csvpath = Path("budget_data.csv")

# Read in the CSV as a DataFrame
data_csv = pd.read_csv(csvpath)
data_csv.head()

#1The total number of months included in the dataset.
data_csv["Profit/Losses"].count()
86

Total_Months= data_csv["Profit/Losses"].count()
Total_Months
86

#2 The net total amount of Profit/Losses over the entire period.
data_csv["Profit/Losses"].sum()
38382578

NetPnl = data_csv["Profit/Losses"].sum()
38382578

#3 The average of the changes in Profit/Losses over the entire period.
data_csv["Profit/Losses"].mean()
446309.0465116279

data_csv["Profit/Losses"].sum()
data_csv['pnl_changes']=data_csv["Profit/Losses"]- data_csv["Profit/Losses"].shift()
data_csv

   Date    Profit/Losses    pnl_changes
0    Jan-2010    867884    NaN
1    Feb-2010    984655    116771.0
2    Mar-2010    322013    -662642.0
3    Apr-2010    -69417    -391430.0
4    May-2010    310503    379920.0
...    ...    ...    ...
81    Oct-2016    102685    -665765.0
82    Nov-2016    795914    693229.0
83    Dec-2016    60988    -734926.0
84    Jan-2017    138230    77242.0
85    Feb-2017    671099    532869.0
86 rows × 3 columns

Mean_PL= data_csv["pnl_changes"].mean()
Mean_PL
-2315.1176470588234

#4 Greatest Increase in Profits: Feb-2012 ($1926159) --) The max is in the row
data_csv["pnl_changes"].max()
1926159.0

data_csv.loc[data_csv["pnl_changes"] == data_csv["pnl_changes"].max(),'Date']
25    Feb-2012
Name: Date, dtype: object
        
#5 The greatest decrease in losses (date and amount) over the entire period.
data_csv["pnl_changes"].min()
-2196167.0

min_difference= data_csv["pnl_changes"].min()
min_difference
-2196167.0

data_csv.loc[data_csv["pnl_changes"] == data_csv["pnl_changes"].min(),'Date']
44    Sep-2013
Name: Date, dtype: object
        
        
        
        
      print("Financial Analysis")
print("----------------------")
print(f"Total Months: {Total_months}")
print(f"Total: ${NetPnl}")
print(f"Average Change: ${Mean_PL}")
print(f"Greatest Increase in Profits: Feb-2012 $({max_difference})")
print(f"Greatest Decrease in Profits: Sep-2013 $({min_difference})")
Financial Analysis
----------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.1176470588234
Greatest Increase in Profits: Feb-2012 $(1926159.0)
Greatest Decrease in Profits: Sep-2013 $(-2196167.0)
