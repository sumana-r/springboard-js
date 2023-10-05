// callback pattern
let baseURL = "https://pokeapi.co/api/v2/pokemon";

$.getJSON(`${baseURL}/1/`, p1 => {
  console.log(`The first pokemon is ${p1.name}`);
  $.getJSON(`${baseURL}/2/`, p2 => {
    console.log(`The second pokemon is ${p2.name}`);
    $.getJSON(`${baseURL}/3/`, p3 => {
      console.log(`The third pokemon is ${p3.name}`);
    });
  });
});

// promise pattern
let baseURL = "https://pokeapi.co/api/v2/pokemon";

$.getJSON(`${baseURL}/1/`)
  .then(p1 => {
    console.log(`The first pokemon is ${p1.name}`);
    return $.getJSON(`${baseURL}/2/`);
  })
  .then(p2 => {
    console.log(`The second pokemon is ${p2.name}`);
    return $.getJSON(`${baseURL}/3/`);
  })
  .then(p3 => {
    console.log(`The third pokemon is ${p3.name}`);
    return $.getJSON(`${baseURL}/3/`);
  });

// async / await pattern
async function catchSomeOfEm() {
  let baseURL = "https://pokeapi.co/api/v2/pokemon";
  let p1 = await $.getJSON(`${baseURL}/1/`);
  let p2 = await $.getJSON(`${baseURL}/2/`);
  let p3 = await $.getJSON(`${baseURL}/3/`);

  console.log(`The first pokemon is ${p1.name}`);
  console.log(`The second pokemon is ${p2.name}`);
  console.log(`The third pokemon is ${p3.name}`);
}

catchSomeOfEm();

// async / await in parallel
async function catchSomeOfEmParallel() {
  let baseURL = "https://pokeapi.co/api/v2/pokemon";
  let p1Promise = $.getJSON(`${baseURL}/1/`);
  let p2Promise = $.getJSON(`${baseURL}/2/`);
  let p3Promise = $.getJSON(`${baseURL}/3/`);

  let p1 = await p1Promise;
  let p2 = await p2Promise;
  let p3 = await p3Promise;

  console.log(`The first pokemon is ${p1.name}`);
  console.log(`The second pokemon is ${p2.name}`);
  console.log(`The third pokemon is ${p3.name}`);
}

catchSomeOfEmParallel();

// async / await using Promise.all
async function catchSomeOfEmParallel2() {
  let baseURL = "https://pokeapi.co/api/v2/pokemon";
  let pokemon = await Promise.all([
    $.getJSON(`${baseURL}/1/`),
    $.getJSON(`${baseURL}/2/`),
    $.getJSON(`${baseURL}/3/`)
  ]);

  console.log(`The first pokemon is ${pokemon[0].name}`);
  console.log(`The second pokemon is ${pokemon[1].name}`);
  console.log(`The third pokemon is ${pokemon[2].name}`);
}

catchSomeOfEmParallel2();