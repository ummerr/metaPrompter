document.getElementById('prompt-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const userInput = document.getElementById('user-input').value;
    const resultContainer = document.getElementById('result-container');

    // Clear previous results
    resultContainer.innerHTML = '';

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

        if (data.scenes && data.scenes.length > 0) {
            data.scenes.forEach((scene, index) => {
                const sceneCard = document.createElement('div');
                sceneCard.classList.add('scene-card');

                const title = document.createElement('h2');
                title.textContent = `Scene ${index + 1}`;
                sceneCard.appendChild(title);

                const subject = document.createElement('h3');
                subject.textContent = 'Subject:';
                const subjectP = document.createElement('p');
                subjectP.textContent = scene.subject;
                sceneCard.appendChild(subject);
                sceneCard.appendChild(subjectP);

                const action = document.createElement('h3');
                action.textContent = 'Action:';
                const actionP = document.createElement('p');
                actionP.textContent = scene.action;
                sceneCard.appendChild(action);
                sceneCard.appendChild(actionP);

                const description = document.createElement('h3');
                description.textContent = 'Description:';
                const descriptionP = document.createElement('p');
                descriptionP.textContent = scene.scene;
                sceneCard.appendChild(description);
                sceneCard.appendChild(descriptionP);

                const composition = document.createElement('h3');
                composition.textContent = 'Composition:';
                const compositionP = document.createElement('p');
                compositionP.textContent = scene.composition;
                sceneCard.appendChild(composition);
                sceneCard.appendChild(compositionP);

                resultContainer.appendChild(sceneCard);
            });

            const sounds = document.createElement('h2');
            sounds.textContent = 'Sounds:';
            const soundsP = document.createElement('p');
            soundsP.textContent = data.sounds;
            resultContainer.appendChild(sounds);

        } else {
            resultContainer.textContent = 'No scenes were generated.';
        }

    } catch (error) {
        console.error('Error:', error);
        resultContainer.textContent = 'Error generating prompt. See console for details.';
    }
});
