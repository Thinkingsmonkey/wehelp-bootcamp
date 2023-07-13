# Task1
print("Task1：雙重 for 迴圈，O(n^2)")

def find_and_print(messages):
# 
    for str in messages:
        for over in ["18", "college ", "legal", "vote"]:
            if over in messages[str]:
                print(str)

find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})

# Task2
print("\nTask2：一個 for 迴圈，O(n)")
def calculate_sum_of_bonus(data):
# bonus = role * performance * (salary*5%)
# role = {CEO: 1.3, Engineer:1.2, Sales: 1.2}
# performance = {above average: 1.3, average: 1.1, below average: 0.9}
    role = {"CEO": 1.3, "Engineer":1.2, "Sales": 1.2}
    performance = {"above average": 1.3, "average": 1.1, "below average": 0.9}
    dic = data["employees"]
    bonus = 0
    # print(type(dic[0]["salary"]) == str)
    for employee in dic:
        if type(employee["salary"]) == int:
            employee["salary"] = str(employee["salary"])
        if "," in employee["salary"]:
            employee["salary"] = employee["salary"].replace(",", "")
        # 會轉換為 int 的部分必須要放在後面，否則會導致後面出現 "int" 無法被遍歷
        if "USD" in employee["salary"]:
            employee["salary"] = int(employee["salary"].replace("USD", "")) * 30
        bonus = bonus + ((int(employee["salary"]) / 20) * performance[employee["performance"]] * role[employee["role"]])
    print(bonus)


calculate_sum_of_bonus({
    "employees":[
        {
            "name":"John",
            "salary":"1000USD",
            "performance":"above average",
            "role":"Engineer"
        },
        {
            "name":"Bob",
            "salary":60000,
            "performance":"average",
            "role":"CEO"
        },
        {
            "name":"Jenny",
            "salary":"50,000",
            "performance":"below average",
            "role":"Sales"
        }
    ]
}) # call calculate_sum_of_bonus function

# Task3
print("\nTask3：雙重 for 迴圈，O(n^2)")
def func(*data):
    unique = False
    for name1 in data:
        sameNumber = 0
        for name2 in data:
            if name1[1] == name2[1]:
                sameNumber += 1
        if sameNumber == 1:
            unique = True
            print(name1)

    if unique == False:
        print("沒有")

func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

# Task4
print("\nTask4：O(1)")

def get_number(index):
# your code here
    if index%2 == 0:
        print(int(3 * (index / 2)))
    else:
        print(int((3 * ((index + 1) / 2)) + 1))
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

# Task5
print("\nTask5：都是單個 for 迴圈，O(n)")
def find_index_of_car(seats, status, number):
# your code here
    dic = {}
    keyList = []
    valueList = []
    noNum = 0
    for index, available in enumerate(status):
        if available != 1:
            continue
        if (seats[index] - number) < 0:
            dic[index] = 100
        else:
            dic[index] = seats[index] - number
    for value in dic.values():
        valueList.append(value)
        if value == 100:
            noNum += 1
    for key in dic.keys():
        keyList.append(key)
    fitNum = min(valueList)
    if noNum == len(dic):
        print(-1)
    else:
        print(keyList[valueList.index(fitNum)])
    # print(dic, keyList, valueList, (min(valueList)), keyList[valueList.index(fitNum)])
find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 5) # print 2

# Additional Task1
print("\nAdditional Task1：雙重 for 迴圈，O(n^2)")
def max_product(nums):
    # 兩兩相乘後所有結果組成新 list
    # 找出 list 中最大數
  lis = []
  for index1, num1 in enumerate(nums) :
      for index2, num2  in enumerate(nums):
        if index1 == index2: 
          continue
        if num1*num2 in lis:
            continue
        lis.append(num1 * num2)
  for index in range(len(lis)-1):
    if lis[index] > lis[index+1]:
      lis[index],lis[index+1] = lis[index+1], lis[index]
  print(lis[len(lis) - 1])

max_product([5,20,2,6]) # 120
max_product([10,-20,0,3]) # 30
max_product([10,-20,0,-3]) # 60
max_product([-1,2]) # -2
max_product([-1,0,2]) # 0
max_product([5,-1,-2,0]) # 2
max_product([-5,-2]) # 10

# Additional Task2
print("\nAdditional Task2：雙重 for 迴圈，O(n^2)")
def twoSum(nums, target):
  # 跑迴圈兩兩相加
  # 找出 target = num1 + num2
  # 若 lis 已經有 index1, index2 跳過
  # 若 index1 = index2 跳過
  # 將 index1, index2 append 到 lis 中
  # print index1, index2
  lis = []
  for index1, num1 in enumerate(nums):
      for index2, num2 in enumerate(nums):
          if index1 == index2: continue
          if index1 in lis or index2 in lis: continue
          if num1 + num2 == target:
              lis.append(index1)
              lis.append(index2)
  return lis
result = twoSum([2, 11, 7, 15], 9)
print(result); # show [0,2]
