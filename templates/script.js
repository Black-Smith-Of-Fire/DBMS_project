var table = document.getElementById('tbl');
var cells =table.getElementsByTagName('td');

for(var i = 0; i< cells.length;i++){
    cells[i].onclick = function(){
        console.log('clicked');
    }
}
