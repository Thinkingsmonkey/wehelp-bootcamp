const searchInput = document.querySelector(".searchInput"),
  searchButton = document.querySelector(".searchButton"),
  memberInfo = document.querySelector(".memberInfo"),
  patchInput = document.querySelector(".patchInput"),
  patchButton = document.querySelector(".patchButton"),
  patchMessage = document.querySelector(".patchMessage"),
  memberName = document.querySelector(".sign__title span");

async function get_memberInfo() {
  const url = `/api/member?username=${searchInput.value}`;
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "text/plain",
      },
    });
    console.log(response);
    if (!response.ok) {
      throw new Error("無此會員");
    }
    const responseData = await response.json();
    memberInfo.textContent = `${responseData.data.name} (${responseData.data.username})`
  } catch (error) {
    memberInfo.textContent = error.message;
  }
}


async function patch_name(){
  const url = `/api/member`;
  const content_usernames = document.querySelectorAll(".content_username");
  const item__titles = document.querySelectorAll(".item__title");

  try {
    const response = await fetch(url,{
      method: "PATCH",
      body: patchInput.value,
      headers: {
        "content-type": "text/plain",
      },
    });
    if (!response.ok) {
      let resData = await response.json();
      throw new Error(resData.message);
    }
    const resData = await response.json();
    // 修改相同 username 留言 title
    // 1：要取得 id？ 還是 使用 username 但先將 username 的資料庫欄位屬性添加為獨一無二
    //  => 發現 留言中並沒有 username 的資料無法選取
    //  => 先讓 member 頁面的留言 for 輸出多一個 username，暫時使用 display:none 
    //  => 將每個留言中的 username 與當前帳號的 username 相同的時候
    //  => 改變留言的 title 為修正後的 name
    item__titles.forEach((title, index) => {
      if (content_usernames[index].textContent === resData.data.username) {
        title.textContent = resData.data.name;
      }
    })
    memberName.textContent = resData.data.name;
    patchMessage.textContent = "更新成功";
    
  } catch (error) {
    patchMessage.textContent = error.message;
  }
}

searchButton.addEventListener("click", get_memberInfo);
patchButton.addEventListener("click", patch_name)