# Currency-Predictor

## Overview
The **Currency Rate Predictor** involves predicting currency rates for 33 different countries using a Random Forest model. The data has been extracted from the Free Currency API, and the prediction includes both individual country rates and conversion rates between countries.

## Data Source
Data has been collected using the Free Currency API. The dataset consists of 33 files, each corresponding to a specific country.It consist of last one year data(From: 01-01-2023 To: 31-12-2023).  

## Currency Codes and Full Forms
- **AUD:** Australian Dollar
- **BGN:** Bulgarian Lev
- **BRL:** Brazilian Real
- **CAD:** Canadian Dollar
- **CHF:** Swiss Franc
- **CNY:** Chinese Yuan
- **CZK:** Czech Koruna
- **DKK:** Danish Krone
- **EUR:** Euro
- **GBP:** British Pound Sterling
- **HKD:** Hong Kong Dollar
- **HRK:** Croatian Kuna
- **HUF:** Hungarian Forint
- **IDR:** Indonesian Rupiah
- **ILS:** Israeli New Shekel
- **INR:** Indian Rupee
- **ISK:** Icelandic Króna
- **JPY:** Japanese Yen
- **KRW:** South Korean Won
- **MXN:** Mexican Peso
- **MYR:** Malaysian Ringgit
- **NOK:** Norwegian Krone
- **NZD:** New Zealand Dollar
- **PHP:** Philippine Peso
- **PLN:** Polish Złoty
- **RON:** Romanian Leu
- **RUB:** Russian Ruble
- **SEK:** Swedish Krona
- **SGD:** Singapore Dollar
- **THB:** Thai Baht
- **TRY:** Turkish Lira
- **USD:** United States Dollar
- **ZAR:** South African Rand

## Model Performance
The model has been trained using a Random Forest algorithm and stored in Pickle file. Evaluation metrics such as Mean Absolute Error (MAE) or Mean Squared Error (MSE) have been used to assess the model's accuracy.

## Project Structure
- `data/`: Contains the datasets for each country.
- `src/`: Includes the Python code for Prediction.
- `models/`: Stores the trained Random Forest model.
- `notebooks/`: Jupyter notebooks for data extraction, exploratory data analysis and model development.

## Note
I have not given the models.pkl file.Run the colab for the models.pkl file

## Dependencies
Ensure you have the necessary dependencies installed(for colab). You can use the following command to install them:

```bash
pip install -r requirements.txt
```

## Image Gallery
![Alt Text](https://github.com/ParthaSarathi-23/Currency-Predictor/blob/main/image/img-1.jpg?raw=true)
![Alt Text](https://github.com/ParthaSarathi-23/Currency-Predictor/blob/main/image/img-2.jpg?raw=true)
![Alt Text](https://github.com/ParthaSarathi-23/Currency-Predictor/blob/main/image/img-3.jpg?raw=true)
![Alt Text](https://github.com/ParthaSarathi-23/Currency-Predictor/blob/main/image/img-4.jpg?raw=true)
