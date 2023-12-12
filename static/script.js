document.addEventListener('DOMContentLoaded', function () {
    const dateInput = document.getElementById('date');
    const fromCurrencySelect = document.getElementById('from_currency');
    const toCurrencySelect = document.getElementById('to_currency');
    const fromPrediction = document.getElementById('from-prediction');
    const toPrediction = document.getElementById('to-prediction');
    const graphContainer = document.getElementById('currency-graph');

    // Function to update the graph and predictions based on the selected date and currencies
    function updateData() {
        const selectedDate = dateInput.value;
        const selectedFromCurrency = fromCurrencySelect.value;
        const selectedToCurrency = toCurrencySelect.value;

        // Update the graph based on the selected date and currencies
        fetch(`/graph?date=${selectedDate}&from_currency=${selectedFromCurrency}&to_currency=${selectedToCurrency}`)
            .then(response => response.json())
            .then(data => {
                Plotly.react(graphContainer, data.data, data.layout);
            })
            .catch(error => console.error('Error fetching graph data:', error));

        // Make a request to the /predict endpoint for currency prediction
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                date: selectedDate,
                from_currency: selectedFromCurrency,
                to_currency: selectedToCurrency,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Update predictions based on the response
            fromPrediction.textContent = `1`;
            toPrediction.textContent = data.prediction;
            
        })
        .catch(error => console.error('Error fetching prediction data:', error));
    }

    // Listen for changes in the date and currency select boxes
    dateInput.addEventListener('change', updateData);
    fromCurrencySelect.addEventListener('change', updateData);
    toCurrencySelect.addEventListener('change', updateData);

    // Initialize the graph and predictions with the default values
    updateData();
});
