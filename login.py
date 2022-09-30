#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret, os
from http.cookies import SimpleCookie

# FROM LAB 3 DEMO


s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if "username" in cookie:
    cookie_username = cookie["username"].value
if "password" in cookie:
    cookie_password = cookie["password"].value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password

if cookie_ok:
    username = cookie_username
    password = cookie_password

if form_ok:
    print("Set-Cookie: username=" + username)
    print("Set-Cookie: password=" + password)
    print("Content-Type: text/html")
print()

if not username or not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())