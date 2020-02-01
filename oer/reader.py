import pandas as pd
from Resource import Resource
from ResourceManager import ResourceManager

excel_file = ("/home/wilson/Projects/OER Challenge/Excel/UWGcoursematerial.xlsx")
entries = pd.read_excel(excel_file)

resources = []

rs = ResourceManager()

for index in range(50):
    resourceData = {}
    resourceData["title"] = entries["Title"][index]
    resourceData["link"] = ""
    resourceData["author"] = entries["Author"][index]
    resourceData["subject"] = entries["Subject"][index]
    resourceData["type"] = Resource.Type.OTHER
    resourceData["isbn"] = entries["ISBN"][index]
    rs.add_resource(resourceData)
