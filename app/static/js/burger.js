let burger = document.querySelector(".burger");
let menu = document.querySelector(".menu");
let headerWrapper = document.querySelector(".header_wrapper");

burger.addEventListener("click", () => {
  menu.classList.toggle("active");
});

window.addEventListener("click", (e) => {
  if (!headerWrapper.contains(e.target)) {
    menu.classList.remove("active");
  }
});

let menuLinks = document.querySelectorAll("a");

menuLinks.forEach((link) => {
  link.addEventListener("click", () => {
    menu.classList.remove("active");
  });
});
