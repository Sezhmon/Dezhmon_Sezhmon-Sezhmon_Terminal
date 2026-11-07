import webbrowser
import time
import random
import platform
import os
import json
from kivy.app import App


Language = "EN"

Folders = {}
Current_Path = []










def Languages(Input_FA, Input_EN):
			
			if Language == "EN":
				
				print(Input_EN)
			
			elif Language == "FA":
				
				print(Input_FA)


def Save_Folders():
    try:
        with open("folders.json", "w", encoding="utf-8") as f:
            json.dump(Folders, f, ensure_ascii=False)
    except Exception:
        pass

def Load_Folders():
    global Folders
    try:
        if os.path.exists("folders.json"):
            with open("folders.json", "r", encoding="utf-8") as f:
                Folders = json.load(f)
    except Exception:
        pass

Load_Folders()








def Where_Am_I():
    
    d = Folders
    
    for p in list(Current_Path):
        
        if isinstance(d, dict) and p in d:
            
            d = d[p]
            
        else:
            
            Current_Path.clear()
            
            return Folders
            
    return d





def Command_Site():
    webbrowser.open("https://sezhmon.github.io/Sezhmon_Site/")
    print("\n Site Has Opened")



def Command_Language():
	
	global Language
	
	if Language == "EN":
		
		Language = "FA"
	
	
	elif Language == "FA":
		
		Language = "EN"
	
	
	print("System Language =", Language)



def fmt(b):
    return f"{b / (1024**3):.1f} GB"


def Command_Screen_Saver():
    
    for i in range(24):
        print("0")




def Command_Time():
    
    Local_Time = time.localtime()
    
    Time = time.strftime("%H:%M:%S", Local_Time)
    
    print(Time)



def Command_Exit():
    
    from kivy.app import App
    App.get_running_app().stop()





def Command_Matrix():
    
    Matrix = ""
    Loop = random.randint(24, 1240)
    
    for i in range(Loop):
        
        Matrix_Int = random.randint(0, 1)
        
        Matrix += str(Matrix_Int)
    
    print(Matrix)




def Command_Help():
    
    Commands = ""
    
    for CMD in Commands_Table:
        
        Commands += CMD +"   |||   "
        
    print(Commands)





def Command_Info():
    
    print("\nSezhmon Terminal")
    print("Version = 1.0.0 Pre Releses")
    print("Sezhmon , A Code World")
    print("")
    print("Powerd By : python3==3.11.6,hostpython3==3.11.6,kivy==2.3.0,pillow==10.4.0,plyer")





def Command_Coin():
    
    print(random.choice(["Shir", "Khat"]))




def Command_System():
	
    try:
        from jnius import autoclass, cast
        Build = autoclass('android.os.Build')
        Version = autoclass('android.os.Build$VERSION')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity

        ActivityManager = autoclass('android.app.ActivityManager')
        MemoryInfo = autoclass('android.app.ActivityManager$MemoryInfo')
        am = cast('android.app.ActivityManager',
                 activity.getSystemService(activity.ACTIVITY_SERVICE))
        mem = MemoryInfo()
        am.getMemoryInfo(mem)

        if Language == "FA":
            Infos = {
                "سازنده": str(Build.MANUFACTURER),
                "مدل": str(Build.MODEL),
                "نسخه اندروید": str(Version.RELEASE)+ "\n",
                "رم کل": fmt(mem.totalMem),
                "رم آزاد": fmt(mem.availMem),
            }
        else:
            Infos = {
                "Creator": str(Build.MANUFACTURER),
                "Model": str(Build.MODEL),
                "Android Version": str(Version.RELEASE),
                "RAM": fmt(mem.totalMem),
                "Free RAM": fmt(mem.availMem)+ "\n",
            }
        print(Infos)
        return "<------Sezhmon Device Info------>" + str(Infos)

    except Exception:
        u = platform.uname()
        print(f"{u.system} {u.release} {u.machine}")





def Command_Clear():
     
     pass







def Command_Echo(Args):
     
     if not Args:
     	
     	print("")
     	
     	return
     
     print(" ".join(Args))
     
     return



