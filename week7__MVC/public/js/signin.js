const signBtn = document.querySelector(".sign__button");
const signCheckbox = document.querySelectorAll(".sign__checkbox input");

const squareBtn = document.querySelector(".square__button");
const squareInput = document.querySelector(".square_intupWrap input");

// 當 signBtn 被點擊 ，先判斷 checkbox 狀態
// 若未勾選跳出 alert "Please checkthe checkbox first"
// 若已勾選，以 POST sumit 到 /signin 路徑
if (signCheckbox && squareBtn) {
  // 兩個 checkbox 都添加事件監聽
  for (const item of signCheckbox) {
    item.form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (item.checked) {
        item.form.submit();
      } else {
        alert("Please checkthe checkbox first");
      }
    });
  }

  squareBtn.form.addEventListener("submit", (e) => {
    e.preventDefault();
    // 判斷是否是數字 或 數字小於零
    if (!Number(squareInput.value) || Number(squareInput.value) <= 0) {
      alert("Please enter a positive number");
    } else {
      e.target.action = "/square/" + Number(squareInput.value);
      console.log(e.target.action);
      squareBtn.form.submit();
    }
  });
}
