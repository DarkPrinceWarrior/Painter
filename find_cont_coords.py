import cv2

def find_contours():

    img = cv2.imread('images/horseshoe.jpg')
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # threshold defined manually its up to image
    ret, thresh = cv2.threshold(img_gray, 169,255,0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contList = []
    max1_cont = 0

    # находим длину конутра рамки
    for i in contours:
        if max1_cont < len(i):
            max1_cont = len(i)

    for i in contours:
        # минимальное число - defined manually (чтобы не взять отдельно лежащие точки)
        # и исключаем рамку из контуров
        if 46 < len(i) < max1_cont:
            contList.append(i)

    return contList