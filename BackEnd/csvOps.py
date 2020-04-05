import pandas as pd
from pandas import DataFrame

df = pd.read_csv(r'covid19-in-india\covid_19_india.csv')

newDataFrame = DataFrame(df, columns=['State/UnionTerritory', 'ConfirmedIndianNational',
                                      'ConfirmedForeignNational', 'Cured', 'Deaths'])
GroupedByState = newDataFrame.groupby(
    ['State/UnionTerritory']).sum().reset_index()
GroupedByState.rename(
    columns={"State/UnionTerritory": "stateOrUnionTerritory",
             "ConfirmedIndianNational": "confirmedIndianNational", "ConfirmedForeignNational":
             "confirmedForeignNational", "Cured": "cured", "Deaths": "deaths"}, inplace=True)
print(GroupedByState.to_json(orient='records'))
