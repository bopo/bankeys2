import re,os
s = open('SUMMARY.md').read()
m = re.findall(r'\((.*?)\)', s, re.M)

for x in m:
    if '/' in x[-1]:
        print(x)
        if not os.path.isdir(x):
            os.mkdir(x)
    else:
        if not os.path.exists(x):
            open(x,'w').write('#'+x)