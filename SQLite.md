#

## ORM
- opp 프로그래밍에서 RDMBS를 연출할때 데이터 베이스와 OOP 프로그래밍 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

### 장점
- SQL문을 몰라도 DB연동이 가능하다.
- SQL의 절차적인 접근이 아닌 객체 지향적인 접근으로 인해 생산성이 증가한다.

### 단점
- ORM 안으로 완전한 서비스를 구현하는데에는 어렵다.

단점 보다 향상되는 생산성이 더 크기 때문에 ORM을 사용한다.

## 클래스
- 객체를 표현하기 위한 문법
- 같은 종류의 집단에 속하는 속성과 행위를 정의한 것으로, OOP프로그램의 기본적인 데이터 타입

### 인스턴스
- 클래스의 인스턴스/객체(실제 메모리상에 할당된 것)
- 인스턴스는 자신 고유의 속성(attribute)을 가지며 클래스에 정의한 행위(behavior)를 수행할 수 있다.
- 인스턴스의 행위는 클래스에 정의된 행위에 대해 매서드를 공유함으로써 메모리를 경제적으로 사용할 수 있다.

----
### CharField()
- 길이에 제한이 있는 문자열을 넣을 때 사용
- max_length는 필수 인자
- 텍스트 길이가 길때는 TextField()를 사용한다.

최대 길이가 존재하지 않는 칼럼
필수 인자가 없다.

auto_now_add 데이터베이스가 최초 생성 일자
django ORM이 최소 Insert 시에만 현재 날짜와 시간으로 갱신

마지막 업데이트 시간으로 갱신한다.


```
from django.db import models

# Create your models here.
class Article(models.Model):
    # 이 컬렌의 데이터의 길이는 최대 20글자
    # 필수 인자가 필요하다.
    title = models.CharField(max_length = 20)
    # 최대 길이가 존재하지 않는 칼럼
    # 필수 인자가 없다.
    contetn = models.TextField()
    # auto_now_add 데이터베이스가 최초 생성 일자
    # django ORM이 최소 Insert 시에만 현재 날짜와 시간으로 갱신
    creted_at = models.DateTimeField(auto_now_add=True)
    # 마지막 업데이트 시간으로 갱신한다.
    upated_at = models.DateTimeField(auto_now=True)
```