
var ul = document.querySelector("ul");

let fourFactPromises = [];

for (let i = 1; i < 5; i++) {
    fourFactPromises.push(
    axios.get(`http://numbersapi.com/random?min=1&max=100/${i}/`)
  );
}
console.log(fourFactPromises)
Promise.all(fourFactPromises)
  .then(factArr => (
    factArr.forEach(p => {
        console.log(p.data)
        let li = document.createElement("li");
            li.appendChild(document.createTextNode(` ${p.data}`));
            ul.appendChild(li);})
  ))
  .catch(err => console.log(err));
