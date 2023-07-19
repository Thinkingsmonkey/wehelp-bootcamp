pageDic = {"url": "example.com", "next_page_url": None, "page_bs4_root": None}
b = pageDic
c = pageDic
print( b == pageDic, c == b, c == pageDic)
def update_pageDic():
    return {"url": "new_url", "next_page_url": "next_page_url", "page_bs4_root": "new_bs4_root"}

pageDic = update_pageDic()
print( b == pageDic, c == b, c == pageDic)

b.update(update_pageDic())
print(b == pageDic, c == b, c == pageDic)
