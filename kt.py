import os, base64, sys, time
from pprint import pformat
alphabet = [
"\U0001f600",
"\U0001f603",
"\U0001f604",
"\U0001f601",
"\U0001f605",
"\U0001f923",
"\U0001f602",
"\U0001f609",
"\U0001f60A",
"\U0001f61b",
]
MAX_STR_LEN = 70
OFFSET = 10
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"
ask = green + '\n[' + white + '-' + green + '] '+ yellow
success = green + '\n[' + white + '✓' + green + '] '
error = red + '\n[' + white + '!' + red + '] '
info= yellow + '\n[' + white + '+' + yellow + '] '+ cyan
pwd=os.getcwd()
logo=f'''
{blue}████████████████████████████████████████████████████████
{red}█─▄─▄─█▄─▀█▄─▄█░▄▄░▄█▀▀▀▀▀██─▄─▄─█─▄▄─█─▄▄─█▄─▄███─▄▄▄▄█
{yellow}███─████─█▄▀─███▀▄█▀██████████─███─██─█─██─██─██▀█▄▄▄▄─█
{red}▀▀▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
{blue}████████████████████████████████████████████████████████
{cyan}                    [ @By iTenzz ]
'''
def sprint(sentence, second=0.04):
for word in sentence + '\n':
sys.stdout.write(word)
sys.stdout.flush()
time.sleep(second)
def about():
os.system("clear")
sprint(logo, 0.01)
print(f"{cyan}[ToolName]  {purple} :[ Tnz Tools ]")
print(f"{cyan}[Version]   {purple} :[ 1.0 ]")
print(f"{cyan}[SourceScript]   {purple} :[ SukitooV1 ]")
print(f"{cyan}[Github]    {purple} :[ https://github.com/ilham040307 ]")
print(f"{cyan}[Telegram]     {purple} :[ @SukitooV1 ]\n")
ret=input(ask+"1 Back Menu | 0 For Exit  > "+green)
if ret=="1":
main()
else:
exit()
def mover(out_file):
move= input(ask+"Pindah ke Folder Lainnya?(y/n) > "+green)
if move=="y":
mpath=input(ask+"Enter the path > "+ green)
if os.path.exists(mpath):
os.system(f'''mv -f "{out_file}" "{mpath}" ''')
sprint(f"{success}{out_file} Pindah Ke {mpath}\n")
else:
sprint(error+"Path do not exist!\n")
else:
print("\n")
exit()
def obfuscate(VARIABLE_NAME, file_content):
b64_content = base64.b64encode(file_content.encode()).decode()
index = 0
code = f'{VARIABLE_NAME} = ""\n'
for _ in range(int(len(b64_content) / OFFSET) + 1):
_str = ''
for char in b64_content[index:index + OFFSET]:
byte = str(hex(ord(char)))[2:]
if len(byte) < 2:
byte = '0' + byte
_str += '\\x' + str(byte)
code += f'{VARIABLE_NAME} += "{_str}"\n'
index += OFFSET
code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
return code
def chunk_string(in_s, n):
"""Chunk string to max length of n"""
return "\n".join(
"{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
).rstrip("\\")
def encode_string(in_s, alphabet):
d1 = dict(enumerate(alphabet))
d2 = {v: k for k, v in d1.items()}
return (
'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
'"{}"\n.split("  ")])))\n'.format(
pformat(d2),
chunk_string(
"  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
MAX_STR_LEN,
),
)
)
def encryptsh():
in_file = input(ask + "Input Filename  > "+cyan)
if not os.path.exists(in_file):
sprint(error+'File not found')
os.system("sleep 2")
encryptsh()
os.system("bash-obfuscate " + in_file + " -o .temp")
if not os.path.exists(".temp"):
try:
sprint(info+"Installing Bash-Obfuscate....\n")
os.system("apt install nodejs -y && npm install -g bash-obfuscate")
os.system("bash-obfuscate " + in_file + " -o .temp")
except:
sprint(error+" Bash-Obfuscate not installed! Install it by:\n"+green+"[+] \"apt install nodejs -y && npm install -g bash-obfuscate\"")
exit(1)
out_file= input(ask + "Output Filename  > " + green)
with open(".temp",'r') as temp_f, open(out_file,'w') as out_f:
filedata = temp_f.read()
out_f.write("# Encrypted by Tnz Tools\n#@SukitooV1\n\n"+filedata)
os.remove(".temp")
sprint(f"{success}saved in {out_file}")
exit()
def decryptsh():
in_file = input(ask + "Input File  > "+cyan)
if not os.path.exists(in_file):
print(error+' File not found')
os.system("sleep 2")
decryptsh()
with open(in_file,'r') as in_f, open(".temp1",'w') as temp_f:
filedata = in_f.read()
if not (filedata.find("eval") != -1):
sprint(error+" Cannot be decrypted!")
exit()
newdata = filedata.replace("eval","echo")
temp_f.write(newdata)
out_file = input(ask + "Output File  > " +green)
os.system("bash .temp1 > .temp2")
os.remove(".temp1")
with open(".temp2",'r') as temp_f2, open(out_file,'w') as out_f:
filedata = temp_f2.read()
out_f.write("# Decrypted by Tnz Tools\n#@SukitooV1\n\n"+filedata)
os.remove(".temp2")
sprint(f"{success}saved in {out_file}")
exit()
def main():
os.system("clear")
sprint(logo, 0.01)
print(f"{green}[1]{yellow} Encrypt{cyan} Bash")
print(f"{green}[2]{yellow} Decrypt{cyan} Bash")
print(f"{green}[3]{yellow} Source")
print(f"{green}[4]{yellow} About")
print(f"{red}[0]{red} Exit")
choose = input(f"{ask}{blue}Choose an option : {cyan}")
while True:
if choose == "1" or choose=="01":
encryptsh()
elif choose == "2" or choose=="02":
decryptsh()
elif choose == "3" or choose=="03":
if os.path.exists("/data/data/com.termux/files/home"):
os.system("xdg-open --view 'https://whatsapp.com/channel/0029VabJsIT4CrfajbppbT2C'")
else:
os.system("xdg-open 'https://whatsapp.com/channel/0029VabJsIT4CrfajbppbT2C'")
main()
elif choose == "4" or choose=="04":
about()
elif choose == "0":
exit()
else:
sprint(error+'Wrong input!')
os.system("sleep 2")
main()
if __name__ == '__main__':
try:
main()
except KeyboardInterrupt:
sprint(info+"Thanks for using. Have a good day!")
exit()
except Exception as e:
sprint(error+str(e))
