const closeBtn = document.querySelectorAll(".btn")[1];
const minBtn = document.querySelectorAll(".btn")[0];
const body = document.querySelector("body");
const nextBtn = document.querySelectorAll(".btn")[2];
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password")

closeBtn.onclick = () => {
  pywebview.api.windowClose();
};
minBtn.onclick = () => {
  pywebview.api.windowMinimize();
};

nextBtn.onclick = () => {
  pywebview.api.setLogin(emailInput.value.toString(), passwordInput.value.toString())
}
