function swapText() {
    var titleText = document.getElementById("text");
    if (titleText.innerHTML === "Kamil Ulfik") {
        titleText.innerHTML = "kamil.ulfik@gmail.com";
    } else {
        titleText.innerHTML = "Kamil Ulfik";
    }
  }