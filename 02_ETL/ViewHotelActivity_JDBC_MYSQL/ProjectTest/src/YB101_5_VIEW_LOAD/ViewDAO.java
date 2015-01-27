package YB101_5_VIEW_LOAD;

import java.sql.*;
import java.io.*;
import java.util.*;

public class ViewDAO implements IViewDAO {
	private static final String INSERT_STMT = "INSERT INTO viewinfo VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?)";
	private static final String INSERT_NEIGHBOR_STMT = "INSERT INTO viewneighbor VALUES (?, ?, ?)";
	Connection conn = null;

	public void getConnection() throws SQLException {
//		String connUrl = "jdbc:sqlserver://localhost:1433;databaseName=Project";
//		conn = DriverManager.getConnection(connUrl, "sa", "passw0rd");
		String connUrl = "jdbc:mysql://10.120.28.19:3306/db01";
		conn = DriverManager.getConnection(connUrl, "yb101", "iii");
	
	}

	public int insertview(ViewVO view) throws SQLException {
		int updateCount = 0;
		PreparedStatement pstmt = conn.prepareStatement(INSERT_STMT);
		pstmt.setNString(1, view.getViewid());
		pstmt.setNString(2, view.getViewname());
		pstmt.setNString(3, view.getViewregion());
		pstmt.setNString(4, view.getViewtype());
		pstmt.setNString(5, view.getViewurl());
		pstmt.setNString(6, view.getViewaddress());
		pstmt.setNString(7, view.getViewtel());
		pstmt.setNString(8, view.getViewstay());
		pstmt.setNString(9, view.getViewintro());
		pstmt.setNull(10,java.sql.Types.INTEGER);
		pstmt.setNull(11,java.sql.Types.INTEGER);
		pstmt.setNull(12,java.sql.Types.INTEGER);
		pstmt.setNull(13,java.sql.Types.INTEGER);
		pstmt.setNull(14,java.sql.Types.INTEGER);
		pstmt.setNull(15,java.sql.Types.INTEGER);
		pstmt.setNull(16,java.sql.Types.INTEGER);
		pstmt.setNull(17,java.sql.Types.INTEGER);
		pstmt.setInt(18,0);
		pstmt.setNull(19,java.sql.Types.FLOAT);
		pstmt.setNull(20,java.sql.Types.FLOAT);
		updateCount = pstmt.executeUpdate();
		return updateCount;
	}
	public int insertneighbor(ViewNeighborVO nei) throws SQLException {
		int updateCount1 = 0;
		PreparedStatement pstmt1 = conn.prepareStatement(INSERT_NEIGHBOR_STMT);
		pstmt1.setNString(1, nei.getViewid());
		pstmt1.setNString(2, nei.getNeighbortype());
		pstmt1.setNString(3, nei.getNeighborname());
		updateCount1 = pstmt1.executeUpdate();
		return updateCount1;
	}

	public void closeConn() throws SQLException {
		if (conn != null)
			conn.close();
	}
} // end of class ActivityDAO