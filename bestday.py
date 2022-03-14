import pandas as pd

data_import = pd.read_csv("RELIANCE.csv",parse_dates=["Date"])
day_mapper = {0 :'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
data_import["DayOfWeek"] = data_import["Date"].map(lambda x:day_mapper[x.dayofweek])
data_import["diff_from_prev_day"] = (data_import["Open"].diff() / data_import["Open"]) *100
final = data_import.groupby("DayOfWeek")["diff_from_prev_day"].mean()
MostDip = final.sort_values(ascending=True)
print(MostDip)