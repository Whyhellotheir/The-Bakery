const placeOrder = document.getElementsByClassName("placeOrder")[0];
const aboutMe = document.getElementsByClassName("aboutMe")[0];

placeOrder.addEventListener("click", function(){
    window.location.href = "/placeOrder"; // This will redirect to the place order page
});

aboutMe.addEventListener("click", function(){
    window.location.href = "/aboutMe"; // This will redirect to the about me page
});
