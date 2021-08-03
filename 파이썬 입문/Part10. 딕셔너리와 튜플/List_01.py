def check_and_clear(box):
    if '불량품' in box.keys() :
        box.clear()     
        print(box)
    else :
        print(box)

box1 = {"불량품" : 10}
check_and_clear(box1)

box2 = {"정상품": 10}
check_and_clear(box2)