def Command_GYP(Args):
     
     if Language == "FA":
     	
     	Gol = random.choice(['چپ', 'راست'])
     
     if Language == "EN":
     	
     	Gol = random.choice(['left', 'right'])
     
     User_Choice = Args[0].lower() if Args else ""
     
     if not Args:
     	
     	print("Retype Command")
     	
     	return
     
     elif User_Choice == Gol:
     	
     	print("You Victory")
     	
     	return
     
     else:
     	
     	print("Defeat")
     	
     	return







def Command_Old_Language():
     
     pass




def Command_Normal_Language():
     
     pass







def Command_Mad(Args = None):
     
     if not Args:
     	
     	if Language == "EN":
     		
     		print("Retype Command And Type Folder Name")
     	
     	if Language == "FA":
     		
     		print("دستور را دوباره بنویسید و رو‌به‌روی دستور نام پوشه را نیز وارد فرمایید .")
     	
     	return
     
     
     Name = Args[0]
     Inside = Where_Am_I()
     
     
     if Name in Inside:
     	
     	print("Exists")
     	
     	return
     
     Inside[Name] = {}
     
     Save_Folders()
     
     if Language == "EN":
     	
     	print("Folder Created")
     	
     if Language == "FA":
     	
     	print("پوشه ساخته شد")




def Command_Wf(Args = None):
     		
     		Inside = Where_Am_I()
     		List_Dirs = ""
     		List_Files = ""
     		
     		
     		Names = ""
     		
     		if not Inside:
     			
     			if Language == "EN":
     				
     				print("Not Find File Or Dir")
     				
     			elif Language == "FA":
     				
     				print("پوشه و یا داده ای پیدا نشد")
     			
     			return
     		
     		
     			
     		for Name, Val in Inside.items():
     		     
     		     if isinstance(Val, dict):
     		     	
     		     	List_Dirs += f"[dir] {Name}   /|\   "
     		     
     		     else:
     		     	
     		     	List_Files += f"[file] {Name}   /|\   "
     		     	
     		print(List_Dirs)
     		print("")
     		print(List_Files)











def Command_Det(Args=None):
    
    if not Args:
        
        if Language == "EN":
            
            print("Retype Command And Type Folder Name")
            
            
        elif Language == "FA":
            
            print("دستور را دوباره بنویسید و روبه‌روی دستور نام پوشه را نیز وارد فرمایید .")
            
        return

    Name = Args[0]
    Inside = Where_Am_I()

    if Name not in Inside:
        
        if Language == "EN":
            
            print("Not Find Folder")
            
        elif Language == "FA":
            
            print("چنین پوشه‌ای پیدا نشد")
            
        return

    del Inside[Name]
    Save_Folders()

    if Language == "EN":
    	
    	print("Folder Deleted")
    
    elif Language == "FA":
    	
    	print("پوشه حذف شد")









def Command_Gt(Args=None):
    
    global Current_Path
    
    if not Args:
        
        if Language == "EN":
            
            print("Retype Command And Type Folder Name")
        else:
            print("اسم پوشه را هم بنویسید")
        return
    
    
    Inside = Where_Am_I()
    Name = Args[0]
    
    if Name in Inside and isinstance(Inside[Name], dict):
        
        Current_Path.append(Name)
        print(Name)
        
    else:
        
        if Language == "EN":
            
            print("Not Find Folder")
            
        elif Language == "FA":
            
            print("چنین پوشه‌ای پیدا نشد")
            
        return





def Command_Bk(Args=None):
    
    global Current_Path
    
    if Current_Path:
    	
    	Current_Path.pop()
    	
    	if Language == "EN":
    		
    		print("Back to root")
    	
    	elif Language == "FA":
    		
    		print("برگشتید به ریشه")
     	
     	
     
     
     
     
def Command_Maf(Args=None):
     	
    if not Args:
        
        if Language == "EN":
            
            print("Retype Command And Type File Name")
            
        elif Language == "FA":
            
            print("اسم فایل را هم بنویسید")
            
        return

    Name = Args[0]
    Text = " ".join(Args[1:]) if len(Args) > 1 else ""
    Inside = Where_Am_I()

    if Name in Inside:
        
        print("Exists")
        
        return

    Inside[Name] = Text
    Save_Folders()

    if Language == "EN":
        
        print("File Created")
        
    elif Language == "FA":
        
        print("داده ساخته شد")









