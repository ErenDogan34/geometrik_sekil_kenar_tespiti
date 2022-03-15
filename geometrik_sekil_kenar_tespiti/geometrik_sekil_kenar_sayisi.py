import cv2

img =cv2.imread("sekiller.png")
img = cv2.resize(img,(300,300))
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gri,150,150)

counters, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in counters:
    area = cv2.contourArea(cnt)
    if area > 1000:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)
        cornerCount = len(approx)
        x,y,z,w = cv2.boundingRect(approx)
        if cornerCount >10:
            cv2.putText(img, "kose yok", (x + 15, y + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        cv2.putText(img,str(cornerCount),(x+14,y+14),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
        cv2.drawContours(img,cnt,-1,(0,255,0),3)

cv2.imshow("orijinal",img)

cv2.waitKey()