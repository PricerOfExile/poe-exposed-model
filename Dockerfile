FROM leddzip/pytorch-generic-model:0.12.0

COPY ./model_architecture.json /app/model_architecture.json
COPY ./model.pth /app/model.pth
COPY ./transformer.py /app/transformer.py
COPY ./translator.py /app/translator.py

WORKDIR /app

CMD ["./.venv/bin/python", "generic_pytorch_model/main.py"]