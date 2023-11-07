# Django-blog

# 목차

* [기획](#기획)
* [WBS](#WBS)
* [요구사항-분석](#요구사항-분석)
* [개발환경](#개발환경)
* [프로젝트 구조](#프로젝트-구조)
* [ERD](#ERD)
* [UI](#UI)
* [겪은 오류들과 해결법](#겪은-오류들과-해결법)

# 기획

:bookmark:플레이하는 게임의 공략, 플레이 영상 글을 기록할 블로그:bookmark:


# WBS

2023.10.25 ~ 2023.11.07

![wbs](https://github.com/su2minig/Django-blog/assets/141402694/b02017d8-baee-46b1-834a-ade5c99022b7)

# 요구사항 분석

### 기본 요구사항

 - 모놀리식
 - 데이터베이스 구조 설계

### 0단계: Django Admin을 이용한 게시글 읽기 및 메인페이지 구현하기
<details markdown="1">
<summary>요구사항</summary>

1. 메인 페이지 구현 - [O]

    *  페이지 제목과 블로그 입장하기 버튼이 있습니다.

2. Django admin을 이용하여 게시글 작성 - [O]

    * 게시글은 제목, 내용으로 구성되어 있습니다.
      

3. 작성되어 있는 게시글 목록을 열람. - [O]
 
    * 게시글들의 제목을 확인 할 수 있습니다.

4. 작성 되어있는 게시글 상세 페이지를 열람. - [O]

    * 게시글의 제목/내용을 보는 기능입니다.

</details>

### 1단계: 블로그 CRUD 기능 구현하기
<details markdown="1">
<summary>요구사항</summary>
  
1. 게시글 작성 기능 구현 - [O]   
  
    - 로그인이 되지 않더라도 글 작성이 가능합니다. 
    - 게시글 제목과 내용을 작성 할 수 있는 페이지
    - 작성한 게시글이 저장되어 게시글 목록에 표시
    - 태그를 지정할 수 있다

2. 게시글 수정 기능 구현 - [O]
    
    - 게시글의 제목 또는 내용을 수정 가능

    - 게시글 제목과 내용을 수정 할 수 있는 페이지

    - 수정된 내용은 게시글 목록보기/상세보기에 반영

3. 게시글 삭제 기능 구현 - [O]

    - 게시글을 삭제하는 기능

    - 삭제를 완료한 이후에 게시판으로 이동

    - 삭제된 게시글은 게시글 목록보기/상세보기에서 표시 안함

4. 게시글 검색 기능 구현 - [O]

     - 게시글 제목, 내용, 태그에 따라 검색가능

     - 검색한 게시물은 시간순에 따라 정렬이 가능해야 합니다
</details>


### 2단계: 로그인/회원가입 기능을 이용하여 블로그 구현하기
<details markdown="1">
<summary>요구사항</summary>

  
  1. 메인페이지 구현 - [O]

     - 회원가입/로그인 버튼

     - 회원가입 버튼을 클릭하면 회원가입 페이지로 이동

     - 로그인 버튼을 클릭하면 로그인 페이지로 이동

  2. 회원가입 기능 구현 - [O]
      
      - 회원가입을 할 수 있는 페이지 
      
      - 입력받는 값은 id, password, nickname, email, profile_image

  3. 로그인 기능 구현 - [O]
   
      - 로그인을 할 수 있는 페이지
  
      - 입력받는 값은 id, password

  4. 게시글 작성 기능 구현 - [O]
  
      - 로그인을 한 유저만 해당 기능을 사용 가능

  5. 게시글 목록 기능 구현 - [O]

     - 모든 사용자들이 게시한 블로그 게시글들의 제목과 작성자, 작성자프로필사진 확인가능
        
  6. 게시글 수정 기능 구현 - [O]

      - 로그인을 한 유저만 해당 기능을 사용 가능

      - 본인의 게시글이 아니라면 수정이 불가

  7. 게시글 삭제 기능 구현 - [O]
   
      - 로그인을 한 유저만 해당 기능을 사용 가능ㅇ
   
      - 본인의 게시글이 아니라면 삭제가 불가
</details>

### 3단계: 블로그 기능 외 추가 기능 작성 및 배포
<details markdown="1">
<summary>요구사항</summary>
  
  1. 게시글 작성 기능 구현 - [O]

     - 사진 업로드
     
     - 게시글 조회수 카운트
    
  2. 회원 관련 추가 기능 - [O]
        
        - 프로필 수정(nickname, profile_image, password 변경가능)
        
        - 닉네임 추가
    
        - 회원탈퇴
   
  3. 댓글 기능 - [O]
      
      - 댓글 추가
        
      - 댓글 삭제
        
      - 대댓글

</details>


## 마인드맵

![mindmap](https://github.com/su2minig/Django-blog/assets/141402694/623b2ff4-e4c2-4917-bd2a-ae171f7e5111)

## 명세표

![명세표](https://github.com/su2minig/Django-blog/assets/141402694/bdae710a-4da0-4a27-85ee-1b76d5c210fd)

# 개발환경

* 💻 기술스택: 
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">


# 프로젝트 구조

```
📦blog
 ┣ 📂accounts
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂blog
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂main
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂makeblog
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┣ 📂accounts
 ┃ ┃ ┗ 📂profile_images
 ┃ ┗ 📂blog
 ┃ ┃ ┗ 📂images
 ┣ 📂static
 ┃ ┣ 📂assets
 ┃ ┃ ┣ 📂img
 ┃ ┗ 📂blog
 ┃ ┃ ┗ 📜main.css
 ┣ 📂templates
 ┃ ┣ 📂accounts
 ┃ ┃ ┣ 📜base.html
 ┃ ┃ ┣ 📜base2.html
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┣ 📜profile.html
 ┃ ┃ ┗ 📜update.html
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📜blog.html
 ┃ ┃ ┣ 📜post.html
 ┃ ┃ ┣ 📜post_confirm_delete.html
 ┃ ┃ ┗ 📜post_form.html
 ┃ ┣ 📂main
 ┃ ┃ ┗ 📜main.html
 ┃ ┗ 📜404.html
 ┣ 📜db.sqlite3
 ┗ 📜manage.py
```

# ERD

![erd](https://github.com/su2minig/Django-blog/assets/141402694/44f2ab3e-6a97-4ce3-8ebc-c2d022dfc5e7)


# UI

### 메인페이지

![메인페이지](https://github.com/su2minig/Django-blog/assets/141402694/7864588c-90b9-4d40-9e25-4a1a78d2ac92)


![메인페이지(비로그인)](https://github.com/su2minig/Django-blog/assets/141402694/16552f2d-d3d3-4d55-b94e-51512b1efc4d)




* 메인페이지화면으로 로그인시에는 상단에 메인페이지로 이동하는 home과 로그아웃이 있고 바로가기를 통해서 게시판과 프로필로 이동가능합니다.
* 비로그인시에는 상단에 로그아웃버튼대신 로그인버튼과 회원가입버튼이 있고 바로가기에는 게시판만 이동가능합니다.

### 게시판

![게시판페이지](https://github.com/su2minig/Django-blog/assets/141402694/e3908a7e-863e-402e-bbfd-b30ec7e9a758)

![게시판페이지(비로그인)](https://github.com/su2minig/Django-blog/assets/141402694/48d7aba7-be24-47af-a00f-43953498df51)

![게시판검색](https://github.com/su2minig/Django-blog/assets/141402694/920a3712-8711-4695-aa40-6f429545c7e7)

![게시판 페이지이동gif](https://github.com/su2minig/Django-blog/assets/141402694/0cfab991-75a6-46ba-84c1-e222a476f8f5)

* 게시판페이지의 경우 비로그인자도 글목록과 게시물을 볼 수 있지만 게시물 작성은 불가합니다.
* 검색창에 단어를 검색할경우 게시물의 제목과 내용 태그에 해당 단어가 포함된 게시물 목록을 보여줍니다.
* 게시물 5개를 기준으로 페이지가 나뉘며 화살표를 통하여 페이지 이동이 가능합니다(현재 페이지는 빨간색으로표시).

### 게시물

![게시물 상세](https://github.com/su2minig/Django-blog/assets/141402694/582e0899-6f18-437f-8108-1c65a93c6782)

![게시물상세비로그인](https://github.com/su2minig/Django-blog/assets/141402694/0e165aff-dfb7-46a9-b9d8-f262762b2350)

* 게시물의 제목,작성자,작성날짜,내용,태그,댓글을 확인가능합니다.
* 해당 게시물 작성자를 제외한 유저는 게시물 수정버튼과 삭제 버튼이 없습니다.

### 게시물 작성

![게시물작성(비로그인)gif](https://github.com/su2minig/Django-blog/assets/141402694/35354326-96ae-46e3-88cc-176a6587e64e)

![게시물작성gif](https://github.com/su2minig/Django-blog/assets/141402694/03149eec-bce7-4e87-beaf-711e5f243d01)

![입력란](https://github.com/su2minig/Django-blog/assets/141402694/c05b7e5e-1a06-44a0-92f4-ab7a35090d76)

* 비로그인자가 이용시 로그인페이지로 이동됩니다.
* 로그인이 되어있으면 작성폼 페이지로 이동합니다.
* 제목,내용은 필수로 작성해야하며 작성한 뒤 저장을 누르면 작성이 완료됩니다(제목,내용 입력안하고 저장 시 해당칸 작성을 요구합니다).
* 작성완료 시 게시판으로 이동합니다.

### 게시물 수정

![게시물삭제(비로그인)](https://github.com/su2minig/Django-blog/assets/141402694/0721c85e-04a1-4c0e-a0d1-e681e5484c84)

![게시물수정gif](https://github.com/su2minig/Django-blog/assets/141402694/a22020a6-c546-4358-9e94-dc2fed5962e2)

* 게시물 수정은 해당 게시물의 작성자일 경우에만 수정버튼이 보이며 클릭 시 수정페이지로 이동하여 기존 게시물의 내용의 변경이 가능합니다.

### 게시물 삭제

![게시물삭제(비로그인)](https://github.com/su2minig/Django-blog/assets/141402694/0721c85e-04a1-4c0e-a0d1-e681e5484c84)

![게시물삭제](https://github.com/su2minig/Django-blog/assets/141402694/39863347-2480-484d-9d0a-254b2febd1c0)

* 해당 게시물의 작성자일 경우에만 삭제버튼이 보이며 삭제버튼 클릭 시 삭제확인페이지로 이동하여 확인 시 게시물이 삭제된다.

### 댓글

![댓글 답글작성git](https://github.com/su2minig/Django-blog/assets/141402694/0a35275e-b57a-4888-83a4-aa56de9573c3)

![댓글 답글수정및삭제gif](https://github.com/su2minig/Django-blog/assets/141402694/df4edb0e-7a6f-47d0-aae5-470ad0583559)

* 게시물에는 댓글을 달 수 있습니다.
* 로그인을 하지 않은 유저가 사용시 로그인페이지로 이동됩니다.
* 게시물에 달린 댓글에 답글을 할 수 있습니다.
* 삭제 버튼 사용 시 댓글을 삭제할 수 있습니다.
* 수정 버튼 사용 시 수정폼이 나오며 댓글의 내용을 수정할 수 있습니다.

### 프로필

![프로필페이지](https://github.com/su2minig/Django-blog/assets/141402694/427a0640-a358-4492-bdce-4ae02080d57d)

* 로그인한 유저의 프로필 페이지입니다.
* 해당 유저의 프로필사진 이메일 닉네임을 보여줍니다.
* 바로가기를 통해서 게시판, 프로필수정, 회원탈퇴페이지로 이동이 가능합니다.

### 프로필 수정

![프로필수정페이지](https://github.com/su2minig/Django-blog/assets/141402694/99f1c37e-0f44-4dde-988c-65db2c92aa90)

![불일치](https://github.com/su2minig/Django-blog/assets/141402694/9c1d05ce-2fa8-410a-853e-548214edba29)

* 유저의 별명,프로필이미지, 비밀번호의 변경이 가능합니다.
* 비밀번호와 비밀번호 확인의 값이 다를경우 비밀번호 불일치를 알려주고 재입력을 요구합니다.

### 회원탈퇴

![회원탈퇴gif](https://github.com/su2minig/Django-blog/assets/141402694/5ad75356-7fd4-4cf8-ab06-496bdd679ab1)

![회원탈퇴취소gif](https://github.com/su2minig/Django-blog/assets/141402694/4ac7bb07-6265-4d26-af81-125eb7a7038b)

* 회원탈퇴 클릭 시 탈퇴여부를 재확인합니다.
* '네'를 클릭 시 유저의 정보를 삭제후 로그아웃됩니다.
* '취소'를 클릭 시 다시 프로필로 이동합니다.

# 겪은 오류들과 해결법

* 게시물 댓글 작성기능 구현 중 발생한 405 에러
  - 발생 원인 : `Request URL` 을 잘못 입력하여 매칭 안된 경우 또는 `HTTP 메서드 (GET/POST/PUT/...)` 가 잘못 매칭된 경우 생긴다고한다. 이번 경우에는 작성 `form`의 `action`에 `url`을 지정 안한 것을 발견했고 `url`을 작성해주니 제대로 댓글이 작성되었다.

* `no such column` 에러
  - recomment 모델을 작성하고서 migrate를 하지 않은 탓에 DB에 테이블이 반영이 안되어 발생하게되었다.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    로 DB에 테이블을 반영한 후 해결되었다.

* `crispy form`을 사용 중 `TemplateDoesNotExist: bootstrap4/uni_form.html` 에러 발생

  - 발생원인: `django-crispy-forms` 2.0부터 템플릿 팩은 이제 별도의 패키지에 있다고한다.

  - 해결방법: 버전 2.0부터 `Crispy-bootstrap4`도 `pip install`한후 INSTALLED_APPS에 `"crispy_bootstrap4"`를 추가하고 `CRISPY_ALLOWED_TEMPLATE_PACKS  =  "bootstrap4"` 템플릿팩 허용을 추가해주었다.
 
* 댓글 수정 삭제 시 404에러 발생

  - 발생 원인: shell에 들어가 각각 상속한 `deleteview`와 `updateview`을 dir로 확인해보니 `pk_url_kwarg`를 보고 찾아보니 전달되는 pk값이 `post`의 pk와 `comment`의 comment_pk 이 두개의 pk값이 전달되었는데 `pk_url_kwarg`에 `post`의 pk값인 pk가 들어가서 댓글의 쿼리값을 찾지못해 발생한 것이였다.

  - 해결방법:

  ```
    class ReCommentDeleteView(UserPassesTestMixin, DeleteView):
            model = ReComment
            pk_url_kwarg = 'recomment_pk'
   ```

  값을 설정을 해주니 해결되었다.

* `DEBUG`를 `False`로 설정하면 static file, media file 사용불가현상

  - 발생 원인: 일반적으로 `DEBUG=False`인 경우는` static file`을 `django project`에서 제공하지 않는다고한다.
  - 해결 방법:
    1.

      ```
                  urlpattern += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

       ```
    이 방법은 `DEBUG=True`, `runserver` 로 서버 돌릴 때에만 작동한다.

    2. `DEBUG=False`인 경우엔 `python manage.py runserver --insecure`로 static file 까지는 제공가능하지만, media의 경우 지원되지 않음((보안 모드를 사용하지 않음).

    3. `STATIC_ROOT`를 설정한 후 `python manage.py collectstatic` 명령어를 사용하면 설정된 `STATIC_ROOT`에 경로의 정적 파일들을 모두 모아준다.
   
    4. `media`, `static` 파일 `url` 경로 추가(project/urls.py)

     ```
    from django.views.static import serve

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
     ```
                
