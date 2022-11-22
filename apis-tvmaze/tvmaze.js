"use strict";

const $showsList = $("#shows-list");
const $episodesArea = $("#episodes-area");
const $searchForm = $("#search-form");


/** Given a search term, search for tv shows that match that query.
 *
 *  Returns (promise) array of show objects: [show, show, ...].
 *    Each show object should contain exactly: {id, name, summary, image}
 *    (if no image URL given by API, put in a default image URL)
 */

async function getShowsByTerm(queryParam) {
  // ADD: Remove placeholder & make request to TVMaze search shows API.
  let reqUrl = `http://api.tvmaze.com/search/shows?q=${queryParam}`;
 
  var resp = await fetch(reqUrl);
  var data = await resp.json();
  const showArr = [];
  for(let dataVal of data){
    
    var obj = {id: dataVal.show.id,
    name: dataVal.show.name,
    summary:dataVal.show.summary,
    image:(dataVal.show.image !== null)?dataVal.show.image.original:"https://tinyurl.com/tv-missing"
    }
  showArr.push(obj);
  }
   return showArr;
 
}


/** Given list of shows, create markup for each and to DOM */

function populateShows(shows) {
  $showsList.empty();

  for (let show of shows) {
    //console.log(show);
    const $show = $(
        `<div data-show-id="${show.id}" class="Show col-md-12 col-lg-6 mb-4">
         <div class="media">
           <img 
              src="${show.image}" 
              alt="Bletchly Circle San Francisco" 
              class="w-25 mr-3">
           <div class="media-body">
             <h5 class="text-primary">${show.name}</h5>
             <div><small>${show.summary}</small></div>
             <button  class="btn" id="btn-episode">
               Episodes
             </button>
           </div>
         </div>  
       </div>
      `);

    $showsList.append($show);  }
}

//class="btn btn-outline-light btn-sm Show-getEpisodes"
/** Handle search form submission: get shows from API and display.
 *    Hide episodes area (that only gets shown if they ask for episodes)
 */

async function searchForShowAndDisplay() {
  const term = $("#searchForm-term").val();
  const shows = await getShowsByTerm($("#search-query"));//(term);

  $episodesArea.hide();
  populateShows(shows);
}

$searchForm.on("submit", async function (evt) {
  evt.preventDefault();
  await searchForShowAndDisplay();
});


/** Given a show ID, get from API and return (promise) array of episodes:
 *      { id, name, season, number }
 */
 $("#shows-list").on("click", '#btn-episode', async function handleEpisodeClick(event) {
  event.preventDefault();
  const episodeId = $(event.target).parents(".Show").data("show-id");
  const episodes = await getEpisodesOfShow(episodeId);
  console.log(episodes);
  //$episodesArea.empty();
  populateEpisodes(episodes);
  $episodesArea.show();
});


async function getEpisodesOfShow(id) {
  let reqUrl = `http://api.tvmaze.com/shows/${id}/episodes`;

  var response = await fetch(reqUrl);
  var respData = await response.json();
  const showArr = [];
  for (let dataVal of respData) {
    var idObj = {
      id: dataVal.id,
      name: dataVal.name,
      season: dataVal.season,
      number: dataVal.number
    }

    showArr.push(idObj);
  }
  //console.log(showArr);
  return showArr;

}

/** Write a clear docstring for this function... */

 function populateEpisodes(episodes) {
  $("#episodes-list").empty();
  for (let episode of episodes) {
  const episodeLi = $(`<li> ${episode.name} (season ${episode.season}, number ${episode.number})</li>`);
  $("#episodes-list").append(episodeLi);
  }
}
