# FastAPI CRUD App

To run the development server
```
uvicorn crud_app.main:app --reload
```

## Deployed the App using DETA

### Installing deta cli
- Windows
```bash
iwr https://get.deta.dev/cli.ps1 -useb | iex
```
**Output:**
```
Deta was installed successfully to C:\Users\<user_name>\.deta\bin\deta.exe
Run 'deta --help' to get started
```
- Linux
```bash
curl -fsSL https://get.deta.dev/cli.sh | sh
```
**Output:**
```
Deta was installed successfully to C:\Users\<user_name>\.deta\bin\deta.exe
Run 'deta --help' to get started
```

## To deploy
```
deta login
deta new
```
**Output:**
```
Successfully created a new micro
{
        "name": "crud_app",
        "runtime": "python3.7",
        "endpoint": "https://rfgtpq.deta.dev",
        "visor": "enabled",
        "http_auth": "disabled"
}
Adding dependencies...
  Downloading aiofiles-0.5.0-py3-none-any.whl (11 kB)
Collecting aniso8601==7.0.0
  Downloading aniso8601-7.0.0-py2.py3-none-any.whl (42 kB)
Collecting async-exit-stack==1.0.1
  Downloading async_exit_stack-1.0.1-py3-none-any.whl (4.7 kB)
Collecting async-generator==1.10
  Downloading async_generator-1.10-py3-none-any.whl (18 kB)
Collecting certifi==2020.12.5
  Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
Collecting chardet==4.0.0
  Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
Collecting click==7.1.2
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting colorama==0.4.4
  Downloading colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting dnspython==2.1.0
  Downloading dnspython-2.1.0-py3-none-any.whl (241 kB)
Collecting email-validator==1.1.2
  Downloading email_validator-1.1.2-py2.py3-none-any.whl (17 kB)
Collecting fastapi==0.65.1
  Downloading fastapi-0.65.1-py3-none-any.whl (50 kB)
Collecting graphene==2.1.8
  Downloading graphene-2.1.8-py2.py3-none-any.whl (107 kB)
Collecting graphql-core==2.3.2
  Downloading graphql_core-2.3.2-py2.py3-none-any.whl (252 kB)
Collecting graphql-relay==2.0.1
  Downloading graphql_relay-2.0.1-py3-none-any.whl (20 kB)
Collecting h11==0.12.0
  Downloading h11-0.12.0-py3-none-any.whl (54 kB)
Collecting idna==2.10
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
Collecting itsdangerous==1.1.0
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2==2.11.3
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe==2.0.1
  Downloading MarkupSafe-2.0.1-cp37-cp37m-manylinux2010_x86_64.whl (31 kB)
Collecting orjson==3.5.2
  Downloading orjson-3.5.2-cp37-cp37m-manylinux2014_x86_64.whl (231 kB)
Collecting promise==2.3
  Downloading promise-2.3.tar.gz (19 kB)
Collecting pydantic==1.8.2
  Downloading pydantic-1.8.2-cp37-cp37m-manylinux2014_x86_64.whl (10.1 MB)
Collecting python-dotenv==0.17.1
  Downloading python_dotenv-0.17.1-py2.py3-none-any.whl (18 kB)
Collecting python-multipart==0.0.5
  Downloading python-multipart-0.0.5.tar.gz (32 kB)
Collecting PyYAML==5.4.1
  Downloading PyYAML-5.4.1-cp37-cp37m-manylinux1_x86_64.whl (636 kB)
Collecting requests==2.25.1
  Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
Collecting Rx==1.6.1
  Downloading Rx-1.6.1-py2.py3-none-any.whl (179 kB)
Collecting six==1.16.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting starlette==0.14.2
  Downloading starlette-0.14.2-py3-none-any.whl (60 kB)
Collecting typing-extensions==3.10.0.0
  Downloading typing_extensions-3.10.0.0-py3-none-any.whl (26 kB)
Collecting ujson==4.0.2
  Downloading ujson-4.0.2-cp37-cp37m-manylinux1_x86_64.whl (179 kB)
Collecting urllib3==1.26.5
  Downloading urllib3-1.26.5-py2.py3-none-any.whl (138 kB)
Collecting uvicorn==0.13.4
  Downloading uvicorn-0.13.4-py3-none-any.whl (46 kB)
Collecting watchgod==0.7
  Downloading watchgod-0.7-py3-none-any.whl (11 kB)
Collecting websockets==8.1
  Downloading websockets-8.1-cp37-cp37m-manylinux2010_x86_64.whl (79 kB)
Using legacy 'setup.py install' for promise, since package 'wheel' is not installed.
Using legacy 'setup.py install' for python-multipart, since package 'wheel' is not installed.
Installing collected packages: six, Rx, promise, typing-extensions, graphql-core, urllib3, starlette, pydantic, MarkupSafe, idna, h11, graphql-relay, dnspython, click, chardet, certifi, aniso8601, websockets, watchgod, uvicorn, ujson, requests, PyYAML, python-multipart, python-dotenv, orjson, Jinja2, itsdangerous, graphene, fastapi, email-validator, colorama, async-generator, async-exit-stack, aiofiles
    Running setup.py install for promise: started
    Running setup.py install for promise: finished with status 'done'
    Running setup.py install for python-multipart: started
    Running setup.py install for python-multipart: finished with status 'done'
Successfully installed Jinja2-2.11.3 MarkupSafe-2.0.1 PyYAML-5.4.1 Rx-1.6.1 aiofiles-0.5.0 aniso8601-7.0.0 async-exit-stack-1.0.1 async-generator-1.10 certifi-2020.12.5 chardet-4.0.0 click-7.1.2 colorama-0.4.4 dnspython-2.1.0 email-validator-1.1.2 fastapi-0.65.1 graphene-2.1.8 graphql-core-2.3.2 graphql-relay-2.0.1 h11-0.12.0 idna-2.10 itsdangerous-1.1.0 orjson-3.5.2 promise-2.3 pydantic-1.8.2 python-dotenv-0.17.1 python-multipart-0.0.5 requests-2.25.1 six-1.16.0 starlette-0.14.2 typing-extensions-3.10.0.0 ujson-4.0.2 urllib3-1.26.5 uvicorn-0.13.4 watchgod-0.7 websockets-8.1
```

# Managing secrets and credentials
Place the secret information in a `.env` file