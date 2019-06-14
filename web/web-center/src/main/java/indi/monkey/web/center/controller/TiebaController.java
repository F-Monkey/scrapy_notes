package indi.monkey.web.center.controller;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import indi.monkey.web.bean.vo.Response;

@Controller
@RequestMapping("/tieba")
public class TiebaController {
	
	@RequestMapping(value = "/queryUsers", method = RequestMethod.GET, produces = {
			MediaType.APPLICATION_JSON_UTF8_VALUE })
	public Response<?> queryUsers(String condition) {
		
		
		
		return null;
	}
}
