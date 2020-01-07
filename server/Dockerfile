FROM python:3.7.6

WORKDIR /usr/app
COPY ./Pip* ./

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . ./

RUN python -c "import nltk; nltk.download('punkt')"
RUN CLI=1 flask db upgrade

ARG model_name
RUN python3 app/prerequisites.py
RUN rm -fr /root/.cache/torch/sentence_transformers

EXPOSE ${FLASK_RUN_PORT}
CMD flask run -h 0.0.0.0 -p ${FLASK_RUN_PORT}
