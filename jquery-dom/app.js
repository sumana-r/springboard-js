


$('#submitBtn').click(function(event){
    event.preventDefault();
    let mvregex = /[a-zA-Z]{2,}/;
    //let mratingregex = /[0-9]/;
   
  const mvTitle = $('#title').val();
 
  const mvrating = $('#rating').val();
 
if (mvTitle != '' && mvrating !='' && mvregex.test(mvTitle)) {
   $('#movietable').append(`<tr> <td id="column-title" > ${mvTitle} </td> 
   <td id="column-rating" type= "number"> ${mvrating} </td> <td><button id="remove-rating" type="button"> Remove </button></td></tr>`)
}

$('#movieform').each(function(){
    this.reset();
});
});

$('#movietable').on('click', '#remove-rating',  function(event){
   $(this).closest('tr').remove();
});
