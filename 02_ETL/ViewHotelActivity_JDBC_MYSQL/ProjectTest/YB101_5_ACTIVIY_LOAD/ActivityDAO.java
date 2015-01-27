package YB101_5_ACTIVIY_LOAD;

import java.sql.*;
import java.io.*;
import java.util.*;

public class ActivityDAO implements IActivityDAO {
	private static final String INSERT_STMT = "INSERT INTO activityinfo VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?)";
	private static final String INSERT_NEIGHBOR_STMT = "INSERT INTO activityneighbor VALUES (?, ?, ?)";
	Connection conn = null;

	public void getConnection() throws SQLException {
		String connUrl = "jdbc:sqlserver://localhost:1433;databaseName=Project";
		conn = DriverManager.getConnection(connUrl, "sa", "passw0rd");
	}

	public int insertfolkfestival(ActivityVO act) throws SQLException {
		int updateCount = 0;
		PreparedStatement pstmt = conn.prepareStatement(INSERT_STMT);
		pstmt.setString(1, act.getActivityid());
		pstmt.setString(2, act.getActivityname());
		pstmt.setString(3, act.getActivityregion());
		pstmt.setString(4, act.getActivitytype());
		pstmt.setNull(5,java.sql.Types.INTEGER);
		pstmt.setNull(6,java.sql.Types.INTEGER);
		pstmt.setNull(7,java.sql.Types.INTEGER);
		pstmt.setNull(8,java.sql.Types.INTEGER);
		pstmt.setNull(9,java.sql.Types.INTEGER);
		pstmt.setNull(10,java.sql.Types.INTEGER);
		pstmt.setNull(11,java.sql.Types.INTEGER);
		pstmt.setNull(12,java.sql.Types.INTEGER);
		pstmt.setNull(13,java.sql.Types.INTEGER);
		pstmt.setNull(14,java.sql.Types.INTEGER);
		pstmt.setNull(15,java.sql.Types.INTEGER);
		pstmt.setNull(16,java.sql.Types.INTEGER);
		pstmt.setNull(17,java.sql.Types.DATE);
		pstmt.setString(18, act.getActivityaddress());
		pstmt.setString(19, act.getActivitytel());
		pstmt.setString(20, act.getActivityintro());
		pstmt.setNull(21,java.sql.Types.FLOAT);
		pstmt.setNull(22,java.sql.Types.FLOAT);
		updateCount = pstmt.executeUpdate();
		return updateCount;
	}
	public int insertneighbor(ActivityNeighborVO nei) throws SQLException {
		int updateCount1 = 0;
		PreparedStatement pstmt1 = conn.prepareStatement(INSERT_NEIGHBOR_STMT);
		pstmt1.setString(1, nei.getActivityid());
		pstmt1.setString(2, nei.getNeighbortype());
		pstmt1.setString(3, nei.getNeighborname());
		updateCount1 = pstmt1.executeUpdate();
		return updateCount1;
	}
	public int insertactivity(ActivityVO act) throws SQLException {
		int updateCount = 0;
		PreparedStatement pstmt = conn.prepareStatement(INSERT_STMT);
		pstmt.setString(1, act.getActivityid());
		pstmt.setString(2, act.getActivityname());
		pstmt.setString(3, act.getActivityregion());
		pstmt.setString(4, act.getActivitytype());
		pstmt.setInt(5,act.getActivityjan());
		pstmt.setInt(6,act.getActivityfeb());
		pstmt.setInt(7,act.getActivitymar());
		pstmt.setInt(8,act.getActivityapr());
		pstmt.setInt(9,act.getActivitymay());
		pstmt.setInt(10,act.getActivityjun());
		pstmt.setInt(11,act.getActivityjul());
		pstmt.setInt(12,act.getActivityaug());
		pstmt.setInt(13,act.getActivitysep());
		pstmt.setInt(14,act.getActivityoct());
		pstmt.setInt(15,act.getActivitynov());
		pstmt.setInt(16,act.getActivitydec());
		pstmt.setNull(17,java.sql.Types.DATE);
		pstmt.setNull(18, java.sql.Types.VARCHAR);
		pstmt.setNull(19, java.sql.Types.NVARCHAR);
		pstmt.setString(20, act.getActivityintro());
		pstmt.setNull(21,java.sql.Types.FLOAT);
		pstmt.setNull(22,java.sql.Types.FLOAT);
		updateCount = pstmt.executeUpdate();
		return updateCount;
	}
	public void closeConn() throws SQLException {
		if (conn != null)
			conn.close();
	}
} // end of class ActivityDAO