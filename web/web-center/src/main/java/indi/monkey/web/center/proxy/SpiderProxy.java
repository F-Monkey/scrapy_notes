package indi.monkey.web.center.proxy;

import java.util.List;
import java.util.Map;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import indi.monkey.web.bean.vo.User;

@FeignClient("/spider")
public interface SpiderProxy {
	
	@RequestMapping(value = "/findAllUsers",method = RequestMethod.GET)
	List<User> findAllUsers();
	
	@RequestMapping(value = "/processUserContent")
	Map<String, Object> processTitleDetail(String userURL);
}
