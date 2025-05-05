let selectedGame = '';
let playerNames = [];
let currentPlayer = 0;
let playerVsComputer = false;
let board = Array(9).fill('');
let ludoPositions = [0, 0];
let currentLudoPlayer = 0;
let snakeLadderPositions = [0, 0]; // Snake and Ladders positions
let snakeLadderBoard = []; // Snake and ladder grid

// Function for Snakes and Ladders initialization
function initSnakes() {
  // Create a board of 100 squares
  snakeLadderBoard = Array(100).fill(0);

  // Define the snake and ladder positions (Sample)
  const snakes = { 16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78 };
  const ladders = { 1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100 };

  // Apply the snakes and ladders
  for (let snake in snakes) {
    snakeLadderBoard[snake - 1] = -Math.abs(snakes[snake] - (snake - 1)); // Snake moves backwards
  }
  for (let ladder in ladders) {
    snakeLadderBoard[ladder - 1] = Math.abs(ladders[ladder] - (ladder - 1)); // Ladder moves forward
  }

  // Show the initial position of the players
  document.getElementById('snakesPosition').innerText = `Player 1 is on square 1.`;
  document.getElementById('snakesCanvas').style.display = 'block';
  document.getElementById('snakes').style.display = 'block';
}

// Dice roll for Snakes & Ladders
function rollDiceSnakes() {
  const roll = Math.ceil(Math.random() * 6);
  snakeLadderPositions[currentPlayer] += roll;

  // Handle snake or ladder
  let move = snakeLadderBoard[snakeLadderPositions[currentPlayer] - 1] || 0;
  snakeLadderPositions[currentPlayer] += move;

  if (snakeLadderPositions[currentPlayer] >= 100) {
    showWinner(`Player ${currentPlayer + 1}`);
    return;
  }

  // Update player position on canvas
  document.getElementById('snakesPosition').innerText = `Player ${currentPlayer + 1} is on square ${snakeLadderPositions[currentPlayer]}`;
  drawSnakesAndLaddersBoard();
  currentPlayer = (currentPlayer + 1) % playerNames.length;
}

function drawSnakesAndLaddersBoard() {
  const canvas = document.getElementById('snakesCanvas');
  const ctx = canvas.getContext('2d');
  const cellSize = 40;
  const boardSize = 10;

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#111';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = '#fff';

  // Draw the grid
  for (let i = 0; i < boardSize; i++) {
    for (let j = 0; j < boardSize; j++) {
      ctx.strokeRect(j * cellSize, i * cellSize, cellSize, cellSize);
    }
  }

  // Draw player tokens (representing players on the board)
  const colors = ['red', 'blue'];
  for (let i = 0; i < snakeLadderPositions.length; i++) {
    const pos = snakeLadderPositions[i];
    const row = Math.floor(pos / boardSize);
    const col = pos % boardSize;
    ctx.beginPath();
    ctx.arc(col * cellSize + 20, row * cellSize + 20, 10, 0, Math.PI * 2);
    ctx.fillStyle = colors[i];
    ctx.fill();
  }
}

// Function to select a game
function selectGame(game) {
  selectedGame = game;
  document.getElementById('gameSelectionPopup').style.display = 'none';
  showModeSelection(game);
}

function showModeSelection(game) {
  const modePopup = document.getElementById('modeSelectionPopup');
  const modeButtons = document.getElementById('modeButtons');
  modeButtons.innerHTML = '';

  if (game === 'ticTacToe' || game === 'snakes') {
    ['1 Player', '2 Player'].forEach(mode => {
      const btn = document.createElement('button');
      btn.textContent = mode;
      btn.onclick = () => askNames(mode.startsWith('1') ? 1 : 2);
      modeButtons.appendChild(btn);
    });
  } else if (game === 'ludo') {
    [2, 3, 4].forEach(players => {
      const btn = document.createElement('button');
      btn.textContent = `${players} Players`;
      btn.onclick = () => askNames(players);
      modeButtons.appendChild(btn);
    });
  }

  modePopup.style.display = 'block';
}

// Function to ask for player names and set game mode
function askNames(numPlayers) {
  document.getElementById('modeSelectionPopup').style.display = 'none';
  const inputArea = document.getElementById('nameInputs');
  inputArea.innerHTML = '';
  playerNames = [];
  playerVsComputer = numPlayers === 1;

  for (let i = 0; i < numPlayers; i++) {
    const input = document.createElement('input');
    input.placeholder = `Player ${i + 1} Name`;
    inputArea.appendChild(input);
  }

  document.getElementById('nameInputPopup').style.display = 'block';
}

// Function to start the selected game
function launchGame() {
  const inputs = document.querySelectorAll('#nameInputs input');
  playerNames = Array.from(inputs).map(input => input.value || `Player`);

  if (playerVsComputer) playerNames.push("Computer");

  document.getElementById('nameInputPopup').style.display = 'none';
  document.querySelectorAll('.game-container').forEach(div => div.style.display = 'none');

  if (selectedGame === 'ticTacToe') {
    document.getElementById('ticTacToe').style.display = 'block';
    startTicTacToe();
  } else if (selectedGame === 'snakes') {
    initSnakes(); // Now initializing the Snakes and Ladders game
  } else if (selectedGame === 'ludo') {
    document.getElementById('ludo').style.display = 'block';
    drawLudoBoard();
  }
}

// Reset the game and show game selection screen
function resetGame() {
  document.getElementById('winnerPopup').style.display = 'none';
  document.getElementById('gameSelectionPopup').style.display = 'flex';
  document.querySelectorAll('.game-container').forEach(div => div.style.display = 'none');
}
