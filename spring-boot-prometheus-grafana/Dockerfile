FROM maven:3-jdk-11
ADD . /code
WORKDIR /code
RUN mvn clean package -DskipTests=true
CMD mvn spring-boot:run
