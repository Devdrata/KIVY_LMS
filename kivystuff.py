# Importing Modules
from kivy.utils import platform
from kivy.core.window import Window
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import *
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.spinner import SpinnerOption
import pickle

# Configuring Window Geometry
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'position', 'custom')
Config.write()
Window.top = 50
Window.left = 540


#Create File in case it does not exist:
f = open('data.dat','ab')
f.close()

class Invalid(Exception):
    " Used to Define a custom exception known as 'Invalid' "
    pass


# Creating Classes for all the screens along with behaviour for the various widgets.
class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.transit_scene, 3)
        
    def transit_scene(self, *args):
        
        
        self.manager.current = "main"
        return
        

class MainScreen(MDScreen):
    def add(self):
        self.manager.current = "add"

    def manip(self):
        self.manager.current = "manip"

    def search(self):
        self.manager.current = "search"

    def sa(self):
        self.manager.current = "sa"


class SaScreen(MDScreen):
    
    def set_spinnerres(self):
        self.lst_holder = []
        
        f = open('data.dat','rb')
        try:
            while True:
                var = pickle.load(f)
                if len(var)!=5:
                    continue
                self.lst_holder.append(str(var))
        except EOFError:
            pass
        if len(self.lst_holder) == 0:
            self.ids.allres.text = "Database is empty, please add entries first.".capitalize()
            self.ids.allres.values = []
        else:
            self.ids.allres.values = self.lst_holder
            self.ids.allres.text = "Click Here to see all entries in the form of a dropdown."
            
        f.close()        
class AddScreen(MDScreen):
    

    def createfile(self):
        lst = [self.ids.num.text, self.ids.pri.text, self.ids.auth.text, self.ids.nam.text, self.ids.quan.text]
        try:
            """We know that Book Number, Book Price and Book Quantity need to be positive integers.
           If they are not integers, the following Statements will raise an error which will be captured by the except statement
           thus showing a PopUp with the statement "Invalid Entry" """
            var = "Book Number"
            if int(self.ids.num.text) > 0:
                var = "Book Price"
                if int(self.ids.pri.text) > 0 :
                    var = "Book Quantity"
                    if int(self.ids.quan.text) > 0 :
                        pass
                    else:
                        raise Invalid()
                else:
                    raise Invalid()
            
            else:
                raise Invalid()

            if self.ids.auth.text == "" or self.ids.nam.text == "":
                popup = Popup(title="Error", content=Label(text=f'One OR More Entries Are Blank.',text_size = (self.width,None),halign = "center"),size_hint=(None, None), size=(400, 400),title_align = "center")
                popup.open()
                return
            f = open('data.dat','rb') 
            try:
                while True:
                    varnew = pickle.load(f)
                    if len(varnew) == 0:
                        break
                    if varnew[0] == self.ids.num.text:
                        popup = Popup(title='Error.', content=Label(text='Book Number Already Exists.',halign = "center"),
                              size_hint=(None, None), size=(400, 400),title_align = "center")
                        popup.open()
                        return
            except EOFError:
                f.close()
                pass


            with open('data.dat', 'ab+') as f:
                while True:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                    try:
                        varread = pickle.load(f)
                        
                        if varread[0] == lst[0]:
                            popup = Popup(title = "Error",content = Label(text = "Book Number Already Exists,\nPlease Check That It Is Unique For Each Entry.",halign = "center"),size_hint = (None,None),size = (400,400),halign = "center")
                            popup.open
                            break
                    except EOFError:
                        
                        break




                pickle.dump(lst, f)
                popup = Popup(title='Success.', content=Label(text='Record Successfully Added.',halign = "center"),
                              size_hint=(None, None), size=(400, 400),title_align = "center")
                popup.open()
        except ValueError: 
            popup = Popup(title='Error', content=Label(text=f'INVALID ENTRY.\n{var} Or More Entries are Non Integers Or Blank.\n Expecting Integer Value.', text_size= (self.width,None),halign = "center"),size_hint=(None, None), size=(400, 400),title_align = "center")
            popup.open()
            return
        except Invalid:
            popup = Popup(title="Error", content=Label(text=f'INVALID ENTRY.\n,"{var}" Or more entries are Negative.\nExpecting Positive Values for integer type fields.',text_size = (self.width,None),halign = "center"),size_hint=(None, None), size=(400, 400),title_align = "center")
            popup.open()
            return
            
        self.ids.num.text, self.ids.pri.text, self.ids.auth.text, self.ids.nam.text, self.ids.quan.text = ["","","","",""]
        

class ManipScreen(MDScreen):
    def delete(self):
        
        self.manager.current = "del"

    def update(self):
        self.manager.current = "update"





