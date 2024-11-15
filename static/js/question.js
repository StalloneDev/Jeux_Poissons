let timeRemaining = 15; // Temps de départ (en secondes)
let isAnswered = false; // Pour vérifier si la question a été répondue
let timer; // Variable globale pour le timer
let totalElapsedTime = 0; // Variable pour le temps total écoulé
let startTime; // Heure de départ pour chaque question

function startTimer() {
    let timeLeft = timeRemaining;
    isAnswered = false; // Réinitialise le statut de réponse

    startTime = new Date();

    const timerElement = document.getElementById('time-remaining');
    const circle = document.querySelector('#timer circle');
    const circumference = 2 * Math.PI * 18;
    circle.style.strokeDasharray = circumference;

    timer = setInterval(() => {
        console.log(`Temps restant : ${timeLeft}`); // Journal pour voir le temps restant
        if (timeLeft > 0) {
            timeLeft--;
            timerElement.textContent = timeLeft;
            const dashoffset = circumference * (1 - timeLeft / timeRemaining);
            circle.style.strokeDashoffset = dashoffset;
        } else {
            clearInterval(timer);
            console.log("Le temps est écoulé."); // Journal pour vérifier si le temps atteint zéro
            if (!isAnswered) {
                console.log("Aucune réponse sélectionnée. Passage à la question suivante."); // Journal de débogage
                recordElapsedTime();
                showNextQuestion();
            }
        }
    }, 1000);
}

function recordElapsedTime() {
    let endTime = new Date(); // Heure de fin de la question
    let elapsedTime = (endTime - startTime) / 1000; // Temps écoulé en secondes
    totalElapsedTime += elapsedTime; // Ajoute le temps de cette question au total
    console.log(`Temps total écoulé jusqu'à présent : ${totalElapsedTime} secondes`);
}

function showNextQuestion() {
    recordElapsedTime(); // Enregistre le temps écoulé pour cette question
    clearInterval(timer);
    const gameContainer = document.getElementById('game-container');
    let currentQuestionId = parseInt(gameContainer.dataset.currentQuestion);
    let nextQuestionId = currentQuestionId + 1;

    window.location.href = `/question/${nextQuestionId}/`;
}

// Option de sélection pour faire le choix
let selectedOption = null; // Variable pour suivre l'option sélectionnée

function selectOption(optionElement) {
    if (selectedOption) {
        selectedOption.classList.remove('selected');
    }

    optionElement.classList.add('selected');
    selectedOption = optionElement;

    const selectedOptionValue = optionElement.getAttribute('data-option');
    document.getElementById('selected-option').value = selectedOptionValue;

    // Marque la question comme répondue et arrête le timer, mais ne passe pas à la question suivante
    isAnswered = true;
    recordElapsedTime(); // Enregistre le temps écoulé pour cette question
    clearInterval(timer);
    console.log("Réponse sélectionnée, timer arrêté."); // Journal pour confirmer l'arrêt du timer
}

function resetTimer() {
    clearInterval(timer);
    startTimer();
}

// Démarre le timer au début
startTimer();


// Démarre le timer au début
// startTimer();

// let attempts = 0;

// function selectOption(optionElement) {
//     const selectedOption = optionElement.getAttribute('data-option');
//     const correctOption = "{{ question.correct }}";  // Assure-toi que tu passes la réponse correcte depuis le backend

//     if (selectedOption === correctOption) {
//         document.getElementById('selected-option').value = selectedOption;
//         document.getElementById('question-form').submit();
//     } else {
//         attempts += 1;
//         if (attempts >= 2) {
//             window.location.href = "{% url 'end_quiz' score=request.session.get('score', 0) %}";
//         } else {
//             document.getElementById('wrong-answer-popup').style.display = 'block';
//         }
//     }
// }

function closePopup() {
    document.getElementById('wrong-answer-popup').style.display = 'none';
}