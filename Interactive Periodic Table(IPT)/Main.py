import tkinter
import PTable

def main():
    root = tkinter.Tk()
    a = PTable.App(root)
    a.grid(row=0, column=0, sticky='nsew') 
    a.mainloop()


# runs main function
if __name__ == "__main__": 
    main()
