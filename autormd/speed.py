import os

def checkComp(cfgdir, file):
    ti = {}
    open(cfgdir / '.filetimes', 'a+').close()
    with open(cfgdir / '.filetimes') as times:
        for i in times:
            try:
                ti[i.split(';')[0]] = i[:-1].split(';')[1]
            except:
                pass
    with open(cfgdir / '.filetimes', 'a') as times:
        ft = os.stat(file).st_mtime
        if str(file) in ti:
            if ti[str(file)] == str(ft):
                return False
            else:
                times.write(f"\n{file};{ft}")
                return True
        else:
            times.write(f"\n{file};{ft}")
            return True
