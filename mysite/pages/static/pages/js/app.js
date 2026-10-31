document.addEventListener("DOMContentLoaded", function () {
  console.log("Сайт загружен: статика подключена");
  document.querySelectorAll(".card").forEach(function (card) {
    card.addEventListener("click", function () {
      card.style.background = "#e8f1f4";
    });
  });
});
