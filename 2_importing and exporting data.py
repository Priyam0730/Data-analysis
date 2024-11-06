#we can import dataset in csv foramat by using pandas library as "import pandas as pd"
# from this library we have to use "read_csv", "read_jason","read_excel","read_sql" method
# first of all we have to create a variable in which we have to store the location of the file
# after that we have to pass that variable under this method#

import pandas as pd
url="D:/car_evaluation.csv"
df=pd.read_csv(url , header= None)
#print(df)

# simply "df" will print all the data from the dataframe(not recommended for the large datasets)
# insted of this we can use
# df.head(N)   print N rows from the top of dataframe

print(df.head(15));



#df.tail(N)  # print N rows from the bottom of dataframe

# we can also edit the headers
# first of all we have to put all the headers in a seprate variable
# now we use df.colomns= Variable_name
# this will allocate the headers to the dataset #
print("\n\nedited\n\n")
headers = ["a","b","c","d","e","f","g"]
df.columns=headers
print(df.head(5))

#for exporting data in csv format we use "to_csv", "to_jason","to_excel","to_sql" method #
export="D:/edited.csv"
df.to_csv(export)