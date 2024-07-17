# python_flask_demo
This is a simple student performance management system (using Python Flask + MySQL)

The first step is to install the MySQL software.
https://dev.mysql.com/downloads/installer/
> For the SQL schema required for this example, please refer to the [sql.txt](sql.txt) file.

The second step is to install the python package flask and flask_mysqldb.
```dos
pip install flask
pip install flask_mysqldb
```

The third step is to execute the program, as follows
```python
python app.py
```

After that, you can see the execution screen on the browser (http://127.0.0.1:5000/), as follows
![main page image](https://github.com/user-attachments/assets/383bf348-bfd8-419c-9981-2bb1436c9b4c)
![students management image](https://github.com/user-attachments/assets/509adbea-f269-4b7c-86fb-1e35bb28f90a)
![courses management image](https://github.com/user-attachments/assets/1dbd4092-ac62-4e24-8313-7fccfee2b7ff)
![grades management image](https://github.com/user-attachments/assets/0ce5deb8-eeca-49be-af20-f0c1ca93cfb0)

[!NOTE]
Regarding this example, do you think there is anything that needs to be improved? 
For example: `mysql password` should not use root privileges and be written in the program.
