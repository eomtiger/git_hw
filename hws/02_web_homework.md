# 1. Semantic Tag

보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된
시맨틱(semantic) 태그를 모두 고르시오.


```python
div, header, h1, section, footer, a, form, span


#header, section, footer, form, a, h1
```

# 3. 크기 단위

크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를
설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기
위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

rem



# 4. 선택자

다음 예제를 통해 ‘자손 결합자’와 ‘자식 결합자’의 차이를 설명하시오

```python
/* 자손 결합자 */
div p {
color: crimson;
}
/* 자식결합자*/
div > p {
    color: crimson;
}
```

자손은 p 에 속한 모든 것들의 색을 crimson으로 바꾼다.

자식은 p만 색을 바꾸고 p에 속한 것들은 변하지 않는다.
