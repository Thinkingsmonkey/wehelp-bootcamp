// Task1
// 只使用一個 forEach 跑變數降低了時間複雜度
function findAndPrint(messages) {
  // 18、college、legal、vote
  // 取出 messages 的 value，對比是否有以上字串
  reg = /18|college|legal|vote/g;

  people = Object.entries(messages);
  people.forEach((el, index) => {
    if (el[1].split(reg).length > 1) {
      console.log(people[index][0]);
    }
  });
}
findAndPrint({
  Bob: "My name is Bob. I'm 18 years old.",
  Mary: "Hello, glad to meet you.",
  Copper: "I'm a college student. Nice to meet you.",
  Leslie: "I am of legal age in Taiwan.",
  Vivian: "I will vote for Donald Trump next week",
  Jenny: "Good morning.",
});

// Task2
function calculateSumOfBonus(data) {
  // total 以三人不超過 10000 為限，三人總薪水要小於 16.5W
  // rule：salary*0.05、ceo*1.1(其他都 1)、performance 1.1>1>0.9
  let total = 0;
  let rule = {
    performance: {
      "above average": 1.1,
      average: 1,
      "below average": 0.9,
    },
    role: {
      Engineer: 1,
      CEO: 1.1,
      Sales: 1,
    },
    salary: 0.05,
  };
  data.employees.forEach((employees, index) => {
    let salary = employees.salary;
    if (typeof salary === "number") salary = salary.toString();
    salary = salary.replace(",", "");
    if (salary.includes("USD")) salary = salary.replace("USD", "") * 30;

    total +=
      rule.salary *
      salary *
      rule.performance[employees.performance] *
      rule.role[employees.role];
  });

  console.log(total);
}
calculateSumOfBonus({
  employees: [
    {
      name: "John",
      salary: "1000USD",
      performance: "above average",
      role: "Engineer",
    },
    {
      name: "Bob",
      salary: 60000,
      performance: "average",
      role: "CEO",
    },
    {
      name: "Jenny",
      salary: "50,000",
      performance: "below average",
      role: "Sales",
    },
  ],
}); // call calculateSumOfBonus function

// Task3
function func(...data) {
  // 第二位與第二位相比，有相同加一
  // 迴避掉與自己相比
  // log 出 0 的表示只有自己

  // 利用哈希表
  // const secondCharMap = {};

  // for (const item of data) {
  //   const secondChar = item[1];

  //   if (secondCharMap[secondChar]) {
  //     secondCharMap[secondChar] = false;
  //   } else {
  //     secondCharMap[secondChar] = true;
  //   }
  // }

  // for (const item of data) {
  //   const secondChar = item[1];

  //   if (secondCharMap[secondChar]) {
  //     console.log(item);
  //     return;
  //   }
  // console.log("沒有");

  // 利用 Set() 元素單一的特性
  let secondCharSet = new Set();
  data.forEach((name) => {
    if (secondCharSet.has(name[1])) {
      secondCharSet.delete(name[1]);
      return;
    }
    secondCharSet.add(name[1]);
  });

  for (let name of data) {
    if (secondCharSet.has(name[1])) {
      console.log(name);
      return;
    }
  }
  console.log("no");
}
func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
// }

// Task4

// 偶數項：3n
// 基數項：3n+4
function getNumber(index) {
  if (index % 2 === 0) {
    console.log(3 * (index / 2));
  } else {
    console.log(3 * Math.floor(index / 2) + 4);
  }
}
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15

// Task5
function findIndexOfCar(seats, status, number) {
  // your code here
  // 在 status 迴圈中找出能夠載客的 index 給出 new Set()、S.add(index)
  // 在 seats 迴圈中 當 S.has(index) 時才去計算 number 與 seats 數量，給入一個 obj = {}，放 相減數量>0 : index
  // 使用 a = Object.keys(obj) 、if a.length === 0 log -1、num = Math.min(a)，log obj[num]
  let ableS = new Set();
  let ableO = {};
  status.forEach((e, index) => {
    if (e) {
      ableS.add(index);
    }
  });
  seats.forEach((e, index) => {
    if (ableS.has(index) && e - number >= 0) {
      let num = e - number;
      ableO[num] = index;
    }
  });
  let arr = Object.keys(ableO);
  if (arr.length === 0) {
    console.log(-1);
    return;
  }
  console.log(ableO[Math.min(...arr)]);
}
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
