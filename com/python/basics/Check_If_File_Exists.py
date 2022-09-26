from pathlib import Path

if __name__ =='__main__':
    if Path(r'C:\hadoop\bin\winutils1.exe').exists():
        print('File Present')
    else:
        print('File not present')