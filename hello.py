#!/usr/bin/env python3
import json, os


# FROM LAB 3 DEMO

# print("Content-Type: text/plain")
# print()
# print(os.environ)

# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=4))

print("Content-Type: text/html")
print()
print(os.environ['HTTP_USER_AGENT'])

# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")