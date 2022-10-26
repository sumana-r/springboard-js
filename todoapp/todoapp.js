
const todoForm = document.getElementById('todo-form');
//const newTask = document.querySelector('input[name="todo-text"]');



todoForm.addEventListener("submit", function (event) {
  event.preventDefault();
  const newTask = document.getElementById('myText').value;
  if (newTask != '') {

    createTaskEle(newTask, false);
    var wishListArr = JSON.parse(localStorage.getItem("wishList"));
    var wisListItem = {
      text: newTask,
      striked: false
    };
    wishListArr.push(wisListItem);
    localStorage.setItem("wishList", JSON.stringify(wishListArr));
  }


  todoForm.reset();

});



function createTaskEle(text, striked) {
  const newLi = document.createElement('li');
  var textlabel = document.createElement('label');
  textlabel.addEventListener('click', function (e) {
    e.target.classList.add("striketext");
    var wishListArr = JSON.parse(localStorage.getItem("wishList"));
    var newWishlistArr = [];
    for (let i = 0; i < wishListArr.length; i++) {
      let curwishList = wishListArr[i];
      if (textlabel.textContent == curwishList.text) { //&& curwishList.striked == false){
        curwishList.striked = true;
      }

      newWishlistArr.push(curwishList);
      console.log(wishListArr);
    }
    localStorage.setItem("wishList", JSON.stringify(newWishlistArr));
  });

  if (striked) {
    textlabel.classList.add("striketext");
  }
  var rmveBtn = document.createElement('button');
  rmveBtn.innerText = 'Remove';
  textlabel.textContent = text;
  rmveBtn.addEventListener('click', function (e) {
    e.target.parentElement.remove();
    var wishListArray = JSON.parse(localStorage.getItem("wishList"));
    var currwishListArr = [];
    for(let i = 0; i < wishListArray.length; i++){
      let curwishList = wishListArray[i];
      if(textlabel.textContent != curwishList.text){
        currwishListArr.push(curwishList);
      }

    }
    localStorage.setItem("wishList",JSON.stringify(currwishListArr));
  });
  const getUl = document.querySelector('ul');
  getUl.appendChild(newLi);
  newLi.append(textlabel);
  newLi.append(rmveBtn);
}

//'[{"text":"djhfjnb","striked":false},{"text":"kassd","striked":true}]'
function init() {
  var wishList = JSON.parse(localStorage.getItem("wishList"));
  for (let i = 0; i < wishList.length; i++) {
    let curwishList = wishList[i];
    createTaskEle(curwishList.text, curwishList.striked);

  }

}

init();
/*
  text, striked
  {text: "asdad", striked: true}
  {text: "asdad", striked: false}
*/