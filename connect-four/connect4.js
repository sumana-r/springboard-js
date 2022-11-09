/** Connect Four
 *
 * Player 1 and 2 alternate turns. On each turn, a piece is dropped down a
 * column until a player gets four-in-a-row (horiz, vert, or diag) or until
 * board fills (tie)
 */

var WIDTH = 7;
var HEIGHT = 6;

var currPlayer = 1; // active player: 1 or 2
var board = []; // array of rows, each row is array of cells  (board[y][x])

/** makeBoard: create in-JS board structure:
 *    board = array of rows, each row is array of cells  (board[y][x])
 */

function makeBoard(){ 
  // TODO: set "board" to empty HEIGHT x WIDTH matrix array
  //form 2D array using the height and width with the help map method.
  // added the elementsto the board using push method
  Array.from({length:HEIGHT}).map(()=>{ 
    board.push(Array.from({length:WIDTH}));
    
  });

}
  /** makeHtmlBoard: make HTML table and row of column tops. */

function makeHtmlBoard() {
  // TODO: get "htmlBoard" variable from the item in HTML w/ID of "board"
  const htmlBoard = document.getElementById('board');
  // TODO: add comment for this code
  // creating the row with the id is column-top
  var top = document.createElement("tr");
  top.setAttribute("id", "column-top");
  // calling the function handleClick by clicking the row with the id is column-top
  top.addEventListener("click", handleClick);

  for (var x = 0; x < WIDTH; x++) {
    var headCell = document.createElement("td");
    headCell.setAttribute("id", x);
    top.append(headCell);
  }
  htmlBoard.append(top);

  // TODO: add comment for this code
  for (var y = 0; y < HEIGHT; y++) {
    const row = document.createElement("tr");
    for (var x = 0; x < WIDTH; x++) {
      const cell = document.createElement("td");
      cell.setAttribute("id", `${y}-${x}`);
      row.append(cell);
    }
    htmlBoard.append(row);
  }
}

/** findSpotForCol: given column x, return top empty y (null if filled) */

function findSpotForCol(x) {
  // TODO: write the real version of this, rather than always returning 0
  // get the board array length and assign length value -1 as board index 
  // to find row value using column value(x)
  for (let row = board.length - 1; row >= 0; row--) {
    if (!board[row][x]) {
        return row;
    }
  }
  return null;
}

/** placeInTable: update DOM to place piece into HTML table of board */

function placeInTable(y, x) {
  // TODO: make a div and insert into correct table cell
  //create div element to fill the player1(red) and player2(blue) 
  // the piece is dropped in the unoccupied place from last index 
  const pieceDiv = document.createElement("div");
  pieceDiv.classList.add('piece',`player${currPlayer}`);
  const gameBrd = document.getElementById(y + '-' + x);
  gameBrd.append(pieceDiv);
}

/** endGame: announce game end */

function endGame(msg) {
  // TODO: pop up alert message
  alert(msg)
}

/** handleClick: handle click of column top to play piece */

function handleClick(evt) {
  // get x from ID of clicked cell
  var x = +evt.target.id;
  
  // get next spot in column (if none, ignore click)
  var y = findSpotForCol(x);
  
  if (y === null) {
    return;
  }

  // place piece in board and add to HTML table
  // TODO: add line to update in-memory board
  placeInTable(y, x);
  board[y][x] = currPlayer;

  // check for win
  if (checkForWin()) {
    return endGame(`Player ${currPlayer} won!`);
  }

  // check for tie
  // TODO: check if all cells in board are filled; if so call, call endGame
  const tieGame = board.every((rowVal)=>{
   return rowVal.every((cell)=> { return cell})});
  if(tieGame){
    return endGame('Tie!');
  }
  

  // switch players
  // TODO: switch currPlayer 1 <-> 2
  currPlayer = (currPlayer === 1 )? 2 :  1;

}

/** checkForWin: check board cell-by-cell for "does a win start here?" */

function checkForWin() {
  function _win(cells) {
    // Check four cells to see if they're all color of current player
    //  - cells: list of four (y, x) cells
    //  - returns true if all are legal coordinates & all match currPlayer

    return cells.every(
      ([y, x]) =>
        y >= 0 &&
        y < HEIGHT &&
        x >= 0 &&
        x < WIDTH &&
        board[y][x] === currPlayer
    );
  }

  // TODO: read and understand this code. Add comments to help you.
  //  iterate the row and column of the array  in the loop 
  // get the horizontal,vertical, diagonal value in separate global array
  // check if each horiz, vert, diagDR, diagDl passing into the -win function
  // return true if any one condition is true
  

  for (var y = 0; y < HEIGHT; y++) {
    for (var x = 0; x < WIDTH; x++) {
      var horiz = [[y, x], [y, x + 1], [y, x + 2], [y, x + 3]];
      var vert = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]];
      var diagDR = [[y, x], [y + 1, x + 1], [y + 2, x + 2], [y + 3, x + 3]];
      var diagDL = [[y, x], [y + 1, x - 1], [y + 2, x - 2], [y + 3, x - 3]];

      if (_win(horiz) || _win(vert) || _win(diagDR) || _win(diagDL)) {
        return true;
      }
    }
  }
}

makeBoard();
makeHtmlBoard();
