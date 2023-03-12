import pandas as pd

#get csv file from url
url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/' \
      'raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
#use pandas to read the files
df = pd.read_csv(url)

#method to delete outliers from data
def delOutliers(data):
    #define column counter
    i = 0
    #4 columns of calculatable data
    while i < 4:
        #iterate through every column
        #calculate mean & deviation
        mean = data[data.columns[i]].mean()
        std = data[data.columns[i]].std()
        #iterate through every element in column
        for index, row in data.iterrows():
            #if element = outlier, then delete the row
            if row[data.columns[i]] < mean - 2*std or row[data.columns[i]] > mean + 2*std:
                data.drop(index, inplace=True)
                #update counter
        i+=1
        #return new dataframe
    return data

#method for calculating ratios and inserting them into dataframe
def insertRatioColumns(data):
    sepalR = data['sepal_width']/data['sepal_length']
    petalR = data['petal_width']/data['petal_length']
    sepalR = sepalR.round(2)
    petalR = petalR.round(2)
    data.insert(data.columns.get_loc('sepal_width'),
                'sepal_ratio',sepalR)
    data.insert(data.columns.get_loc('petal_width'),
                'petal_ratio', petalR)
    #defining additional id column and making it as the first column
    data['id'] = list(range(1,len(data)+1))
    #print(data['id'])
    first_column = data.pop('id')
    data.insert(0, 'id', first_column)
    return data

#new data without outliers + added ratio columns
newdata = insertRatioColumns(delOutliers(df))




