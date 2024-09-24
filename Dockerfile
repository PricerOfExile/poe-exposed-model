FROM leddzip/pytorch-generic-model:0.9.0

# Copy the model configuration and state dictionary
COPY ./model_architecture.json /app/model_architecture.json
COPY ./model.pth /app/model.pth
COPY ./translator.py /app/translator.py

# Inject the transformation logic
COPY ./transformer.py /app/transformer.py

WORKDIR /app

CMD ["./.venv/bin/python", "generic_pytorch_model/main.py"]