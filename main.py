import cv2
from tkinter import*
import pytesseract
from PIL import Image
from tkinter.filedialog import*

letter = [
    'A','B','C','D','E','F','G','H','I','J','K',
    'L','M','N','O','P','Q','R','S','T','U','V',
    'W','X','Y','Z'
]
def tianjinlicense(licensenum):
    if len(licensenum) != 8:
        return False
    if licensenum[0] != '津': # 天津车牌的开头汉字
        return False
    if licensenum[1] not in letter:
        return False
    if licensenum[2] != '·':
        return False
    for i in range(3, 7):
        if licensenum[i].isdecimal() == False:
            return False
    return True

def chepaishibei():
    root = Tk()
    text = '车牌识别系统欢迎使用'
    root.title('车牌识别')
    var = StringVar(root)
    var.set('当前识别出来的车牌是：'+str(text))
    Label(root,textvariable = var).pack()
    root.mainloop()

cap = cv2.VideoCapture(0)
i = 0
while (1):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        filename = cv2.imwrite('D:/Python/' + str(i) + '.jpg', frame)
        i += 1
        print('已记录车牌。')
        text = pytesseract.image_to_string(Image.open(filename))
        chepaishibei()
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()