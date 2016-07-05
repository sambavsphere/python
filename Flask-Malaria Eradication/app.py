from flask import Flask, render_template, jsonify
from stock_scraper import get_data
import os
import pandas as pd 

app = Flask(__name__)


@app.route("/data")
def data():
    return jsonify(get_data())

@app.route("/")
def index():
	return render_template('index1.html')
@app.route("/statistics/")
def statistics():
	data=pd.read_csv('xmart.csv')
	data=data.describe()
	return data.to_html()


@app.route("/treemap/")
def treemap():
	data=pd.read_csv('xmart.csv')
	data_group_year_values=list(data.groupby('YEAR').sum()['Numeric'].values)
	data_group_year_index=list(data.groupby('YEAR').sum().index)
	return render_template('treemap.html',data=data,data_group_year_values=data_group_year_values)


@app.route("/multistacked/")
def multistacked():
	data=pd.read_csv('xmart.csv')
	data_group_year_values=list(data.groupby('YEAR').sum()['Numeric'].values)
	data_group_year_index=list(data.groupby('YEAR').sum().index)

	return render_template('multistacked.html',data=data,data_group_year_values=data_group_year_values)

@app.route("/bar/")
def bar():
	data=pd.read_csv('xmart.csv')
	data_group_year_values=list(data.groupby('YEAR').sum()['Numeric'].values)
	data_group_year_index=list(data.groupby('YEAR').sum().index)

	return render_template('barchart.html',data_group_year_values=data_group_year_values,data_group_year_index=data_group_year_index,data=data)
    #return render_template("index.html")
@app.route("/circle/")
def circle():
	data=pd.read_csv('xmart.csv')
	data_group_country_values=list(data.groupby('COUNTRY').sum()['Numeric'].dropna().values)
	data_group_country_index=list(data.groupby('COUNTRY').sum().index)

	return render_template('circle.html',data_group_country_values=data_group_country_values,data_group_country_index=data_group_country_index,data=data)

@app.route("/scaterplot/")
def scater():
	data=pd.read_csv('xmart.csv')
	data_group_year_values=list(data.groupby('YEAR').sum()['Numeric'].values)
	data_group_year_index=list(data.groupby('YEAR').sum().index)
	data=[[i,j] for (i,j) in zip(data_group_year_values,range(2000,2014))]

	return render_template('scaterplot.html',data=data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
