document.addEventListener('DOMContentLoaded', function () {
    const dateInput = document.getElementById('date');
    const fromCurrencySelect = document.getElementById('from_currency');
    const toCurrencySelect = document.getElementById('to_currency');
    const fromPrediction = document.getElementById('from-prediction');
    const selectedfromPrediction = document.getElementById('selected-from-prediction');
    const selectedfrom = document.getElementById('selected-from');
    const toPrediction = document.getElementById('to-prediction');
    const selectedtoPrediction = document.getElementById('selected-to-prediction');
    const selectedto = document.getElementById('selected-to');
    const graphContainer = document.getElementById('currency-graph');
    const container = document.getElementById('down-container');
    const name = document.getElementById('name');
    const inputValue = document.getElementById('from-convert');
    const convertValue = document.getElementById('to-convert');
    const fromto = document.getElementById('fromto');
    

    // Function to update the graph and predictions based on the selected date and currencies
    function updateData() {
        const selectedDate = dateInput.value;
        const selectedFromCurrency = fromCurrencySelect.value;
        const selectedToCurrency = toCurrencySelect.value;
        const input = inputValue.value;



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
                inputV: input,
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
            selectedfromPrediction.textContent = data.selectedDate;
            selectedtoPrediction.textContent = data.oneyearDate;
            selectedto.textContent = data.oneyearPrediction;
            selectedfrom.textContent = data.todayPrediction;
            name.textContent = data.currencyCode
            convertValue.textContent = data.result
            fromto.textContent = data.fromto
            
            if (data.oneyearPrediction > data.todayPrediction) {
                container.style.backgroundColor = '#8B0000';
                selectedfromPrediction.style.backgroundColor = 'red';
                selectedtoPrediction.style.backgroundColor = 'red';
                selectedfrom.style.backgroundColor = 'red';
                selectedto.style.backgroundColor = 'red';
            }
            else if(data.oneyearPrediction == data.todayPrediction){
                container.style.backgroundColor = '#daa520';
                selectedfromPrediction.style.backgroundColor = '#ffd700';
                selectedtoPrediction.style.backgroundColor = '#ffd700';
                selectedfrom.style.backgroundColor = '#ffd700';
                selectedto.style.backgroundColor = '#ffd700';

            } 
            
            else {
                container.style.backgroundColor = 'green';
                selectedfromPrediction.style.backgroundColor = '#556B2F';
                selectedtoPrediction.style.backgroundColor = '#556B2F';
                selectedfrom.style.backgroundColor = '#556B2F';
                selectedto.style.backgroundColor = '#556B2F';
            }
            
        })
        .catch(error => console.error('Error fetching prediction data:', error));
    }

    // Listen for changes in the date and currency select boxes
    dateInput.addEventListener('change', updateData);
    fromCurrencySelect.addEventListener('change', updateData);
    toCurrencySelect.addEventListener('change', updateData);
    inputValue.addEventListener('click', updateData);

    // Initialize the graph and predictions with the default values
    updateData();

});
