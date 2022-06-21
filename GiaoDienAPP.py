import tkinter as tk
from tkinter import *
import tkinter.ttk as exTk
import cv2
import time
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import PIL.Image, PIL.ImageTk
from cv2 import waitKey 

# TẠO MÀN HÌNH LOAD (CHÀO)
class DemoSplashScreen: 
    def __init__(self, parent): 
        self.parent = parent 
        self.aturSplash() 
        self.aturWindow() 

    def aturSplash(self): 
        self.gambar = Image.open('./2.jpg')
        self.imgSplash = ImageTk.PhotoImage(self.gambar)

    def aturWindow(self):
        lebar, tinggi = self.gambar.size 
        setengahLebar = (self.parent.winfo_screenwidth()-lebar)//2 
        setengahTinggi = (self.parent.winfo_screenheight()-tinggi)//2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setengahLebar,setengahTinggi))
        Label(self.parent, image=self.imgSplash).pack()

if __name__ == '__main__': 
    win = Tk()
    win.overrideredirect(True) 
    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=10000, mode='determinate') 
    progressbar.pack(side="bottom") 
    app = DemoSplashScreen(win) 
    progressbar.start()
    win.after(2000, win.destroy) 
    win.mainloop()

# Dùng hàm VideoCapture của OpenCV để mở video, 
# lấy kích thước chiều cao và chiều rộng
class MyVideoCapture:
    def __init__(self, video_source):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source",video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)//2
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)//2

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            frame = cv2.resize(frame,(640,480))
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret,None)

#####################
""" class App:
    def __init__(self, window, window_title,video_source = 0, fpsLimit = 30):

        self.window = window

        self.video_source = video_source
        self.fpsLimit = fpsLimit

        self.vid = MyVideoCapture(video_source)    
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        self.btn_getvideo=tkinter.Button(window, text="getvideo", width=50, command=self.getvideo)
        self.btn_getvideo.pack(anchor=tkinter.CENTER, expand=True)
        self.delay = 1
        self.update()

        self.window.mainloop()
    def getvideo(self):
        start_time = time.time()
        out = cv2.VideoWriter('output_'+time.strftime("%d-%m-%Y-%H-%M-%S")+'.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))

        while int(time.time()-start_time) < self.fpsLimit:           
            ret, frame = self.vid.get_frame()
            if ret:
                out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            else:
                break
        out.release()
        # tkinter.messagebox.showinfo(title="Notification", message="save video successful")
        print("success")
        cv2.destroyAllWindows()


    def update(self):
        ret, frame = self.vid.get_frame()
        frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)
        


 """
# Tạo phiên bản
win = Tk()  
scrW = win.winfo_screenwidth ()
scrH = win.winfo_screenheight() 
dai = 800
rong = 600

# Tạo GUI và căn giữa
win.geometry ('%dx%d+%d+%d' % (dai, rong, scrW/2-dai/2, scrH/2-rong/2))
win.configure(bg="#075A54")
# Thêm tiêu đề      
win.title("App Nhan Dien")  
win.iconbitmap('D:\__Monhoc\DAcdt\GUI_TUAN_5/LOGOico.ico')


def clickbtnSTART():
    cap = cv2.VideoCapture(0)
    time.sleep(1.0)
    if not cap.isOpened:
        print('cmaera dnag duoc mo')
        exit(0)
    cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)
    while True:
        ret, frame = cap.read()
        if frame is None:
            print('khong doc duoc frame')
            break
        #frame = cv.flip(frame,1)
        cv2.imshow('Video',frame)
        key = waitKey(30)
        if key == 27:
            break
        if key == ord('s') or key == ord('S'):
            st= time.localtime()
            filename = 'Hinh_%04d_%02d_%02d_%02d_%02d_%02d.jpg' \
            % (st.tm_year, st.tm_mon, st.tm_mday,st.tm_hour,st.tm_min,st.tm_sec)
            cv2.imwrite(filename, frame)
    cv2.destroyAllWindows()

def clickbtnSTOP():
    btnSTOP.config(bg="white", fg="black",state="disable")
    btnSTART.config( bg="green", fg="white",state=NORMAL)
    btnTURNON.config(state="disable")
    cmbCAMERA.set('')
    canvas = Canvas (win, width = canvas_w, height= canvas_h, bg= "red").place(x=400, y=110 )

def clickbtnEMERGENCY():
    btnSTART.config( bg="green", fg="white",state=NORMAL)
    btnSTOP.config( bg="red", fg="white",state="disable")
    cmbCAMERA.set('')
    btnTURNON.config(state="disable")
    canvas = Canvas (win, width = canvas_w, height= canvas_h, bg= "red").place(x=400, y=110 )
    btnEMERGENCY['state']="disable"

def clickbtnTURNON():
    camera = cmbCAMERA.get()
    if camera == "Webcam":
        canvas = Canvas (win, width = canvas_w, height= canvas_h, bg= "gray").place(x=400, y=110 )


Label(win, text="Button Start:   ", font=("Roboto", 12,"bold", "italic"), bg="#075A54", fg="white", width=16, height=1, justify=LEFT).place(x= 0, y = 30)
Label(win, text="Button Stop:    ", font=("Roboto", 12, "bold", "italic"), bg="#075A54", fg="white", width=16, height=1, justify=LEFT).place(x= 0, y = 90)
Label(win, text="EMERGENCY:      ", font=("Roboto", 12, "bold", "italic"), bg="#075A54", fg="white", width=16, height=1, justify=LEFT).place(x= 0, y = 150)

# Nút START
btnSTART = Button (win, text="START", font=("Roboto", 14, "bold"), bg="green", fg="white", width=8, height=1, command=clickbtnSTART)
btnSTART.place(x= 160, y = 25) 

# Nút STOP
btnSTOP = Button (win, text="STOP", font=("Roboto", 14, "bold"), state="disable", bg="red", fg="white", width=8, height=1, command=clickbtnSTOP)
btnSTOP.place(x= 160, y = 85) 
 

# Nút EMERGENCY
btnEMERGENCY = Button (win, text="EMERGENCY", font=("Roboto", 14, "bold"), state="disable", bg="blue", fg="white", width=12, height=1, command=clickbtnEMERGENCY)
btnEMERGENCY.place(x= 135, y = 140) 


# Nút exit
btnEXIT = Button (win, text="EXIT", font=("Roboto", 10, "bold"), bg="gray", fg="white", width=6, height=1, command=quit)
btnEXIT.place(x=700, y = 550) 

# Nút TURN ON CAMERA
btnTURNON = Button (win, text="TURN ON", font=("Roboto", 10, "bold"), bg="#5AC1C3", fg="white", width=10, height=1, state= "disable", command=clickbtnTURNON)
btnTURNON.place(x= 650, y = 70) 

# COMBOBOX
cmbCAMERA = exTk.Combobox (win,width=30, font = ('Roboto', 10, "italic"), state='readonly')
cmbCAMERA.place(x= 400, y = 70)
cmbCAMERA ['values'] = ('Webcam', 'Camera 1', 'Camera 2')

#CAMERA
Label(win, text="Lựa chọn Camera:", font=("Roboto", 14,"italic", "bold"), bg="#075A54", fg="white", width=14, height=1).place(x= 400, y = 30)
video = cv2.VideoCapture (0)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH) // 2
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2
canvas = Canvas(win, width = canvas_w, height= canvas_h, bg= "white").place(x=400, y=110 )

#App(win, 0,10)
win.mainloop ()

