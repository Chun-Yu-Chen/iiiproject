package yb101_5_project_tests;

import java.sql.*;

// 採用屬性檔方式載入JDBC Driver
public class FileProperties {
	public static void main(String[] args) {
		Connection conn = null;
		try {     
			conn = DatabaseConnect.getConnection();
			String qryStmt = "SELECT * FROM employee";
			PreparedStatement stmt = conn.prepareStatement(qryStmt);
			ResultSet rs = stmt.executeQuery();
			while(rs.next()) {
				System.out.print("name = " + rs.getString("ename") + ", ");
				System.out.println("salary = " + rs.getDouble("salary"));
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if (conn != null)
				try {
					conn.close();
				} catch(SQLException e) {
					e.printStackTrace();
				}
		}
	}// end of main()
}// end of class FileProperties 
