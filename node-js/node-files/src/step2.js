const fs = require('fs');
const process = require('process');
const axios = require('axios');



function cat(path) {
    
        fs.readFile(path,'utf8',(err,data)=>{
            if(err){
                console.log("ERROR:", err.stack);
                
                process.exit(1)
            }
            console.log(data);
        })
}
function webCat(webpath){
    
            axios.get(webpath).then(function(resp) {
            console.log(resp.data.slice(0, 80), '...');
 });

}
const isValidUrl = urlString=> {
    var urlPattern = new RegExp('^(https?:\\/\\/)?'+ // validate protocol
  '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // validate domain name
  '((\\d{1,3}\\.){3}\\d{1,3}))'+ // validate OR ip (v4) address
  '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // validate port and path
  '(\\?[;&a-z\\d%_.~+=-]*)?'+ // validate query string
  '(\\#[-a-z\\d_]*)?$','i'); // validate fragment locator
return !!urlPattern.test(urlString);
}
if(isValidUrl(process.argv[2])){
    webCat(process.argv[2]);
}
else{
    cat(process.argv[2]);
}


