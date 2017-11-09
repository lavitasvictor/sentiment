def code_name():
    import time
    return sum([int(x)**3 for x in list(str(time.time()).replace('.',''))])
    
def main_cycle(url):
    import requests
    r=requests.get(url)
    if not r.encoding=='utf-8':
        r.encoding='utf-8'
    name=url[url.rfind('olx.ua')+7:].replace('/','_')+str(code_name())+".txt"
    import os
    while name in os.listdir():
        name=url[url.rfind('olx.ua')+7:].replace('/','_')+str(code_name())+".txt"
    with open(name,'wt',encoding='utf-8') as f:
        f.write(r.text)
    return name,r
        
def re_cycle(r):
    import re
    dict_final={}
    line=re.compile(r'(?P<ref>(?<=href=")http.*html)[.\D\d\s\S\w\W]*?(?P<text>(?<=detailsLink\" >\n\t\t\t\t\t\t\t\t\t<strong>)\D*.*(?=\<\/strong\>))[.\D\d\s\S\w\W]*?(?P<price>(?<=\>).+грн)(?i)(?u)')
    for num,match in enumerate(line.finditer(r.text)):
        dict_final[num]=match.groupdict()
    return dict_final


    

if __name__ == "__main__":
    import sys
    final_dict={}
    for url in sys.argv[1:]:
        name, r=main_cycle(url)
        final_dict.update(re_cycle(r))
    with open('final_dict.txt','wt',encoding='utf-8') as f:
        f.write(str(final_dict))
