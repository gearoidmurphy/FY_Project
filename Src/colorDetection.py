import cv2 
import numpy as np

boundaries = [
	([17, 15, 100], [50, 56, 200], 11040),
	([86, 31, 4], [220, 88, 50] , 21012),
	([25, 146, 190], [62, 174, 250], 3),
	([103, 86, 65], [145, 133, 128], 4)
]
# colorlist = [["RED",0, 0, 130,1],["BLUE",255, 0, 0,2]]
def getTagNumberbyColor(camera):
    while True:
        if camera.isOpened():
            ret,frame = camera.read()
            if ret:
                #ret, buffer = cv2.imencode('.jpg',frame)
                cv2.imwrite('color.png', frame)
                #frame = buffer.tobytes()
                frame = cv2.imread('color.png', cv2.IMREAD_UNCHANGED)
                w, h, _ = frame.shape
                # w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
                # h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
                for (lower, upper , tagnumber) in boundaries:
                    # create NumPy arrays from the boundaries
                    lower = np.array(lower, dtype = "uint8")
                    upper = np.array(upper, dtype = "uint8")
                    # find the colors within the specified boundaries and apply
                    # the mask
                    mask = cv2.inRange(frame, lower, upper)
                    if 255 in mask[:, w]:
                        return tagnumber
                # for x in range(w):
                #     for y in range(h):
                #         b,g,r = (frame[x,y])
                #         for i in colorlist:
                #             if b == i[2] & g == i[3] & r == i[4]:
                #                 return i[5]
