##httpd.conf

下記を追加

```
WSGIScriptAlias / /path/to/project.test1/project1/wsgi.py
WSGIPythonPath /path/to/project.test1

<Directory /path/to/project.test1>
	<Files wsgi.py>
		Order deny,allow
		Allow from all
	</Files>
</Directory>

Alias /static/ /path/to/project.test1/app1/static/
```
