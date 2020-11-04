var x = document.getElementsByName("viewframe");

function playVid() {
  for (var i = 0; i < x.length; i++) {
  	x[i].play();
  }
}

function pauseVid() {
  x.pause();
}

document.addEventListener("load", playVid())