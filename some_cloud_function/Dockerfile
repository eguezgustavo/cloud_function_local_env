FROM public.ecr.aws/lambda/python:3.8

COPY some_cloud_function/app.py ${LAMBDA_TASK_ROOT}
COPY people_app ${LAMBDA_TASK_ROOT}/people_app
COPY people_app/requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
WORKDIR ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]
