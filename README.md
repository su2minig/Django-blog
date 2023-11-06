# Django-blog

# WBS

![wbs](https://github.com/su2minig/Django-blog/assets/141402694/b02017d8-baee-46b1-834a-ade5c99022b7)


# 개발환경

* 기술스택: 
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

# 단계별 요구사항

### 0단계: Django Admin을 이용한 게시글 읽기 및 메인페이지 구현하기
<details markdown="1">
<summary>요구사항</summary>

1. 메인 페이지 구현

    *  url : `/`

    *  페이지 제목과 블로그 입장하기 버튼이 있습니다.

2. Django admin을 이용하여 게시글 작성

    * 게시글은 제목, 내용으로 구성되어 있습니다.
      
    * `/admin` 을 이용하여 게시글을 작성해보세요.

3. 작성되어 있는 게시글 목록을 볼 수 있습니다.

    * url : `/blog`
 
    * 게시글들의 제목을 확인 할 수 있습니다.

4. 작성 되어있는 게시글 상세 페이지를 볼 수 있습니다.
 
    * url : `/blog/<int:id>` ex)`/blog/1, /blog/2,...`

    * 게시글의 제목/내용을 보는 기능입니다.

</details>

### 1단계: 블로그 CRUD 기능 구현하기
<details markdown="1">
<summary>요구사항</summary>
  
1. **게시글 작성 기능 구현**
    
    <aside>
    🧐 로그인이 되지 않더라도 글 작성이 가능합니다. 인증은 다음단계에 있습니다.    
    </aside>
    
    - url : `/blog/write`
    - 게시글 제목과 내용을 작성 할 수 있는 페이지가 있어야합니다.
    - 작성한 게시글이 저장되어 게시글 목록에 보여야 합니다.
    - 카테고리가 지정될 수 있어야 합니다.

2. **게시글 수정 기능 구현**

    - url : `/blog/edit/<int:id>`
    
    - 게시글의 제목 또는 내용을 수정 하는 기능입니다.

    - 게시글 제목과 내용을 수정 할 수 있는 페이지가 있어야합니다.

     - 수정된 내용은 게시글 목록보기/상세보기에 반영되어야합니다.

3. **게시글 삭제 기능 구현**

    - url : `/blog/delete/<int:id>`

    - 게시글을 삭제하는 기능입니다.

    - 삭제를 완료한 이후에 게시글 목록 화면으로 돌아갑니다.

    - 삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능하며,
    접근 시도 시 404 에러가 뜨게 됩니다.

4. **게시글 검색 기능 구현**

     - url : `/blog/search/<str:tag>`

     - 주제와 카테고리에 따라 검색이 가능하게 합니다.

     - 검색한 게시물은 시간순에 따라 정렬이 가능해야 합니다
</details>


### 2단계: 로그인/회원가입 기능을 이용하여 블로그 구현하기
<details markdown="1">
<summary>요구사항</summary>

  
  1. **메인페이지 구현**

     - 회원가입/로그인 버튼이 있습니다.

     - 회원가입 버튼을 클릭하면 회원가입 페이지로 이동합니다.

     - 로그인 버튼을 클릭하면 로그인 페이지로 이동합니다.

  3. **회원가입 기능 구현**
      
      - url : `/register`
      
      - 회원가입을 할 수 있는 페이지가 있어야합니다.
      
      - 입력받는 값은 id, password입니다.

  4. **로그인 기능 구현**
   
      - url : `/login`
 
      - 로그인을 할 수 있는 페이지가 있어야합니다.
  
      - 입력받는 값은 id, password입니다.

  5. **게시글 작성 기능 구현**
  
      - **로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.**

  6. **게시글 목록 기능 구현**

      - **모든 사용자들이 게시한 블로그 게시글들의 제목을 확인 할 수 있습니다.**

  8. **게시글 수정 기능 구현**

      - **로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.**

      - **본인의 게시글이 아니라면 수정이 불가능합니다.**

  10. **게시글 삭제 기능 구현**
   
      - **로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.**
   
      - **본인의 게시글이 아니라면 삭제가 불가능합니다.**

      - **삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능하며,
      접근 시도 시 <존재하지 않는 게시글입니다> 라는 페이지를 보여줍니다.**
</details>

### 3단계: 블로그 기능 외 추가 기능 작성 및 배포
<details markdown="1">
<summary>요구사항</summary>
  
  1. **게시글 작성 기능 구현**

     - **사진 업로드가 가능하도록 합니다.**
     
     - **게시글 조회수가 올라갈 수 있도록 합니다.**
    
  2. **회원 관련 추가 기능(UI 직접 구현 필요)**
    
        - 비밀번호 변경기능
        
        - 프로필 수정
        
        - 닉네임 추가
   
  3. **댓글 기능(UI 직접 구현 필요)**
      
      - 댓글 추가
        
      - 댓글 삭제
        
      - 대댓글
        
      - disqus와 같은 솔루션 서비스를 사용하시면 안됩니다.
          - 가산점만 안될 뿐이지 완성도를 위해 추가하는 것은 괜찮습니다.

</details>


## 마인드맵

![mindmap](https://github.com/su2minig/Django-blog/assets/141402694/623b2ff4-e4c2-4917-bd2a-ae171f7e5111)

## 명세표

![명세표](https://github.com/su2minig/Django-blog/assets/141402694/bdae710a-4da0-4a27-85ee-1b76d5c210fd)


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

![erd](https://github.com/su2minig/Django-blog/assets/141402694/57232e6a-42e8-4e5a-a21e-84334deb5cec)


# UI

### 메인페이지

![메인페이지](https://github.com/su2minig/Django-blog/assets/141402694/0a0f0a87-8ccc-446f-a7df-60268972d103)


![메인페이지(비로그인)](https://github.com/su2minig/Django-blog/assets/141402694/c43ff314-cc39-445e-b26c-86821001c80d)



* 메인페이지화면으로 
