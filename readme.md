# SukHo Fastapi Mysql

-----
### 프로잭트 개요
>포트폴리오 겸 필자가 가진 프로그래밍 방식과 기술들을 다시한번 사용해 보고자 시작한 프로젝트 입니다.
> 2개의 사이트, 도메인과 
> 총괄하는 1개의 자바 스프링서버,
> 각 사이트 디비와 연결되있는 2개의 api서버로 이루어져있습니다.

### 서버 설명
>현재 보고 계시는 서버는 개인적인 기술블로그로 만들 [석호.com](http://석호.com)의 api 서버입니다.
>python을 이용한 프레임워크인 fastapi를 사용하였으며 DB는 SQLalchemy를 이용해 연동하였습니다.

### 서버 구성
>테스트 환경은 annaconda를 이용하였으며 현재 구동중인 서버환경은 Esxi에 가상장치 생성 후 CentOs 7버전 최소 설치, ssh 및 vsftpd를 설치 해 주었고
> 최대한 컴팩트한 환경에서 구동할 수 있도록 구성해보았습니다.

-----
## 기능설명

-----

글 CRUD
댓글 CURD
관리자 로그인시 JWT토큰 발급 및 검증