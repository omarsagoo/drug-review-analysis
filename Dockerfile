FROM jupyter/scipy-notebook

# copy over the requirements.txt file first.
COPY ./requirements.txt /home/jovyan/work/requirements.txt

RUN python -m pip install --no-cache -r /home/jovyan/work/requirements.txt

COPY ./notebooks /home/jovyan/work/notebooks

CMD start-notebook.sh --NotebookApp.token='' --NotebookApp.password='' --ip=0.0.0.0
