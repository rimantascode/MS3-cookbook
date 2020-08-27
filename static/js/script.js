var imageUrl = "https://cdn.sstatic.net/Sites/stackoverflow/img/sprites.svg";
var blob = null;
var xhr = new XMLHttpRequest();
xhr.open("GET", imageUrl, true);
xhr.responseType = "blob";
xhr.onload = function () {
  blob = xhr.response;
  console.log(blob, blob.size);
};
xhr.send();
