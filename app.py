from flask import Flask, render_template, request , jsonify
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle
from datetime import datetime , timedelta

app = Flask(__name__)

pickle_file_name = "D:\College\SEM-5\ML\ML_PROJECT\datasets\models.pkl"
with open(pickle_file_name, 'rb') as pickle_file:
    models = pickle.load(pickle_file)
    

def make_currency_prediction(date, from_country, to_country):
    
    user_date = pd.to_datetime(date)
    user_features = [user_date.dayofweek, user_date.month, user_date.year]
    
    rf_model = models[from_country][to_country]

    predicted_rate = rf_model.predict([user_features])[0]

    return predicted_rate


# Define the get_flag_symbol function
def get_flag_symbol(currency_code):
    # Map currency codes to emoji flag symbols (you may need to expand this)
    flag_symbols = {
        'AUD' : '🇦🇺',
        'BGN' : '🇧🇬',
        'BRL' : '🇧🇷',
        'CAD' : '🇨🇦',
        'CHF' : '🇨🇭',
        'CNY' : '🇨🇳',
        'CZK' : '🇨🇿',
        'DKK' : '🇩🇰',
        'EUR' : '🇪🇺',
        'GBP' : '🇬🇧',
        'HKD' : '🇭🇰',
        'HRK' : '🇭🇷',
        'HUF' : '🇭🇺',
        'IDR' : '🇮🇩',
        'ILS' : '🇮🇱',
        'INR' : '🇮🇳',
        'ISK' : '🇮🇸',
        'JPY' : '🇯🇵',
        'KRW' : '🇰🇷',
        'MXN' : '🇲🇽',
        'MYR' : '🇲🇾',
        'NOK' : '🇳🇴',
        'NZD' : '🇳🇿',
        'PHP' : '🇵🇭',
        'PLN' : '🇵🇱',
        'RON' : '🇷🇴',
        'RUB' : '🇷🇺',
        'SEK' : '🇸🇪',
        'SGD' : '🇸🇬',
        'THB' : '🇹🇭',
        'TRY' : '🇹🇷',
        'USD' : '🇺🇸',
        'ZAR' : '🇿🇦'
    }
    
    return flag_symbols.get(currency_code, '')  # Return the flag symbol or an empty string if not found

@app.route('/graph', methods=['GET'])
def graph():
    
    file_paths = ["D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\AUD.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\BGN.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\BRL.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\CAD.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\CHF.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\CNY.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\CZK.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\DKK.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\EUR.xlsx", "D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\GBP.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\HKD.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\HRK.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\HUF.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\IDR.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\ILS.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\INR.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\ISK.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\JPY.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\KRW.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\MYR.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\MXN.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\NOK.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\NZD.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\PHP.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\PLN.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\RON.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\RUB.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\SEK.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\SGD.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\THB.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\TRY.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\USD.xlsx","D:\\College\\SEM-5\\ML\\ML_PROJECT\\datasets\\ZAR.xlsx"]
    
    country_names = {'AUD':0,'BGN':1,'BRL':2,'CAD':3,'CHF':4,'CNY':5,'CZK':6,'DKK':7,'EUR':8,'GBP':9,'HKD':10,'HRK':11,'HUF':12,'IDR':13,'ILS':14,'INR':15,'ISK':16,'JPY':17,'KRW':18,'MXN':19,'MYR':20,'NOK':21,'NZD':22,'PHP':23,'PLN':24,'RON':25,'RUB':26,'SEK':27,'SGD':28,'THB':29,'TRY':30,'USD':31,'ZAR':32}

    currency_codes = {
    'INR': 'Indian Rupee',
    'AUD': 'Australian Dollar',
    'BGN': 'Bulgarian Lev',
    'BRL': 'Brazilian Real',
    'CAD': 'Canadian Dollar',
    'CHF': 'Swiss Franc',
    'CNY': 'Chinese Yuan',
    'CZK': 'Czech Koruna',
    'DKK': 'Danish Krone',
    'EUR': 'Euro',
    'GBP': 'British Pound Sterling',
    'HKD': 'Hong Kong Dollar',
    'HRK': 'Croatian Kuna',
    'HUF': 'Hungarian Forint',
    'IDR': 'Indonesian Rupiah',
    'ILS': 'Israeli New Shekel',
    'ISK': 'Icelandic Krona',
    'JPY': 'Japanese Yen',
    'KRW': 'South Korean Won',
    'MXN': 'Mexican Peso',
    'MYR': 'Malaysian Ringgit',
    'NOK': 'Norwegian Krone',
    'NZD': 'New Zealand Dollar',
    'PHP': 'Philippine Peso',
    'PLN': 'Polish Zloty',
    'RON': 'Romanian Leu',
    'RUB': 'Russian Ruble',
    'SEK': 'Swedish Krona',
    'SGD': 'Singapore Dollar',
    'THB': 'Thai Baht',
    'TRY': 'Turkish Lira',
    'USD': 'United States Dollar',
    'ZAR': 'South African Rand'
    }

    
    # Get the selected date
    selected_date = request.args.get('date')
    selected_country = request.args.get('to_currency')
    from_country = request.args.get('from_currency')
    
    exchange_rates = pd.read_excel(file_paths[country_names[from_country]])  # Update with your dataset file\
    #exchange_rates['DATE'] = pd.to_datetime(exchange_rates['DATE'])
    

    # Input dates as strings in the format 'YYYY-MM-DD'
    date1_str = '2023-10-12'
    date2_str = selected_date

    # Convert input strings to datetime objects
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    
    one_month_before = date2 - timedelta(days=30)

