package YB101_5_ACTIVIY_LOAD;

import java.sql.SQLException;
import java.util.*;

public interface IActivityDAO {
	public void getConnection() throws SQLException;
	public int insertfolkfestival(ActivityVO act) throws SQLException;
	public int insertactivity(ActivityVO act) throws SQLException;
	public int insertneighbor(ActivityNeighborVO nei) throws SQLException; 
	public void closeConn() throws SQLException;
} // end of class IEmpDAO