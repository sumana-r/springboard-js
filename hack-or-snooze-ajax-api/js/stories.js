"use strict";

// This is the global list of the stories, an instance of StoryList
let storyList;



/** Get and show stories when site first loads. */

async function getAndShowStoriesOnStart() {
  storyList = await StoryList.getStories();
  $storiesLoadingMsg.remove();
  putStoriesOnPage();
}

/**
 * A render method to render HTML for an individual Story instance
 * - story: an instance of Story
 *
 * Returns the markup for the story.
 */

function generateStoryMarkup(story) {
  // console.debug("generateStoryMarkup", story);

  const hostName = $(location).attr('hostname');
  const storyId = story.storyId;
  return $(`
      <li id="${story.storyId}">
     ${currentUser? getFavIconMarkup(storyId):""}
      ${currentUser?getDeleteMarkup(storyId):""}
       <a href="${story.url}" target="a_blank" class="story-link">
          ${story.title}
        </a>
        <small class="story-hostname">(${hostName})</small>
        <small class="story-author">by ${story.author}</small>
        <small class="story-user">posted by ${story.username}</small>
      </li>
    `);
}
/* list the favourite and other stories */
function getFavIconMarkup(storyId){
  let userFavourites = `<i class="fa fa-star-o userfav" ></i>`;
  if(currentUser.favorites){
    for(let i = 0; i < currentUser.favorites.length; i++){
      if((currentUser.favorites[i].storyId === storyId)){
         userFavourites = `<i class="fa fa-star userfav" ></i>`
      }
    } 
  }
 return userFavourites;
}
/*list delete icon for logged user  */
function getDeleteMarkup(storyId){
  let deleteUserStory = "";
  if(currentUser.ownStories){
    for(let i = 0; i < currentUser.ownStories.length; i++){
      if(currentUser.ownStories[i].storyId === storyId){
        deleteUserStory = `<i class="fa fa-trash story-delete" aria-hidden="true"></i>`;
      }
      
    }
   
  }
  return deleteUserStory;
}

$(".stories-container").on("click",".story-delete", async function(evt){
  const storyId = $(evt.target).parent().attr("id");
  await deleteMyStory(storyId);
  storyList = await StoryList.getStories();
  if($("#fav-stories-list").is(":visible")){
    putFavStoriesOnPage();
   } else if($("#my-stories-list").is(":visible")){
    putmyStoriesOnPage();
   }else{
    putStoriesOnPage();
   }

});

$(".stories-container").on("click",".userfav", async function(evt){
  const favStoryId = $(evt.target).parent().attr("id");
 if($(evt.target).hasClass("fa-star")){
  await removeFavStory(favStoryId);
 }else{
  await addFavStory(favStoryId);
 }
 if($("#fav-stories-list").is(":visible")){
  putFavStoriesOnPage();
 } else if($("#my-stories-list").is(":visible")){
  putmyStoriesOnPage();
 }else{
  putStoriesOnPage();
 }

 
 
});

async function addFavStory(storyId) {
  const response = await axios({
    url: `${BASE_URL}/users/${currentUser.username}/favorites/${storyId}`,
    method: "POST",
    data:{"token": currentUser.loginToken},
    headers:{
      "Content-Type":"application/json"
    }
  });
  
  currentUser.favorites = response.data.user.favorites;
  
  
}

async function removeFavStory(storyId) {
  
  
  console.log(currentUser.favorites);
  const response = await axios({
    url: `${BASE_URL}/users/${currentUser.username}/favorites/${storyId}`,
    method: "DELETE",
    data:{"token": currentUser.loginToken},
    headers:{
      "Content-Type":"application/json"
    }
  });
   //console.log(response);
   currentUser.favorites = response.data.user.favorites;

}



/** Gets list of stories from server, generates their HTML, and puts on page. */

function putStoriesOnPage() {
  console.debug("putStoriesOnPage");

  $allStoriesList.empty();

  // loop through all of our stories and generate HTML for them
  for (let story of storyList.stories) {
   
    const $story = generateStoryMarkup(story);
    $allStoriesList.append($story);
  }

 $allStoriesList.show();
}
/** Filter the list of  favourite stories generates their HTML, and puts on Favourites page. */

async function getMyFavStory() {
  const response = await axios({
    url: `${BASE_URL}/users/${currentUser.username}?token=${currentUser.loginToken}`,
    method: "GET"
  });
  currentUser.favorites = response.data.user.favorites;
  console.log(currentUser.favorites);
  }

async function putFavStoriesOnPage() {
  await getMyFavStory();
  $favStoriesList.empty();
  console.log(currentUser.favorites);
  // loop through all of our stories and generate HTML for them
  if(currentUser.favorites.length !== 0){
    for (let story of currentUser.favorites) {
      const $story = generateStoryMarkup(story);
      $favStoriesList.append($story);
    }
  }
  }

  

  //$allStoriesList.show();


async function getMyStory() {
const response = await axios({
  url: `${BASE_URL}/users/${currentUser.username}?token=${currentUser.loginToken}`,
  method: "GET"
});
currentUser.ownStories = response.data.user.stories;

}

async function putmyStoriesOnPage() {
  //console.debug("putFavStoriesOnPage");
  await getMyStory();
  $myStoriesList.empty();

  // loop through all of our stories and generate HTML for them
  for (let story of currentUser.ownStories) {
   const $story = generateStoryMarkup(story);
   $myStoriesList.append($story);
 }

}
async function deleteMyStory(storyId) {
  const response = await axios({
    url: `${BASE_URL}/Stories/${storyId}?token=${currentUser.loginToken}`,
    method: "DELETE"
  });
   console.log(response);
  }

async function createStory(){
  const title = $("#submit-title").val();
  const url = $("#submit-url").val();
  const story = $("#submit-text").val();
  const username = currentUser.username;
  const author = currentUser.username;
  const createdAt = "";
  const storyId = "";

//storyId, title, author, url, username, createdAt
  const newStory =  new Story(storyId,title,username, url, createdAt);
  const hostname =  newStory.getHostName();
  
  const storyObj = {title, author, url};
  const storyAdd = new StoryList(storyList);
  console.log(storyObj);
  const createStory =  storyAdd.addStory(username,storyObj);
  console.log(hostname);
  $storyForm.trigger("reset");

 storyList = await StoryList.getStories();
 putStoriesOnPage();

}

$("#story-submit").on("click",  createStory);
