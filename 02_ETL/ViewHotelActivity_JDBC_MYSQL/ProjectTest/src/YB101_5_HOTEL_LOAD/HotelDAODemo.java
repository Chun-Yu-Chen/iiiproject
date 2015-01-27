package YB101_5_HOTEL_LOAD;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.*;
import java.io.InputStreamReader;
import java.io.IOException;
import java.sql.SQLException;
import java.util.*;


public class HotelDAODemo {
	public static void main(String[] args) {
		IHotelDAO dao = new HotelDAO();
		try {
			dao.getConnection();
			String[] data;
			String dataline = null;
			int countline=-1;
			String hotelid = null;
			File readfile = new File("C://Users//BigData//100_project//done//tainan_hotel.txt");
			InputStreamReader fr = new InputStreamReader(new FileInputStream(readfile),"UTF-8");
			BufferedReader br = new BufferedReader(fr);
			while ((dataline = br.readLine()) != null) {
				countline++;
				if (countline==0){continue;}
				data = dataline.split("\\|");
				if (countline<10){
					hotelid="H000"+countline;
				}else if(countline>=10 && countline<100){
					hotelid="H00"+countline;
				}else if(countline>=100 && countline<1000){
					hotelid="H0"+countline;
				}else{
					hotelid="H"+countline;
				}
				System.out.println(hotelid+","+data[0]+","+data[1]+','+data[2]+','+data[3]+','+data[4]+','+data[5]+','+data[6]+','+data[7]);

				HotelVO hotel1 = new HotelVO();
				hotel1.setHotelid(hotelid);
				hotel1.setHotelname(data[0]);
				hotel1.setHotelregion(data[1]);
				hotel1.setHoteltype(data[2]);
				hotel1.setHotelurl(data[3]);
				hotel1.setHoteladdress(data[4]);
				hotel1.setHoteltel(data[5]);
				hotel1.setHotelfax(data[6]);
				hotel1.setHotelintro(data[7]);
				hotel1.setHotelop(0);
				int count1 = dao.insert(hotel1);
				System.out.println("insert " + count1 + " rows");
				System.out.println("---------------------------------");
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				dao.closeConn();
			} catch (SQLException e) {
			e.printStackTrace();
		} 
		}
	}
} // end of class EmpDAODemo