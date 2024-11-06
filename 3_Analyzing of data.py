#"df.dtype" is used to check data type
#"df.describe(coulumn no)" is used to check mathematical issue or to get statistical summary of data"
# "df.describe(include="all") is used to get a full statistical summary of data i.e, all columns
#"df.info" it provides a concise summary of our dataframe, it basically shows us the top 30 and bottom 30 rows of our dataframe#

import pandas as pd
url="D:/car_evaluation.csv"
df=pd.read_csv(url , header= None)
#print(df.dtypes)
#print(df.describe())
#print(df.describe(include="all"))
print(df.info)

#We see that for object-type columns, a different set of statistics is evaluated, like unique,top and frequency.
#"Unique" is the number of distinct objects in the column,
# "top" is the most frequently occurring object,
#and "freq" is the number of times the top object appears in the column.
#Some values in the table are shown here as "NaN", which stands for "not a number".
#This is because that particular statistical metric cannot be calculated for that specific column data type.

