const drawBtn = document.getElementById("get-card-btn");
const cardCntr = document.getElementById("card-cntr");

var deckId;
var count = 0;
function getDeckId(){
    return axios.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1");
}  

function drawCard(deckId){
    return axios.get(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`);

}
function createImageEle(source) {
    let img = document.createElement('img');
    img.src = source;
    return img;
}
deckId = getDeckId().then(resp => {
    deckId = resp.data.deck_id;
    drawBtn.addEventListener('click',()=>{
        drawCard(deckId).then(resp =>{
           console.log(resp.data.cards[0].image);
            let li = document.createElement("li");
            li.style.transform = `rotate(${count}deg)`;
            li.appendChild(createImageEle(resp.data.cards[0].image));
            cardCntr.appendChild(li);
            count = count + 20;
            console.log(resp.data.remaining);
            if (resp.data.remaining == 0) {
                drawBtn.style.display = 'None';
            }
        })
    });
    
});


