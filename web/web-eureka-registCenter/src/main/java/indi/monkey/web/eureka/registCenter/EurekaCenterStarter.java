package indi.monkey.web.eureka.registCenter;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@EnableEurekaServer
@SpringBootApplication
public class EurekaCenterStarter {
	public static void main(String[] args) {
		SpringApplication.run(EurekaCenterStarter.class, args);
	}
}
