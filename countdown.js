function countDown(num){
    let interval = setInterval(function() {
        finalval(--num);
       
        if(num == 0){
            console.log("DONE!");  
            clearInterval(interval);
        }
    }, 1000);
    } 
    
function finalval(numVal){
    console.log(numVal);
}