const fs = require('fs');
const process = require('process');
const axios = require('axios');

let writepath;
let path;

if(process.argv[2] === '--out') {
  writepath = process.argv[3];
  path = process.argv[4];
} else {
  path = process.argv[2];
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
if(isValidUrl(path)){
  webCat(path);
}
else{
  cat(path);
}

function webCat(webpath){
  
  axios.get(webpath).then(function(resp) {
  outFile(resp.data,writepath);  
  console.log(resp.data.slice(0, 80), '...');
});
}

function cat(path) {
    
  fs.readFile(path,'utf8',(err,data)=>{
      if(err){
          console.log("ERROR:", err);
          
          process.exit(1)
      }
      outFile(data,writepath);
  })
}



function outFile(content,writepath){

    fs.writeFile(writepath, content, "utf8", function(err) {
        if (err) {
          console.error(err);
          process.exit(1);
        }
        console.log('Successfully wrote to file!');
      });

}

// outFile(process.argv[2]);
//--out /data/new.txt