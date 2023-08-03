# week5 作業截圖

- 要求一與二：創建並使用 website database

   ![image.png](./week5%20作業截圖-assets/image.png)

   - 建立資料庫和資料表

      ![image 1.png](./week5%20作業截圖-assets/image%201.png)

- 要求三：

   - 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。

      ![image 2.png](./week5%20作業截圖-assets/image%202.png)

      

   - 接著繼續新增⾄少 4 筆隨意的資料。

   - 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。

      ![image 3.png](./week5%20作業截圖-assets/image%203.png)

   

   - 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

      ![image 4.png](./week5%20作業截圖-assets/image%204.png)

   

   - 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 \~ 4 筆資料 )

      ![image 5.png](./week5%20作業截圖-assets/image%205.png)

      

   - 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。

      ![image 6.png](./week5%20作業截圖-assets/image%206.png)

      

   - 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

      ![image 7.png](./week5%20作業截圖-assets/image%207.png)

   - 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

      ![image 8.png](./week5%20作業截圖-assets/image%208.png)

- 要求四：

   - 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

      ![image 9.png](./week5%20作業截圖-assets/image%209.png)

      

   - 取得 member 資料表中，所有會員 follower_count 欄位的總和。

   - 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

      ![image 10.png](./week5%20作業截圖-assets/image%2010.png)

- 要求五：SQL JOIN

   - 建立新資料表紀錄留⾔資訊，取名字為 message

      ![image 11.png](./week5%20作業截圖-assets/image%2011.png)

      ![image 12.png](./week5%20作業截圖-assets/image%2012.png)

   - 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。

      ![image 13.png](./week5%20作業截圖-assets/image%2013.png)

   - 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者的姓名。

      ![image 14.png](./week5%20作業截圖-assets/image%2014.png)

   - 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。

      - 先更新按讚數

         ![image 15.png](./week5%20作業截圖-assets/image%2015.png)

      - 查詢按讚平均值

         ![image 16.png](./week5%20作業截圖-assets/image%2016.png)

      


