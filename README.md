# lambda@edge

## serverless pyenv 사용

```bash
pyenv install 3.7.0
pyenv virtualenv -p python3.7 3.7.0 <project>
```

## serverless-python-requirements plugin

```bash
# serverless-python-requirements@5.0.0에 dockerize를 하지않는 버그가 있음 -> serverless-python-requirements@4.1.1 사용
yarn add serverless-python-requirements@4.1.1 -D

# requirements.txt 생성
pip3 freeze > requirements.txt
```

## 사용법

```bash
# deploy
sls deploy

# test
sls invoke local -p event.json -f hello
```
