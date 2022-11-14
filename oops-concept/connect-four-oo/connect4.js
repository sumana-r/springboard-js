/** Connect Four
 *
 * Player 1 and 2 alternate turns. On each turn, a piece is dropped down a
 * column until a player gets four-in-a-row (horiz, vert, or diag) or until
 * board fills (tie)
 */

//const WIDTH = 7;
//const HEIGHT = 6;

//let  // active player: 1 or 2
//let board = []; // array of rows, each row is array of cells  (board[y][x])

class Game{

  constructor(WIDTH,HEIGHT,p1,p2){
    this.WIDTH = WIDTH;
    this.HEIGHT = HEIGHT;
    this.board = [];
    this.currPlayer = p1;
    this.p1 = p1;
    this.p2 = p2;
    this.finished = false;
  }
  makeBoard(){
    for (let y = 0; y <  this.HEIGHT; y++) {
      this.board.push(Array.from({ length: this.WIDTH }));
    }
  }
  makeHtmlBoard() {
    const board = document.getElementById('board');
  
    // make column tops (clickable area for adding a piece to that column)
    const top = document.createElement('tr');
    top.setAttribute('id', 'column-top');
    var that = this;
    top.addEventListener('click', this.handleClick.bind(this));
  
    for (let x = 0; x < this.WIDTH; x++) {
      const headCell = document.createElement('td');
      headCell.setAttribute('id', x);
      top.append(headCell);
    }
  
    board.append(top);
  
    // make main part of board
    for (let y = 0; y < this.HEIGHT; y++) {
      const row = document.createElement('tr');
  
      for (let x = 0; x < this.WIDTH; x++) {
        const cell = document.createElement('td');
        cell.setAttribute('id', `${y}-${x}`);
        row.append(cell);
      }
  
      board.append(row);
    }
  }
  findSpotForCol(x) {
    for (let y = this.HEIGHT - 1; y >= 0; y--) {
      if (!this.board[y][x]) {
        return y;
      }
    }
    return null;
  }
  placeInTable(y, x) {
    const piece = document.createElement('div');
    piece.classList.add('piece');
    //piece.classList.add(`p${this.currPlayer}`);
    piece.style.top = -50 * (y + 2);
    piece.style.backgroundColor = (this.currPlayer === this.p1)?this.p1.colorName :this.p2.colorName;
  
    const spot = document.getElementById(`${y}-${x}`);
    spot.append(piece);
  }
  endGame(msg) {
    alert(msg);
  }

  handleClick(evt) {
    if(this.finished){
      return;
    }
    // get x from ID of clicked cell
    const x = +evt.target.id;
  
    // get next spot in column (if none, ignore click)
    const y = this.findSpotForCol(x);
    if (y === null) {
      return;
    }
  
    // place piece in board and add to HTML table
    this.board[y][x] = this.currPlayer;
    this.placeInTable(y, x);
    
    // check for win
    if (this.checkForWin()) {
      this.finished = true;
      return this.endGame(`Player ${this.currPlayer.colorName} won!`);
    }
    
    // check for tie
    if (this.board.every(row => row.every(cell => cell))) {
      return this.endGame('Tie!');
    }
      
    // switch players
    this.currPlayer = this.currPlayer === this.p1 ? this.p2 : this.p1;
  }
  checkForWin() {
    function _win(cells) {
      // Check four cells to see if they're all color of current player
      //  - cells: list of four (y, x) cells
      //  - returns true if all are legal coordinates & all match currPlayer
  
      return cells.every(
        ([y, x]) =>
          y >= 0 &&
          y < this.HEIGHT &&
          x >= 0 &&
          x < this.WIDTH &&
          this.board[y][x] === this.currPlayer
      );
    }
  
    for (let y = 0; y < this.HEIGHT; y++) {
      for (let x = 0; x < this.WIDTH; x++) {
        // get "check list" of 4 cells (starting here) for each of the different
        // ways to win
        const horiz = [[y, x], [y, x + 1], [y, x + 2], [y, x + 3]];
        const vert = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]];
        const diagDR = [[y, x], [y + 1, x + 1], [y + 2, x + 2], [y + 3, x + 3]];
        const diagDL = [[y, x], [y + 1, x - 1], [y + 2, x - 2], [y + 3, x - 3]];
  
        // find winner (only checking each win-possibility as needed)
        if (_win.call(this, horiz) || _win.call(this, vert) || 
            _win.call(this, diagDR) || _win.call(this, diagDL)) {
          return true;
        }
      }
    }
  }
  
}

class Player{
  constructor (colorName){
    this.colorName = colorName;
  }
}


function startGame(){
  let p1 = document.getElementById("p1-bcolor").value;
  let p2 = document.getElementById("p2-bcolor").value;

  let makingBoard = new Game(7,6,new Player(p1),new Player(p2));
  makingBoard.makeBoard();
  makingBoard.makeHtmlBoard();
}

let startGameBtn = document.getElementById("strtBtn")
startGameBtn.addEventListener('click',(event) =>{
  startGame();
});
const restartBtn = document.getElementById('restrtBtn');
restartBtn.addEventListener('click',function(event){
  document.getElementById("board").innerText = ""
  startGame();
});
 