# Convert the result back to a string
    one_month_before = one_month_before.strftime("%Y-%m-%d")

    # Calculate the difference between the two dates
    date_difference = date2 - date1

    # Extract the number of days from the date difference
    number_of_days = date_difference.days

    date_list = [date1 + timedelta(days=i) for i in range(1, number_of_days+1)]

    date = []
    
    # Print the list of dates
    for dates in date_list:
        date.append(dates.strftime('%Y-%m-%d'))

    for i in range(0 , number_of_days):
        pred = [date[i], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pred[country_names[selected_country]+1] = make_currency_prediction(date[i], from_country, selected_country)
        new_data = pd.DataFrame([pred], columns=['DATE','AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HRK','HUF','IDR','ILS','INR','ISK','JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON','RUB','SEK','SGD','THB','TRY','USD','ZAR'])
        exchange_rates = pd.concat([exchange_rates, new_data], ignore_index=True)

    
    exchange_rates['DATE'] = pd.to_datetime(exchange_rates['DATE'])
    
    exchange_rates = exchange_rates.sort_values('DATE')
    
    selected_data = exchange_rates[(exchange_rates['DATE'] >= one_month_before) & (exchange_rates['DATE'] <= selected_date)]
    
    fig = px.line(selected_data, x='DATE', y=selected_country)
    new_width = 425  # Set your desired width in pixels
    new_height = 350  # Set your desired height in pixels

# Update the layout with the new width and height
    fig.update_layout(
    title_text= currency_codes[selected_country],  # Set the title text
    title_x=0.5,  # Center the title
    title_font=dict(color='white', size=24)  # Change title color and size
    )
    fig.update_layout(plot_bgcolor='rgba(0,0,0,1)', paper_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(width=new_width, height=new_height)
    
    fig.update_traces(line_color='#aba9a9',line={'width': 3})
    
    fig.update_yaxes(title_text='',tickfont=dict(color='white'),gridcolor='gray') 
    fig.update_xaxes(title_text='',tickfont=dict(color='white'),showgrid=False) 

    return fig.to_json()

@app.route('/')
def index():
    currencies_to = ['INR','AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HRK','HUF','IDR','ILS','ISK','JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON','RUB','SEK','SGD','THB','TRY','USD','ZAR']
    currencies_from = ['USD','AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HRK','HUF','IDR','ILS','INR','ISK','JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON','RUB','SEK','SGD','THB','TRY','ZAR']

    current_date = datetime.now().strftime('%Y-%m-%d')

    # Pass the get_flag_symbol function to the template context
    return render_template('index.html', currencies_from = currencies_from , currencies_to = currencies_to, current_date=current_date, get_flag_symbol=get_flag_symbol)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    selected_date = data['date']
    from_currency = data['from_currency']
    to_currency = data['to_currency']

    # Use the make_currency_prediction function to get the prediction
    prediction = make_currency_prediction(selected_date, from_currency, to_currency)
    prediction = round(prediction, 5)

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)