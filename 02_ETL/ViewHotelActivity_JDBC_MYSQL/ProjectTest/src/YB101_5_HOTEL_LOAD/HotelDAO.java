package YB101_5_HOTEL_LOAD;

import java.sql.*;
import java.io.*;
import java.util.*;

public class HotelDAO implements IHotelDAO {
	private static final String INSERT_STMT =
		"INSERT INTO hotelinfo VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?,?,?)";

		
	Connection conn = null;
	public void getConnection() throws SQLException{
		//String connUrl = "jdbc:sqlserver://localhost:1433;databaseName=Project";
		String connUrl = "jdbc:mysql://10.120.28.19:3306/db01";
		conn = DriverManager.getConnection(connUrl, "yb101", "iii");
		//conn = DriverManager.getConnection(connUrl, "sa", "passw0rd");
	}
	
	public int insert (HotelVO hotel) throws SQLException {
		int updateCount = 0;
		PreparedStatement pstmt = conn.prepareStatement(INSERT_STMT);
		System.out.println(hotel.getHotelid());
		pstmt.setNString(1,hotel.getHotelid());
		pstmt.setNString(2,hotel.getHotelname() );
		pstmt.setNString(3,hotel.getHotelregion() );
		pstmt.setNString(4,hotel.getHoteltype() );
		pstmt.setNString(5,hotel.getHotelurl() );
		pstmt.setNString(6,hotel.getHoteladdress());
		pstmt.setNString(7,hotel.getHoteltel());
		pstmt.setNString(8,hotel.getHotelfax());
		pstmt.setNString(9,hotel.getHotelintro());
		pstmt.setInt(10,hotel.getHotelop());
		pstmt.setNull(11,java.sql.Types.FLOAT);
		pstmt.setNull(12,java.sql.Types.FLOAT);
		updateCount = pstmt.executeUpdate();
		return updateCount;
	}
	public void closeConn() throws SQLException {
		if (conn != null)
			conn.close();
	}
} // end of class EmpDAO