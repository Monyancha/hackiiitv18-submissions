import re
import mechanize
from bs4 import BeautifulSoup
import csv

def cv_parser(file):
    browser = mechanize.Browser(factory=mechanize.RobustFactory()) 
    browser.set_handle_robots(False)
    browser.open("http://recruitplushrxmlapidemo.onlineresumeparser.com/Default.aspx")
    browser.select_form(nr=0)
    browser.form.set_all_readonly(False)
    file = '/home/heet/My-Work/MyProjects/hackiiitv18-submissions/team28-Automation/iscreening/Sample resumes/CV1.pdf'
    browser.form.add_file(open(file), 'text/plain', file)
    response = browser.submit()
    soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
    extracted_cv = soup.find(id="txtResume")
    text = extracted_cv.get_text().encode('utf-8')
    print(text)
    ext_file = open("./cv_parsed.txt", "w")
    ext_file.write(text)
    ext_file.close()

def main():
    cv_parser(None)

if __name__ == '__main__':
    main()