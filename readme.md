# We have tested several images and containers here in docker
<ol>
    <li>
        MySql: This has mysql instance ready which uses mysql default port 3306. There is one change which is after creating an instance it will create another user <b>myuser</b> with password <b>mypassword</b>. It calls mysql:latest base image so I don't know when I will be using it again, so if I am calling it from the graveyard! fuck this man. 
    </li>
    <li>
        Django with built-in mysql: try <b>docker compose build --no-cache && docker compose up</b> but before that you have to create an .env file inside the DjangoWithMysql folder. And the contents are given below.
    </li>
</ol>

## .env contents for DjangoWithMysql
>MYSQL_ROOT_PASSWORD= <br>
MYSQL_DATABASE= <br>
MYSQL_USER= <br>
MYSQL_PASSWORD= <br>
DATABASE_NAME= <br>
DATABASE_USER= <br>
DATABASE_PASSWORD= <br>
DATABASE_HOST=db <br>
DATABASE_PORT=3306 <br>

I have removed my contents due to git warning, but you can put yours. The contents should match mysql > init.sql. For the MYSQL_ROOT_PASSWORD you can set as you wish, it will be initiated at run time.