# api_rasoi
API created to manage orders in a restaurant.

## How to start the server

```bash
  $ uvicorn app.application:get_app --reload
```

### How to start the server with custom logger:


```bash
  $ uvicorn app.application:get_app --reload --log-config=log_conf.yaml
```