from tkinter import *
from pytube import YouTube
from tkinter import messagebox

def video_download():
    try:
        url = name_var.get()
        if not url:
            messagebox.showerror("Error", "Please enter a valid YouTube URL.")
            return


        video = YouTube(url)
        video_stream = video.streams.get_highest_resolution()
        title = video.title
        video_stream.download()
        messagebox.showinfo("Download Complete", f"Video '{title}' has been downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
window=Tk()
window.title("Youtube Downloader")
name_var=StringVar()

Label(window,text="Enter URL").grid(row=0,column=0,padx=5,pady=5)
Entry(window,textvariable=name_var).grid(row=0,column=1,padx=5,pady=5)
Button(window,text="Download",bg="green",command=video_download).grid(row=1,column=1,padx=5,pady=5)
Button(window,text="Close",bg="red",command=window.destroy).grid(row=2,column=1,padx=5,pady=5)

window.mainloop()


