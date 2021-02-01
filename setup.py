#!/usr/bin/env python3

# +------------------------+			   
# | Created with Sailboat  |			   
# |			                   |			   
# | Do not edit this file  |			   
# | directly. Instead  	   |			   
# | you should edit the	   |			   
# | `sailboat.toml` file.  |			   
# +------------------------+	

import setuptools

try:
  with open("README.md", "r") as fh:
	  long_description = fh.read()
except:
	long_description = "# empty_project\nempty project for sailboat testing\n### Contributors\n- cole wilson\n### Contact\n<cole@colewilson.xyz> "

options = {
	"name":"emptyproject1",
	"version":"0.0.1",
	"scripts":[],
	"entry_points":{'console_scripts': []},
	"author":"cole wilson",
	"author_email":"cole@colewilson.xyz",
	"description":"empty project for sailboat testing",
	"long_description":long_description,
	"long_description_content_type":"text/markdown",
	"url":"https://github.com/cole-wilson/empty",
	"packages":setuptools.find_packages(),
	"install_requires":[],
	"classifiers":["Programming Language :: Python :: 3"],
	"python_requires":'>=3.6',
	"package_data":{"": [],},
	"license":"none",
	"keywords":'',
}

custom_options = {}

if __name__=="__main__":
	setuptools.setup(**custom_options,**options)