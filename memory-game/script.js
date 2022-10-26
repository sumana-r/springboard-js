const gameContainer = document.getElementById("game");

const COLORS = [
  "red",
  "blue",
  "green",
  "orange",
  "purple",
  "red",
  "blue",
  "green",
  "orange",
  "purple"
];

// here is a helper function to shuffle an array
// it returns the same array with values shuffled
// it is based on an algorithm called Fisher Yates if you want ot research more
function shuffle(array) {
  let counter = array.length;

  // While there are elements in the array
  while (counter > 0) {
    // Pick a random index
    let index = Math.floor(Math.random() * counter);

    // Decrease counter by 1
    counter--;

    // And swap the last element with it
    let temp = array[counter];
    array[counter] = array[index];
    array[index] = temp;
  }

  return array;
}
let score = 0;

//let shuffledColors = ;


// this function loops over the array of colors
// it creates a new div and gives it a class with the value of the color
// it also adds an event listener for a click for each card
function createDivsForColors(colorArray) {
  
  for (let color of colorArray) {
    // create a new div
    const newDiv = document.createElement("div");

    // give it a class attribute for the value we are looping over
    newDiv.classList.add('clickhold');
    newDiv.classList.add(color);
    newDiv.classList.add('card');
    newDiv.setAttribute("color",color);

      newDiv.addEventListener("click", function(event) {
       handleCardClick(event);
     
  });

    // append the div to the element with an id of game
    gameContainer.append(newDiv);
   

    
    //localStorage.setItem("bestScore",)
    
  }
  
}

// TODO: Implement this function!
function handleCardClick(event) {
  
  // you can use event.target to see which element was clicked
  //console.log("you just clicked", event.target);
  if(event.target.classList.contains('selected')|| event.target.classList.contains('matched') ){
    
    return;
  }
    let scoreVal = ++score;
    document.getElementById("game-score").innerText = scoreVal;
   
  
  
  const divColorAttr = event.target.getAttribute('color');
  console.log("you just clicked", divColorAttr);
  const openCard = document.querySelector('.selected');
  
  event.target.classList.add('selected');
 
  if(openCard != null){
    const colorAttr = openCard.getAttribute('color');
    if(colorAttr == divColorAttr){
      openCard.classList.add('matched');
      event.target.classList.add('matched');
      openCard.classList.remove('selected');
      event.target.classList.remove('selected'); 
      if(document.querySelectorAll(".matched").length == document.querySelectorAll(".card").length){
        bestScore(document.getElementById("game-score").innerText);
      }
      
    }
    else{
       const cardHolder = document.querySelectorAll('.card');
       cardHolder.forEach(element =>{
        element.classList.add('clickhold');
       })
       
      const myTargetTimeout = setTimeout(function(){
        openCard.classList.remove('selected');
        event.target.classList.remove('selected'); 
        rmvCardHolds();
      },1000);
           
    }
    

  }
  
  /*if(!openCard){
    const colorAttr = openCard.getAttribute('color');
    if(colorAttr == divColorAttr){
     console.log("matched");
    }
  }*/
    

  
}
const startBtn = document.getElementById('btn-start');
startBtn.addEventListener('click',function(event){
  
  // give it a class attribute for the value we are looping over
  rmvCardHolds();
 });

// when the DOM loads
createDivsForColors(shuffle(COLORS));

const restartBtn = document.getElementById('btn-restart');
restartBtn.addEventListener('click',function(event){
    const gameCntr= document.getElementById('game');
    gameCntr.innerText = "";
    document.getElementById("game-score").innerText = 0;
    score = 0; 
    createDivsForColors(shuffle(COLORS));
    rmvCardHolds();
  });
  
  function rmvCardHolds(){
    const cardHolds = document.querySelectorAll('.clickhold');
    cardHolds.forEach(element => {
      element.classList.remove('clickhold');
    });
  
  }


 function bestScore(score){
  console.log(score);
  score = score - 0;
 
    let curBestScore = localStorage.getItem("bestScore")-0;
    curBestScore = curBestScore == 0 ? score: curBestScore;
   
  localStorage.setItem("bestScore",Math.min(score,curBestScore));
  displayBestScore();
 }

 displayBestScore();
 function displayBestScore(){
  let storedScore = localStorage.getItem("bestScore")-0;
  document.getElementById("best-score").innerText = storedScore;
 }
// bestScore(document.getElementById("game-score").innerText);;