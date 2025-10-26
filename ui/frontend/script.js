document.getElementById('prompt-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const userInput = document.getElementById('user-input').value;
    const resultContainer = document.getElementById('result-container');
    const promptOutput = document.getElementById('prompt-output');

    try {
        const response = await fetch('http://127.0.0.1:8000/generate-prompt/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: userInput }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        promptOutput.textContent = JSON.stringify(data, null, 2);
        resultContainer.style.display = 'block';

    } catch (error) {
        console.error('Error:', error);
        promptOutput.textContent = 'Error generating prompt. See console for details.';
        resultContainer.style.display = 'block';
    }
});