def Command_Ref(Args=None):
    
    if not Args:
        
        if Language == "EN":
            
            print("Retype Command And Type File Name")
            
        elif Language == "FA":
            
            print("اسم فایل را هم بنویس")
            
        return

    Name = Args[0]
    Inside = Where_Am_I()

    if Name not in Inside:
        
        if Language == "EN":
            
            print("Not Find File")
            
        elif Language == "FA":
            
            print("چنین فایلی پیدا نشد")
            
        return

    Val = Inside[Name]

    if isinstance(Val, dict):
        
        if Language == "EN":
            
            print("This is folder, use gt")
            
        elif Language == "FA":
            
            print("این پوشه است، با gt برو داخلش")
            
        return

    if Val == "":
        
        print("(Empty)")
        
    else:
        
        print(Val)









def Command_Edf(Args=None):
    
    if not Args or len(Args) < 2:
        
        if Language == "EN":
            
            print("Retype Like: edf salam new-text")
            
        elif Language == "FA":
            
            print("مثل این بنویسید: edf salam متن-جدید")
            
        return

    Name = Args[0]
    Text = " ".join(Args[1:])
    Inside = Where_Am_I()

    if Name not in Inside:
        
        if Language == "EN":
            
            print("Not Find File")
            
        elif Language == "FA":
            
            print("اینچنین داده‌ای پیدا نشد")
            
        return

    if isinstance(Inside[Name], dict):
        
        if Language == "EN":
            
            print("This is folder, use gt")
            
        elif Language == "FA":
            
            print("این پوشه است، فایل نیست")
            
        return

    Inside[Name] = Text
    Save_Folders()

    if Language == "EN":
        
        print("File Edited")
        
    elif Language == "FA":
        
        print("فایل ویرایش شد")









def Command_Font_Size(Args):
	
	Apps = App.get_running_app()
	
	if not Args:
		
		if Language == "EN":
			
			print("Retype Command And Type Font Size")
		
		elif Language == "FA":
			
			print("دستور را دوباره وارد کنید و اندازه واژه ها را نیز جلوی ان بنویسید")
		
		
		return
	
	
	Font_Size = Args[0]
	
	try:
		
		Font_Size = float(Font_Size)
		
	
	except:
		
		Languages("لطفا عدد و یا عدد ممیز دار وارد فرمایید", "Enter a int or float")
		
		return
	
	
	try:
		
		Apps.Terminal_Label.font_size = Font_Size
	
	except:
		
		print("Error 404")



	
		


	

Commands_Table = {
    "/site": Command_Site,
    "/help": Command_Help,
    "/info": Command_Info,
    "matrix": Command_Matrix,
    "snc": Command_Screen_Saver,
    "time": Command_Time,
    "exit": Command_Exit,
    "coin": Command_Coin,
    "langu": Command_Language,
    "sysinfo": Command_System,
    "clear": Command_Clear,
    "echo": Command_Echo,
    "gyp": Command_GYP,
    "old-langu": Command_Old_Language,
    "normal-langu": Command_Normal_Language,
    "mad": Command_Mad,
    "wf": Command_Wf,
    "det": Command_Det,
    "gt": Command_Gt,
    "bk": Command_Bk,
    "maf": Command_Maf,
    "ref": Command_Ref,
    "edf": Command_Edf,
    "font-size": Command_Font_Size,
    
}

def Commands(User_Input):
    
    Parts = User_Input.strip().split()
    if not Parts:
        return ""
    Cmd = Parts[0].lower()
    Args = Parts[1:]
    
    Action = Commands_Table.get(Cmd)
    
    
    
    if Action:
        try:
            try:
                Result = Action(Args)
            except TypeError:
                Result = Action()
            return Result if Result is not None else ""
        except Exception as e:
            Output = f"Error: {e}"
            print(Output)
            return Output
    else:
        Output = f"\nError : {User_Input} Not Found \n"
        print(Output)
        return Output