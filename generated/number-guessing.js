let numberToGuess = Math.floor(Math.random() * 100) + 1;
let guessCount = 0;

while (true) {
  let userGuess = prompt("Guess a number between 1 and 100:");
  guessCount++;

  if (isNaN(userGuess)) {
    alert("Invalid input. Please enter a number.");
    continue;
  }

  if (parseInt(userGuess) < numberToGuess) {
    alert("Too low! Try again.");
  } else if (parseInt(userGuess) > numberToGuess) {
    alert("Too high! Try again.");
  } else {
    alert(`Congratulations! You guessed the number in ${guessCount} attempts.`);
    break;
  }
}
