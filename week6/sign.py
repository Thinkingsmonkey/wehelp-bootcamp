# 註冊帳號
def signup(data, collection):
    checked = check_member(data, collection)
    if checked:
        return "This e-mail has already been registered, please try another one。"
    insert(data, collection)
    return "Congratulations, registration is successful"

# 添加帳號
def insert(data, collection):
    collection.insert_one({
    "nickName": data["nickName"],
    "password": data["password"],
    "username": data["username"]
})

# 檢查是否存在此帳號
def check_member(data, collection):
    result = collection.find_one({"username": data["username"]})
    if result:
        return True
    else:
        return False
    
# 登入帳號
def signin(data, collection):
    result = check_member_password(data, collection)
    if result != None:
        return "Congratulations, you have successfully logged in"
    return "Username or password is not correc"

# 檢查帳號密碼
def check_member_password(data, collection):
    return collection.find_one({
        "$and": [
            {"username": data["username"]},
            {"password": data["password"]}
        ]
    })

# 取得暱稱
# def get_nickName(data, collection):
#     doc = collection.find_one({
#         "username": data["username"]
#     })
#     return doc