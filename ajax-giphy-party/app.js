console.log("Let's get this party started!");
document.addEventListener("DOMContentLoaded", init);
function init() {
    document.getElementById("submitBtn").addEventListener("click", async (event) => {
        event.preventDefault();
        let string = document.getElementById("searchVal").value.trim();
        let url = `https://api.giphy.com/v1/gifs/search?api_key=29nF6I1Prs3ipmWMRbUifBH7ng6yEl1N&q=${string}&limit=25&offset=0&rating=g&lang=en`
        console.log(url);
        var resp = await fetch(url);
        var data = await resp.json();
        console.log(data);
        console.log(data.meta);
        let img = document.createElement('img');

        let imgSrc = data.data[0].images.downsized.url;
        img.setAttribute('src', imgSrc)

        $("#imgarea").append(img);

    });
    // remove all the gif
    $("#rmbtn").on("click", (event) => {
        $("#imgarea").empty();
    });
}