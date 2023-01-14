




var letterOfWord = '';


$('#game').on('click', '#board.active', function (e) {
  
  const $curCell =  $(e.target)
  if($curCell.hasClass("unselect")){
    $curCell.addClass("selected").removeClass("unselect");
    letterOfWord = $(e.target).text();
    $('#newword').val($('#newword').val() + letterOfWord);
    
    
  }else{
    $curCell.addClass("unselect").removeClass("selected");
    const word = $('#newword').val();
    $('#newword').val(word.slice(0,-1));  
    
  }
  
})
// Add the guessed word and update the score if the word is valid
$('button[name=add_word]').click(function(e) {
  e.preventDefault()
  $('#board tr td').removeClass("selected").addClass("unselect")
  axios.post('/addWord/'+ $('#newword').val())
  
  .then(function(response){
    console.log(response.data);
    $('#scoreid').val(response.data[1])
  })
  $('#newword').val('')
  
  
})



$('#gamestart').click(function(e) {
  e.preventDefault();
  $('#board').addClass("active");
  var count = 59, timer = setInterval(function() {
    $("#timer").html(count--);
    if(count < 0) {      
      clearInterval(timer);
      setBestScore(); 
      gameEnd();
      
      }
  }, 1000);  
})



function gameEnd() {
  
  const score = $('#scoreid').val();
  alert(`Time up! your Score is ${score}`);
  alert(`start new game`);
  $('#board').removeClass("active");
  $('#board tr td').removeClass("selected");
  $('#newword').val('');
  $('#scoreid').val('0');
  
}

function setBestScore(){
  const score = $('#scoreid').val() - 0; 
   
  let curBestScore = localStorage.getItem("bestScore")-0; 
  localStorage.setItem("bestScore",Math.max(score,curBestScore));
  displayBestScore();
  
 }


// $('#newgame').click(function(e) {

  
  

// })
function displayBestScore(){
  let highscore = localStorage.getItem("bestScore") - 0;
  $('#highscore-id').val(highscore);
}
setBestScore();


 
  
  






