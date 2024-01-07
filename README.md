# Currency-Predictor

## Overview
The currency rate predictor involves predicting currency rates for 32 different countries using a Random Forest model. The data has been extracted from the Free Currency API, and the prediction includes both individual country rates and conversion rates between countries.

## Data Source
Data has been collected using the Free Currency API. The dataset consists of 32 files, each corresponding to a specific country, with 100 rows and 32 columns. 

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

## Project Structure
- `data/`: Contains the datasets for each country.
- `src/`: Includes the Python code for data extraction, preprocessing, model training, and evaluation.
- `models/`: Stores the trained Random Forest model.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model development.

## Dependencies
Ensure you have the necessary dependencies installed. You can use the following command to install them:

```bash
pip install -r requirements.txt
