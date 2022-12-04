// categories is the main data structure for the app; it looks like this:

//  [
//    { title: "Math",
//      clues: [
//        {question: "2+2", answer: 4, showing: null},
//        {question: "1+1", answer: 2, showing: null}
//        ...
//      ],
//    },
//    { title: "Literature",
//      clues: [
//        {question: "Hamlet Author", answer: "Shakespeare", showing: null},
//        {question: "Bell Jar Author", answer: "Plath", showing: null},
//        ...
//      ],
//    },
//    ...
//  ]

let categories = [];
let clueSize = 5;
let categorySize = 6;



/** Get NUM_CATEGORIES random category from API.
 *
 * Returns array of category ids
 */

async function getCategoryIds() {
    let catIds = [];
    for (let i = 0; i < categorySize; i++) {
        let catUrl = `http://jservice.io/api/random`;//`https://jservice.io/api/categories`;
        let catResponse = await fetch(catUrl);
        let data = await catResponse.json();
        catIds.push(data[0].category.id);
    }
    return catIds;
}

/** Return object with data about a category:
 *
 *  Returns { title: "Math", clues: clue-array }
 *
 * Where clue-array is:
 *   [
 *      {question: "Hamlet Author", answer: "Shakespeare", showing: null},
 *      {question: "Bell Jar Author", answer: "Plath", showing: null},
 *      ...
 *   ]
 */

async function getCategory(catId) {

    let catIdUrl = `http://jservice.io/api/category?id=${catId}`;//`https://jservice.io/api/categories`;
    let catIdResponse = await fetch(catIdUrl);
    let catIddata = await catIdResponse.json();
    var clueArray = (catIddata.clues || []).splice(0, clueSize).map(cur => {
        return {
            question: cur.question,
            answer: cur.answer,
            showing: null
        }
    });
    var catObj = {
        title: catIddata.title,
        clues: clueArray
    }
    return catObj;
}

/** Fill the HTML table#jeopardy with the categories & cells for questions.
 *
 * - The <thead> should be filled w/a <tr>, and a <td> for each category
 * - The <tbody> should be filled w/NUM_QUESTIONS_PER_CAT <tr>s,
 *   each with a question for each category in a <td>
 *   (initally, just show a "?" where the question/answer would go.)
 */

async function fillTable() {
    let titleId = 0;
    for (let category of categories) {
        $("#jeopardy thead").append(`<td>${category.title}</td>`);
        let clues = category.clues;
        for (let i = 0; i < clueSize; i++) {
            let curIndex = i + 1;
            let strAppend = '<td></td>';
            if (clues.length > i) {
                strAppend = `<td id="${i}" data-q="${clues[i].question}" data-a="${clues[i].answer}" data-showing="${clues[i].showing}"> ? </td>`;
            }
            $("#jeopardy tr:nth-of-type(" + curIndex + ")").append(strAppend);
        }
        titleId++;
    }
}

/** Handle clicking on a clue: show the question or answer.
 *
 * Uses .showing property on clue to determine what to show:
 * - if currently null, show question & set .showing to "question"
 * - if currently "question", show answer & set .showing to "answer"
 * - if currently "answer", ignore click
 * */

function handleClick(evt) {
    if ($(evt.target).attr("data-showing") === "null") {
        let $dataq = $(evt.target).attr("data-q");
        $(evt.target).html($dataq).attr("data-showing", "question");

    } else if ($(evt.target).attr("data-showing") === "question") {
        let $dataa = $(evt.target).attr("data-a");
        $(evt.target).html($dataa).attr("data-showing", "answer");
    }
}
/** Wipe the current Jeopardy board, show the loading spinner,
 * and update the button used to fetch data.
 */

function showLoadingView() {
    $("#spin-container").show();
}

/** Remove the loading spinner and update the button used to fetch data. */

function hideLoadingView() {
    $("#spin-container").hide();

}

/** Start game:
 *
 * - get random category Ids
 * - get data for each category
 * - create HTML table
 * */

async function setupAndStart() {
    categories = [];
    let catIds = await getCategoryIds();
    for (let j = 0; j < clueSize; j++) {
        $("#jeopardy tbody").append(`<tr id="${j}"></tr>`);
    }
    for (let catId of catIds) {
        let data = await getCategory(catId);
        categories.push(data);
        hideLoadingView();
    }
    await fillTable();
}
hideLoadingView();
/** On click of start / restart button, set up game. */
$("#start").on("click", async () => {
    showLoadingView();
    $("#jeopardy thead").html("");
    $("#jeopardy tbody").html("");
    await setupAndStart();
});

/** On page load, add event handler for clicking clues */
$("#jeopardy tbody").on("click", function handleTdClick(event) {
    handleClick(event);
});

