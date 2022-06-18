import pikepdf
from tqdm import tqdm



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("\n\n\n\n\n\n\n")
f = open("ascii.json", "r")
file_contents = f.read()
print(bcolors.OKCYAN + file_contents + "\n\nby: redKatz" + bcolors.ENDC)
f.close()
print(bcolors.WARNING+"\n\n 𝙩𝙝𝙚 𝙖𝙪𝙩𝙝𝙤𝙧 𝙖𝙨𝙨𝙪𝙢𝙚𝙨 𝙣𝙤 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙞𝙡𝙞𝙩𝙮 𝙛𝙤𝙧 𝙝𝙤𝙬 𝙩𝙝𝙞𝙨 𝙘𝙤𝙣𝙩𝙚𝙣𝙩 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙪𝙨𝙚𝙙\n======================================================================="+bcolors.ENDC)

name_pdf = input("\n\nEnter the name of pdf file: ")
name_ps = input("\n\nenter the name of password list file: ")

password = [line.strip() for line in open(name_ps)]

for password in tqdm(password, bcolors.FAIL + "\n\nricerca password PDF" + bcolors.ENDC):
	try:
		with pikepdf.open(name_pdf,password = password) as pdf:
			print(bcolors.OKGREEN+"\n\nPassword trovata ", password+bcolors.ENDC)
			break
	except pikepdf._qpdf.PasswordError as e:
		continue
