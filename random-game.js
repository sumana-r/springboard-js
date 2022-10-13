function randomGame() {
    let counter = 0;
    let interval = setInterval(function () {

        let randNo = Math.random();
        console.log(randNo);

        counter++;
        
        if (randNo > 0.75) {
            console.log(counter);
            clearInterval(interval);
        }

    }, 1000);
}