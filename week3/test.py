def getTitles(page, num) :
    # 創一個空物件，空物件將參數當作 key，賦予需要的值
    # 回傳該物件
    variable = {}
    variable[page +"_titles"] = f'11111 {num}'
    variable[page] = [1234]
    return variable



test = getTitles("page1",1)
print(test["page1_titles"])


# for i in range(1,10):
#     locals()['number'+str(i)] = i
#     print('Print In Once: ', type(locals()['number'+str(i)]))