"use strict";

/******************************************************************************
 * Handling navbar clicks and updating navbar
 */

/** Show main list of all stories when click site name */

function navAllStories(evt) {
  console.debug("navAllStories", evt);
  hidePageComponents();
  putStoriesOnPage();
  //$storyForm.hide();
}

$body.on("click", "#nav-all", navAllStories);
/** Show submit  */
function navSubmitClick(evt) {
  console.debug("navSubmitClick", evt);
  hidePageComponents();
  $storyForm.show();
  $allStoriesList.show(); 


}

$navSubmit.on("click",navSubmitClick);

/** Show user favorites*/
async function navFavStories(evt) {
  //console.debug("navAllStories", evt);
  hidePageComponents();
  await putFavStoriesOnPage();
  $favStoriesList.show();
  //$storyForm.hide();
}
$navFav.on("click",navFavStories);

/** Show the stories based on the current user */
async function navMyStories(evt) {
  //console.debug("navAllStories", evt);
  hidePageComponents();
  await putmyStoriesOnPage();
  $myStoriesList.show();
}

$navMyStories.on("click",navMyStories);
/** Show login/signup on click on "login" */

function navLoginClick(evt) {
  console.debug("navLoginClick", evt);
  hidePageComponents();
  $loginForm.show();
  $signupForm.show();
}

$navLogin.on("click", navLoginClick);

/** When a user first logins in, update the navbar to reflect that. */

function updateNavOnLogin() {
  console.debug("updateNavOnLogin");
  $(".main-nav-links").show();
  $navLogin.hide();
  $navLogOut.show();
  $navUserProfile.text(`${currentUser.username}`).show();
}
 