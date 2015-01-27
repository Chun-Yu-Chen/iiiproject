package YB101_5_VIEW_LOAD;

import java.sql.SQLException;
import java.util.*;

public interface IViewDAO {
	public void getConnection() throws SQLException;
	public int insertview(ViewVO view) throws SQLException;
	public int insertneighbor(ViewNeighborVO nei) throws SQLException; 
	public void closeConn() throws SQLException;
} // end of class IEmpDAO