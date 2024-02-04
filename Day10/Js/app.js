// const myPara = document.getElementById("para").innerText
// console.log(myPara)

const myBtn = document.getElementById("clickBtn");
function gettingUserName(){
    event.preventDefault();
    const userFirstName = document.getElementById("username").value;
    const userPassword = document.getElementById("userPassword").value;
    console.log(userFirstName, userPassword);
}
myBtn = addEventListener("click", gettingUserName)