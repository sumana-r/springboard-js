//1. Select the section with an id of container without using querySelector.
const sectId = document.getElementById('container');
console.log(sectId);

//2. Select the section with an id of container using querySelector.
const sectionId = document.querySelector('section');
console.log(sectionId);

//3. Select all of the list items with a class of “second”.
const secondClass = document.getElementsByClassName('second');

//4. Select a list item with a class of third, but only the list item inside of the ol tag.
const olList = document.querySelector('ol');
const olThird = olList.getElementsByClassName('third')
console.log(olThird);

//5. Give the section with an id of container the text “Hello!”.
//sectId.innerText = "Hello!"

//6. Add the class main to the div with a class of footer
const divfooter = document.querySelector('.footer');
divfooter.classList.add('main');

//7. Remove the class main on the div with a class of footer.
divfooter.classList.remove('main');

//8. Create a new li element.
const liFour = document.createElement("li");

//9. Give the li the text “four”.
liFour.textContent='four';
//liFour.classList.add('four');

//10. Append the li to the ul element.
const ulList = document.querySelector('ul');
ulList.append(liFour);

//11. Loop over all of the lis inside the ol tag and give them a background color of “green”.
function olListLoop(){
    const liVal = document.querySelectorAll('ol > li');
    
        for(let li of liVal){
            console.log(li);
            li.classList.add('content-color');
            //liVal.classList.toggle('content-class');
    }
}
olListLoop();

//12. Remove the div with a class of footer
const removediv = document.querySelector('.footer');
removediv.remove();

