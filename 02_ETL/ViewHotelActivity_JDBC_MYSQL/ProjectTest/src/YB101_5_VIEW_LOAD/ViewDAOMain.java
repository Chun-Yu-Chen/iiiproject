package YB101_5_VIEW_LOAD;

import java.io.*;
import java.sql.SQLException;
import java.util.*;

public class ViewDAOMain {
	public static void main(String[] args) {
		IViewDAO dao = new ViewDAO();
		try {
			dao.getConnection();
			String[] doc = { "tainan_mountain_spot", "tainan_nature_spot","tainan_geography_spot","tainan_hotspring_spot","tainan_culture_spot","tainan_resort_spot"};

			String[] data;
			String dataline = null;
			int recordline = 0; // numbers of record
			String viewid = null;
			for (int d = 0; d < doc.length; d++) {
				int countline = 0; // numbers of lines
				// insert mountain_spot
				String[] tempdata = new String[11];
				File readfile = new File(
						"C://Users//BigData//100_project//done//"+doc[d]+".txt");
				InputStreamReader fr = new InputStreamReader(
						new FileInputStream(readfile), "UTF-8");
				BufferedReader br = new BufferedReader(fr);

				while ((dataline = br.readLine()) != null) {
					countline++;
					if (countline == 1) {
						continue;
					} // skip the line 1, title

					data = dataline.split("\\|");

					if (data.length < 11) { // 跳行的資料放到前一筆record之中
						tempdata[10] += data[0];
					}

					if (data.length == 11) { // 每筆資料應該要有的正常筆數為九
						for (int i = 0; i < 11; i++) { // 把資料站時放入tempdata以便結合後續跳行的資料
							tempdata[i] = data[i];
						}
						if (tempdata.length == 11 && tempdata[0] != null) {

							recordline++;
							if (recordline < 10) {
								viewid = "V000" + recordline;
							} else if (recordline >= 10 && recordline < 100) {
								viewid = "V00" + recordline;
							} else if (recordline >= 100 && recordline < 1000) {
								viewid = "V0" + recordline;
							} else {
								viewid = "V" + recordline;
							}

							System.out.println(viewid + "," + tempdata[0] + ","
									+ tempdata[1] + "," + tempdata[2] + ","
									+ tempdata[3] + "," + tempdata[4] + ","
									+ tempdata[5] + "," + tempdata[6] + ","
									+ tempdata[7] + "," + tempdata[8] + ","
									+ tempdata[9] + "," + tempdata[10]);
							
							 ViewVO view = new ViewVO();
							 view.setViewid(viewid);
							 view.setViewname(tempdata[0]);
							 view.setViewregion(tempdata[1]);
							 view.setViewtype(tempdata[2]);
							 view.setViewurl(tempdata[3]);
							 view.setViewaddress(tempdata[4]);
							 view.setViewtel(tempdata[5]);
							 view.setViewstay(tempdata[9]);
							 view.setViewintro(tempdata[10]);
							 int count1 = dao.insertview(view);
							 System.out.println("insert view " + count1 + " rows");

							 //insert 附近美食/景點/住宿資訊
							 int neighborfood =tempdata[6].split("暫無提供").length;
							 int neighborhouse =tempdata[7].split("暫無提供").length;
							 int neighborspot =tempdata[8].split("暫無提供").length;
							 if (neighborfood > 0) {
								 String[] neighborfooddata =tempdata[6].split("\\/");
								 for (String s : neighborfooddata) {
									 if (s.length()==0){
										 continue;
									 }
									 ViewNeighborVO nei = new ViewNeighborVO();
									 System.out.println(viewid+",美食,"+s);
									 nei.setViewid(viewid);
									 nei.setNeighbortype("美食");
									 nei.setNeighborname(s);
									 int count2 = dao.insertneighbor(nei);
									 System.out.println("insert neighbor " + count2 + " rows");
								 }
							 }//if (neighborfood > 0)
							
							 if (neighborhouse > 0) {
							 String[] neighborhousedata = tempdata[7].split("\\/");
							 	for (String s : neighborhousedata) {
							 		if (s.length()==0){
										 continue;
									 }
							 		ViewNeighborVO nei = new ViewNeighborVO();
							 		System.out.println(viewid+",住宿,"+s);
							 		nei.setViewid(viewid);
							 		nei.setNeighbortype("住宿");
							 		nei.setNeighborname(s);
							 		int count2 = dao.insertneighbor(nei);
							 		System.out.println("insert neighbor " + count2+ " rows");
							 	}
							 }//if (neighborhouse > 0)
							
							 if (neighborspot > 0) {
								 String[] neighborspotdata = tempdata[8].split("\\/");
								 for (String s : neighborspotdata) {
									 if (s.length()==0){
										 continue;
									 }
									 ViewNeighborVO nei = new ViewNeighborVO();
									 System.out.println(viewid+",景點,"+s);
									 nei.setViewid(viewid);
									 nei.setNeighbortype("景點");
									 nei.setNeighborname(s);
									 int count2 = dao.insertneighbor(nei);
									 System.out.println("insert neighbor " + count2+ " rows");
								 }
							 }//if (neighborspot > 0)
							System.out.println("---------------------------------");
						}// if (tempdata.length == 9 && tempdata[0] != null)
					}// if (data.length == 9)

				}// while

			}//for (int i = 0; i < doc.length; i++)

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
		}// finally
	}// main
} // end of class EmpDAODemo