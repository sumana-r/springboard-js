const drawBtn = document.getElementById("get-card-btn");
const cardCntr = document.getElementById("card-cntr");

var deckId;
var count = 0;

async function getDeckId(){
    let resp = await $.getJSON("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1");
    drawBtn.addEventListener('click', () => handleClick(resp.deck_id),false);
}  
async function handleClick(deckId) {
    let resp = await drawCard(deckId);

    let li = document.createElement("li");
    li.style.transform = `rotate(${count}deg)`;
    li.appendChild(createImageEle(resp.cards[0].image));
    cardCntr.appendChild(li);
    count = count + 20;

    if (resp.remaining == 0) {
        drawBtn.style.display = 'None';
    }

}

async function drawCard(deckId){
    let resp =  await $.getJSON(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`);
    return resp;
}
function createImageEle(source) {
    let img = document.createElement('img');
    img.src = source;
    return img;
}

deckId = getDeckId()


