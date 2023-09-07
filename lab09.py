import requests
# requests library is needed

r = requests.get('http://172.25.0.29/index.php')
# send a request to the webpage and load the entire response into the variable

web_headers = r.headers
print("Headers are here:")
print(web_headers)
# fetch the web headers then print them here

web_html = r.text
print("html from the body of the webpage")
print(web_html)
# print the body of the webpage

web_status_code = r.status_code
print("HTTP status code here:")
print(web_status_code)
# print the status code of the request

web_cookies = r.cookies
print("Returned cookies here:")
print(web_cookies)
# print web cookies