class DeleteScreen(MDScreen):
    lst2 = []
    lst3 = []
    lst4 = []
    def set_spinner(self):
        self.lst2 = []
        with open('data.dat', 'rb') as file:
            while True:
                try:
                    var = pickle.load(file)
                    if len(var)!=5:
                        continue
                    self.lst2.append(var[0])
                except EOFError:
                    break

        self.ids.my_spinner.values = self.lst2
        if len(self.ids.my_spinner.values) == 0:
            self.ids.my_spinner.values = []
            popup = Popup(title='Error', content=Label(text='DATABASE IS EMPTY. PLEASE ADD RECORDS FIRST.',halign = "center"),
                          size_hint=(None, None), size=(400, 400),title_align = "center")
            popup.open()

    def delfunc(self):
        with open('data.dat','rb') as f:
                while True:
                    try:
                        varnew = pickle.load(f)
                        if varnew[0] == self.ids.my_spinner.text:
                            
                            popup = Popup(title='Success!', content=Label(text=f"Entry containing Book Number {varnew[0]} has been deleted.",halign = "center"),
                                          size_hint=(None, None), size=(400, 400),title_align = "center")

                            popup.open()
                            
                            
                            
                            self.ids.my_spinner.text = ""
                            continue
                        self.lst4.append(str(varnew[0]))   
                        self.lst3.append(varnew)
              
                    except EOFError:
                        break
                        
                        
        with open('data.dat','wb') as f:
            for i in self.lst3:
                pickle.dump(i,f)
            pickle.dump(self.lst3,f)
            self.ids.my_spinner.values = self.lst4
class UpdateScreen(MDScreen):
    lst_book = []
    dataformat = ['Book Number','Price Of Book','Author Of Book','Name Of Book','Quantity Of Book']
    lst3 = []
    flag = None
    def spinner_set(self):
        self.lst3 = []
        with open('data.dat', 'rb') as file:
            while True:
                try:
                    var = pickle.load(file)
                    if len(var)!=5:
                        continue
                    self.lst3.append(var[0])
                except EOFError:
                    break

        self.ids.spin_num.values = self.lst3
        if len(self.lst3) == 0:
            self.ids.spin_num.values = []
            popup = Popup(title='Error', content=Label(text='DATABASE IS EMPTY. PLEASE ADD RECORDS FIRST.',halign = "center"),
                          size_hint=(None, None), size=(400, 400),title_align = "center")
            popup.open()
    

    def updat(self):
        bno = self.ids.spin_num.text
        by = self.ids.spin.text
        query = self.ids.newv.text
        f = open('data.dat','rb')
        try:
            while True:
                variread = pickle.load(f)
                if variread[0] == bno:
                    if by not in ['Author Of Book','Name Of Book']:
                        if int(query)<0:
                            raise Invalid
                    variread[self.dataformat.index(by)] = query                    
                    popup = Popup(title='SUCCESS!', content=Label(text=f'RECORD CONTAINING BOOK NUMBER {self.ids.spin_num.text}\nSUCCESSFULLY UPDATED.',halign = "center"),size_hint=(None, None), size=(400, 400),title_align = "center")
                    popup.open()
                self.lst_book.append(variread)
        except EOFError:
            return
        except (Invalid,ValueError):
            popup = Popup(title='ERROR', content=Label(text=f'Invalid Entry! Please Re-Check your entries..',halign = "center"),size_hint=(None, None), size=(400, 400),title_align = "center")
            popup.open()
            return
        f.close()
        with open('data.dat','wb') as f:
            for i in self.lst_book:
                pickle.dump(i,f)
                self.ids.spin_num.text = "Select Book Number To Update."


        self.ids.newv.text = ""
        self.ids.spin.text = "Select Value to be updated"
                
                        
                        










        

class SearchScreen(MDScreen):   
    dataformat = ['Book Number','Price Of Book','Author Of Book','Name Of Book','Quantity Of Book']
    def extr(self):
        self.lst = []
        f = open('data.dat','rb')
        try:
            while True:                                        
                var = pickle.load(f)
                self.lst.append(var)
                
                
                    
        except EOFError:
            f.close()
            if len(self.lst) == 0:
                popup = Popup(title='Error', content=Label(text='DATABASE IS EMPTY. PLEASE ADD RECORDS FIRST.',halign = "center"),size_hint=(None, None), size=(400, 400),title_align = "center")
                popup.open()
                
                    
    def srs(self):
        
        
        self.lstresult = []
        self.flag = False             
        
        
        
       
        for i in self.lst:
            
           
            if str(i[self.dataformat.index(self.ids.by.text)]).lower() == str(self.ids.query.text).lower():
                self.lstresult.append(str(i))                                
                self.flag = True
                
        if self.flag == True:
        
                self.ids.search_result.values = self.lstresult
                self.ids.search_result.text = "Select DropDown To View Results."
                
        if self.flag == False:
        
            self.ids.search_result.values = ["-"]
            self.ids.search_result.text = "No Results Found."
            

                
                       
                



            

# Creating Class For ScreenManager
class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)

    def on_key(self, window, key, *args):
        if key == 41 or key == 27:  # the esc key
            
            self.current = "main"
            return True
   

    

# Creating Class For The App
class LMSApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
         
   


# Running App Instance

LMSApp().run()


 
