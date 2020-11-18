# Start with miniconda
FROM continuumio/miniconda:latest
# Copy project directory to container and set wd to copied directory
COPY . /Project
WORKDIR /Project
# Create environment to mimic development environment from YAML file
RUN conda env create -f environment.yml
# Reload bash and activate environment
ENV PATH /opt/conda/envs/docker_del/bin:$PATH
RUN /bin/bash/ -c "source activate docker_del"
# Expose Flask port so we may send CURL requests
EXPOSE 5000
# fire up flask app
ENTRYPOINT ["python", "run.py"]