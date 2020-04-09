FROM python:3.7

WORKDIR /var/pysudoku

ENV PYTHONPATH "${PYTHONPATH}:/var/pysudoku"

COPY requirements.txt ./
COPY *.py ./
COPY *.yaml ./

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "solve_grid.py", "-G", "grid.yaml"]
