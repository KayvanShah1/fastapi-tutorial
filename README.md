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

### Managing secrets and credentials
Place the secret information in a `.env` file