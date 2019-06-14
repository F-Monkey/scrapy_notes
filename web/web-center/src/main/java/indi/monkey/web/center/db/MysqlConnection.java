package indi.monkey.web.center.db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * 
 * @author tangjf
 *
 */
public class MysqlConnection {
	public static Connection getConnection() throws SQLException, ClassNotFoundException {
		//我也忘了差不多了
		String url = "jdbc:mysql://localhost:3306/test?serverTimezone=UTC";
		String userName = "root";
		String password = "root";
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection connection = DriverManager.getConnection(url, userName, password);
		return connection;
	}
	
	/**
	 * 测试一下
	 * @param args
	 * @throws SQLException 
	 * @throws ClassNotFoundException 
	 */
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		/**  
		 * 	创建一个简单的用户表  然后我们测试一下
		 * mysql> create table user(username varchar(100),password varchar(50));
			Query OK, 0 rows affected (0.11 sec)
			
			mysql> desc user;
			+----------+--------------+------+-----+---------+-------+
			| Field    | Type         | Null | Key | Default | Extra |
			+----------+--------------+------+-----+---------+-------+
			| username | varchar(100) | YES  |     | NULL    |       |
			| password | varchar(50)  | YES  |     | NULL    |       |
			+----------+--------------+------+-----+---------+-------+
			2 rows in set (0.02 sec)
		 */
		
		// 插入一条数据
		query();
	}
	
	public static void insert() throws SQLException, ClassNotFoundException {
		Connection connection = getConnection(); // 获取连接
		Statement statement = connection.createStatement(); // 获取statement 我忘了
		String sql = "insert into user values('tom','111111')"; // 写sql
		statement.execute(sql); // 执行
//		connection.commit(); // 提交 
		 // Can''t call commit when autocommit=true  开启了自动提交，不需要手动commit
		// =.=有数据了
	}
	
	public static void query() throws ClassNotFoundException, SQLException {
		Connection connection = getConnection(); // 获取连接
		Statement statement = connection.createStatement(); // 获取statement 我忘了
		String sql = "select * from user"; // 写sql
		ResultSet result = statement.executeQuery(sql); // 执行
		while(result.next()) {
			String username = result.getString("username");
			String password = result.getString("password");
			System.out.println(String.format("username:%s --- password:%s", username,password));
		}
	}
}
