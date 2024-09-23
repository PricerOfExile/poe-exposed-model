FROM leddzip/generic-pytorch-model:0.2.0

# Copy the model configuration and state dictionary
COPY ./model_architecture.json /app/model_architecture.json
COPY ./model.pth /app/model.pth

# Inject the transformation logic
COPY ./transformer.py /app/transformer.py