async function getStarWarsData() {
  console.log("starting!");
  let movieData = await $.getJSON(
      "https://swapi.dev/api/films/");
  // these lines do NOT run until the promise is resolved!
  console.log("all done!");
  console.log(movieData);
}

getStarWarsData();

let starWars = {
  genre: "sci-fi",
  async logMovieData() {
    let url = "https://swapi.dev/api/films/";
    let movieData = await $.getJSON(url);
    console.log(movieData.results);
  }
};

starWars.logMovieData();

async function getUser(user) {
  try {
    let url = `https://api.github.com/users/${user}`;
    let response = await $.getJSON(url);
    console.log(`${response.name}: ${response.bio}`);
  } catch (e) {
    console.log("User does not exist!");
  }
}
// end get user fn

getUser("mmmaaatttttt");
// Matt Lane: Co-founder at @rithmschool.
// Teacher of how the internet works.
// Check us out at rithmschool.com

getUser("nopenouserhereomggoaway");
// User does not exist!
