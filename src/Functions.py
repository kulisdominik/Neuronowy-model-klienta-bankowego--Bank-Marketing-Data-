import pandas
# import csv
def openFile():
    # with open('bank-additional-full.csv') as fileDataSet:
    #     dataSet = csv.reader(fileDataSet, delimiter=';')
    return pandas.read_csv('bank-additional-full.csv', sep=';')


def getInput():
    dataSet = openFile()
    categories = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m']
    dataSet = dataSet[list(categories)]

    age = pandas.get_dummies(dataSet['age'])
    job = pandas.get_dummies(dataSet['job'])
    marital = pandas.get_dummies(dataSet['marital'])
    education= pandas.get_dummies(dataSet['education'])
    default = pandas.get_dummies(dataSet['default'])
    housing = pandas.get_dummies(dataSet['housing'])
    loan = pandas.get_dummies(dataSet['loan'])
    emp_var_rate = pandas.get_dummies(dataSet['emp.var.rate'])
    cons_price_idx = pandas.get_dummies(dataSet['cons.price.idx'])
    cons_conf_idx = pandas.get_dummies(dataSet['cons.conf.idx'])
    euribor3m = pandas.get_dummies(dataSet['euribor3m'])

    return pandas.concat (
        [age, job, marital, education, default, housing, loan, emp_var_rate, cons_price_idx,cons_conf_idx, euribor3m],
        axis=1
    )


def getOutput():
    dataSet = openFile()
    y = pandas.get_dummies(dataSet['y'])
    return y