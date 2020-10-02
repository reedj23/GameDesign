Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> strVar=" Here are the instructions to install Drivers 1. After the download is completed go to where you saved the folder. (By default everything you download from the Internet is saved to the Downloads folder) 2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again. 3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon. 4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:*setup application*Asussetup*pnpinstal64*pnputil*Igxpin 5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up."
print(len(strVar))
indexNum = strVar.find("Drivers")
print(strVar.replace('Extract', 'EXTRACT'))
print(strVar.replace('setup', 'SETUP'))
indexNum = strVar.find("\n")
