import tkinter as tk
from tkinter import filedialog
import keras
import numpy as np
from keras.preprocessing import image
model = keras.models.load_model('/home/niharika/Desktop/ML_Project/CNN/CNN_trained_model(2).model')


from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("CNN Model")
        self.pack(fill=BOTH, expand=1)
        
        button = tk.Button(root, text='Upload Image', width=25, command=self.upload_img)
        button.pack()
        
        button = tk.Button(root, text='Exit', width=25, command=self.client_exit)
        button.pack()
        
    def upload_img(self):
        file_path = filedialog.askopenfilename()
        test_image = image.load_img(file_path, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        
        if result[0][0] == 1:
            prediction = 'dog'
        else:
            prediction = 'cat'
        
               
        self.showImg(file_path,prediction)
                
        
    def showImg(self,file_path,prediction):
        
        load = Image.open(file_path)
        load = load.resize((250, 250), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image = render)
        img.image = render
        img.place(x = 75, y=0)
        text = Label(self,text ="PREDICTION: " + prediction)
        text.pack()
      
       
    
    def client_exit(self):
        root.destroy()
        
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
        


