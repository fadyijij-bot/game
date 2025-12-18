const targetTextDiv = document.getElementById('target-text');
const inputBox = document.getElementById('input-box');
const car = document.getElementById('car');
const progressSpan = document.getElementById('progress');

let targetText = "";
let lastValidValue = ""; 

function fetchNewSentence() {
    fetch('/get_sentence')
        .then(response => response.json())
        .then(data => {
            targetText = data.text.trim();
            targetTextDiv.innerText = targetText;
            inputBox.value = "";
            lastValidValue = ""; 
            car.style.left = "0%";
            progressSpan.innerText = "0";
            inputBox.focus();
        });
}

fetchNewSentence();

inputBox.addEventListener('input', () => {
    const currentInput = inputBox.value;
    
    // فحص لو الحروف صح
    if (targetText.startsWith(currentInput)) {
        lastValidValue = currentInput;
        let progress = (currentInput.length / targetText.length) * 100;
        car.style.left = Math.min(progress, 90) + "%";
        progressSpan.innerText = Math.round(progress);
    } else {
        // لو غلط يمسح الحرف الغلط فوراً
        inputBox.value = lastValidValue;
    }

    if (inputBox.value === targetText) {
        setTimeout(() => {
            alert("عاش يا بطل! 🏆");
            fetchNewSentence();
        }, 100);
    }
});