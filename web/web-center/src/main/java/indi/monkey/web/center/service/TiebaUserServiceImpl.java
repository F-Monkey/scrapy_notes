package indi.monkey.web.center.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import indi.monkey.web.bean.vo.Response;
import indi.monkey.web.bean.vo.User;
import indi.monkey.web.center.proxy.SpiderProxy;

@Service
public class TiebaUserServiceImpl implements TiebaUserService{
	
	@Resource
	SpiderProxy proxy;
	
	@Override
	public Response<?> findAllUsers() {
		List<User> users = proxy.findAllUsers();
		List<User> females = new ArrayList<User>();
		List<User> males = new ArrayList<User>();
		users.forEach(u->{
			if("F".equals(u.getSex())) {
				females.add(u);
			}else {
				males.add(u);
			}
		});
		Map<String, List<User>> sexMap = new HashMap<String, List<User>>(2);
		sexMap.put("female", females);
		sexMap.put("male", males);
		return Response.createSuccessResp(sexMap);
	}
	
	
	
}
