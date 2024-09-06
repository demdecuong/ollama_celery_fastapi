## Simple Ollama service with Celery and FastAPI

I’m trying to make my life less dull by spending time learning , researching and doing some hands-on “how it works“ in the AI/Data field.

![](asset/img.png)

### Tech - Begineer Level

- Celery : Message Queue
- FastAPI : Serving/Routing endpoints
- Docker : containerize
- Flower : Monitoring
- Ollama : OSS LLM (Sorry, I love open source)

### Quick start

1. Run application

```
docker-compose up -d
```

2. Run Ollama

In details, you can follow [Ollama](https://ollama.com/) site

```
ollama pull llama llama3.1:8b
ollama serve
```

After the above script, ensure the port http://localhost:11434/ shows `Ollama is running`

### Usage

in details are lists in [./docs](./docs/)

### Reference

https://medium.com/@simeon.emanuilov/ollama-with-fastapi-7f43cf532c43  
https://github.com/zhanymkanov/fastapi-best-practices  
https://github.com/derlin/fastapi-notebook-runner/tree/main
