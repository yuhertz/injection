import requests
import re

url = input("Enter website URL: ")
response = requests.get(url)
text_files = re.findall(r'<a href="(.*\.txt)">', response.text)

for file in text_files:
    file_url = url + file
    file_content = requests.get(file_url).text
    print(f"Content of {file_url}:")
    print("--------------------")
    print(file_content)
    print("--------------------")
