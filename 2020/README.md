# Skeleton


## Plain

```
-.
  |-- hello

```



# Hexagonal Skeleton


```
`-.
  |-- domain/
  |-- app/
  |-- infra
  |    `.
         |-- adapters
         |-- port
         `--
```







```
{
    "python.venvPath": "plain/.venv",
    "python.pythonPath": "${workspaceFolder}/plain/.venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.banditEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.formatOnType": false,
    "editor.formatOnPaste": false
}
```
