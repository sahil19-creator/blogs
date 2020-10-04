console.log("sahil")
console.log("efnjenfkj")
sideBtn=document.querySelector("#sB")
sidebar=document.querySelector("#sideBr")
navbr=document.querySelector("#navBr")
Carea=document.querySelector(".dashboard_area")
console.log(Carea)

var i=0
sideBtn.addEventListener("click",()=>{

    if (i==0){
        i=i+1
        sidebar.style.width="0px";
        navbr.style.marginLeft="0px";
        Carea.style.marginLeft="0px";
    }
    else{
        sidebar.style.width="300px";
        navbr.style.marginLeft="300px";
        Carea.style.marginLeft="300px";
        i=0

    }
    
})