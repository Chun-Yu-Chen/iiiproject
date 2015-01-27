package YB101_5_HOTEL_LOAD;

import java.sql.SQLException;
import java.util.*;

public interface IHotelDAO {
	public void getConnection() throws SQLException;
	public int insert(HotelVO hotel) throws SQLException;
	public void closeConn() throws SQLException;
} // end of class IEmpDAO