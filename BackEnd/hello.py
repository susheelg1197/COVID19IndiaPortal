from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from pandas import DataFrame

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/get-statecount', methods=['GET'])
def get_state_count():
    df = pd.read_csv(r'covid19-in-india\CovidcasesinIndia.csv')
    newDataFrame = DataFrame(df, columns=['Name of State / UT', 'Total Confirmed cases (Indian National)',
                                          'Total Confirmed cases ( Foreign National )', 'Cured/Discharged/Migrated', 'Deaths'])
    newDataFrame.rename(
        columns={"Name of State / UT": "stateOrUnionTerritory",
                 "Total Confirmed cases (Indian National)": "confirmedIndianNational", "Total Confirmed cases ( Foreign National )":
                 "confirmedForeignNational", "Cured/Discharged/Migrated": "cured", "Deaths": "deaths"}, inplace=True)
    
    return newDataFrame.to_json(orient='records')


if __name__ == '__main__':
    app.run()
