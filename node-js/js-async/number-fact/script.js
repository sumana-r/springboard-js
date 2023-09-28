
var ul = document.querySelector("ul");

async function numberFacts(){
  let baseURL = "http://numbersapi.com/random?min=1&max=100/";
  let promises = [];
  for(let i = 0; i < 5; i++)
  {
    promises.push(axios.get(`${baseURL}${i}/`));
  }
  let facts = await Promise.all(promises);
  facts.forEach(fact => {
    console.log(fact.data);
    let li = document.createElement("li");
    li.appendChild(document.createTextNode(` ${fact.data}`));
    ul.appendChild(li);
  });

}

numberFacts();