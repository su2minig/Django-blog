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
