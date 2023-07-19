// page loading
const loadBg = document.querySelector(".load-bg");
window.addEventListener("load", () => {
  loadBg.classList.add("fade-out")

  setTimeout(() => {
    loadBg.style.display = "none";
    console.log(123);
  },1000);

})

// side bar
const burger = document.querySelector(".menuBurger");
const menu = document.querySelector(".menu");
const burgerBg = document.querySelector(".menuBurgerBg");
let items;
function burgerActive() {
  menu.classList.toggle("active");
}

burger.addEventListener("click", burgerActive);
burgerBg.addEventListener("click", burgerActive);

// render Img
url =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
async function getResult(url) {
  return (await fetch(url)).json();
}

document.addEventListener("DOMContentLoaded", async () => {
  const result = await getResult(url);
  const results = result["result"]["results"];
  const addBtn = document.querySelector(".addImg");
  const contentCards = document.querySelector(".contentCards");
  const headerCards = document.querySelector(".headerCards");
  let target = 33;
  let num = 0;

  // 
  for (num; num < 15; num++) {
    renderImg(results[num], num, headerCards, contentCards);
  }
  addBtn.addEventListener("click", () => {
    for (num; num < target; num++) {
      renderImg(results[num], num, headerCards, contentCards);
    }
    if (target == 58) {
      addBtn.style.display = "none";
    }
    if (num === target) {
      target += 18;
    }
    if (target > 58) {
      target = 58;
    }
  });
});

function renderImg(result, num, headerCards, contentCards) {
  const li = document.createElement("li");
  const span = document.createElement("span");
  const img = document.createElement("img");
  const h3 = document.createElement("h3");
  let reStr = /(.jpg)/gi;
  let imgSrc = result["file"].split(reStr);
  img.src = imgSrc[0] + imgSrc[1];
  img.src = img.src;
  h3.textContent = result["stitle"];

  //  headerCards
  if (num < 3) {
    li.classList = "d-flex align-items-center";
    li.append(img, h3);
    headerCards.appendChild(li);
    return;
  }

  // contentCards
  span.classList = "material-symbols-outlined";
  span.textContent = "star";
  contentCards.appendChild(li);
  li.append(span, img, h3);
}
