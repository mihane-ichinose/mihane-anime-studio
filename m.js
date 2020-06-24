function backToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function topNav() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

function offNav() {
    var x = document.getElementById("myLinks");
    x.style.display = "none";
}

// var mobileAgent = new Array("iphone", "ipod", "ipad", "android", "mobile", "blackberry", "webos", "incognito", "webmate", "bada", "nokia", "lg", "ucweb", "skyfire")
// var browser = navigator.userAgent.toLowerCase();
// var isDesktop = false;
// for (var i=0; i<mobileAgent.length; i++){ if (browser.indexOf(mobileAgent[i])==-1){ isDesktop = true;
// //Desktop visit m.html illegal
// location.href = "index.html";
// break; } }
// BUG: Dead loop occurs.