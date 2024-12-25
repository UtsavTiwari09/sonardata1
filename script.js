async function makePrediction() {
    const inputField = document.getElementById("features");
    const resultDiv = document.getElementById("result");
    const features = inputField.value;

    // Clear previous result
    resultDiv.textContent = "";

    if (!features) {
        resultDiv.textContent = "Please enter the features.";
        return;
    }

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ features }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch prediction. Please try again.");
        }

        const data = await response.json();
        const prediction = data.prediction;
        resultDiv.innerHTML = `The object is classified as: <span>${prediction}</span>`;
    } catch (error) {
        console.error(error);
        resultDiv.textContent = "An error occurred. Please check the input format and try again.";
    }
}
