# key board input test

import Tkinter

def key(event):

    if event.keysym=='Escape':
        root.destroy()

    if event.char==event.keysym:
        if event.char.lower()=='a':
            print "a"
        else:
            print("Normal key %r" % event.char)
    elif len(event.char)==1:
        print("Punctuation key %r (%r)" % (event.keysym, event.char))
    else:
        print("Special Key %r" % event.keysym)

root=Tkinter.Tk()
print( "press a key (escape to quit): ")
root.bind_all('<Key>',key)
#root.withdraw()
root.mainloop()
