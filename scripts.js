$(function(){
  var x = 0;
      $(".pseudo-search-type").typed({
        strings: ["a camera", "a book", "a guitar", "a bike", "kitchenware"],
        typeSpeed: 90, // typing speed
        startDelay: 300,
        backDelay: 4000, // pause before backspacing
        backSpeed: 90,
        loop: true, // loop on or off (true or false)
        loopCount: false, // number of loops, false = infinite
        onStringTyped: function() {
          console.log(x);
          ++x;
          if (x == 5) {
            x = 0;
          }
          changeBGImage(x);
       },

       resetCallback: function() { changeBGImage(x); }
     });
});

function changeBGImage(arrayPos) {
  if (arrayPos == 1){
    document.getElementById('top-background').className="bg-camera";
  } else if (arrayPos == 2){
    document.getElementById('top-background').className="bg-book";
  } else if (arrayPos == 3){
    document.getElementById('top-background').className="bg-guitar";
  } else if (arrayPos == 4){
    document.getElementById('top-background').className="bg-bike";
  } else if (arrayPos == 0){
    document.getElementById('top-background').className="bg-kitchen";
  }
}

function getAuthData() {
  var text = document.getElementById("signup-input-name").value;
  document.getElementById("demo").innerHTML = text;
}
