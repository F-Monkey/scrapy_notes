package indi.monkey.web.center.controller;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import indi.monkey.web.center.db.MysqlConnection;

@RestController
@RequestMapping("/user")
public class UserController {
	@RequestMapping("/login")
	public String login(String username, String password, String checkCode) throws SQLException, ClassNotFoundException {
		// 这里拿到了账号密码 
		System.err.println(String.format("username:%s,password:%s,checkcode:%", username,password,checkCode));
		// 这里拿到账户密码了
		// 然后获取连接
		Connection connection = MysqlConnection.getConnection();
		// 执行这句sql
		String sql = "select 1 from user where username = " +username + " and password= "+ password;
		
		Statement statement = connection.createStatement();
		
		ResultSet result = statement.executeQuery(sql);
		// 然后查看resultset的结果
		
		return null;
	}
}
