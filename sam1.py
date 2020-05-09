import pandas

df = pandas.read_excel("res1.xlsx")
print(list(set(df[' AC NAME '].values.tolist())))