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

4. https://pypi.org/project/django-imagekit/
    - pip install django-imagekit

5. setting에 imagekit을 넣는다.
    - 이미지 원본을 줄여서 다운 받는 시간을 굉장히 줄여줄수 있다.
    - 이번에 긁어오는 건 원본을 안 남기는 것
    - 같은 곳에 원본을 줄여서 출력하는 것도 있음.
