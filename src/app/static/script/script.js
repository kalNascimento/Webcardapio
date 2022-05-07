


function CardBorderChange(number) {
    //console.log(number);
    let border = document.getElementById(`border-${number}`);
    let check = document.getElementById(`checkbox-${number}`);
    check.checked = !check.checked;
    if(check.checked == true){
        border.style.border = '2px solid #FFDE38'
    }else{
        border.style.border = '2px solid #FFFFFF'
    }
}