1. html처음에 예정은 텍스트만 보내는 것이 기준이였기 때문에 이미지를 보내는 것은 상정 X
    - 그래서 이미지를 보내고 싶으면 속성을 새로 줘야 한다.
    - https://www.w3schools.com/html/html_forms.asp
2. image = models.ImageField()
    - `pip install fillow`

3. setting.py 에 어디에 저장할지와 위치를 지정한다.
    ``` python
    MEDIA_URL = '/media/'
    # 파일을 저장할 위치
    MEDIA_ROOT = os.path.join(BASE_DIR,"media")
    ```