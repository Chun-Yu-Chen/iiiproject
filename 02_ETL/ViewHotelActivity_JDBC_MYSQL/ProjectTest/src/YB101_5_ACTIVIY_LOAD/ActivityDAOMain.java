package YB101_5_ACTIVIY_LOAD;

import java.io.*;
import java.sql.SQLException;
import java.util.*;

public class ActivityDAOMain {
	public static void main(String[] args) {
		IActivityDAO dao = new ActivityDAO();
		try {
			dao.getConnection();
			String[] data;
			String dataline = null;
			int countline = 0; // numbers of lines
			int recordline = 0; // numbers of record
			String activityid = null;

			// insert folkfestival
			String[] tempdata = new String[9];
			File readfile = new File(
					"C://Users//BigData//100_project//done//tainan_folkfestival.txt");
			InputStreamReader fr = new InputStreamReader(new FileInputStream(
					readfile), "UTF-8");
			BufferedReader br = new BufferedReader(fr);

			while ((dataline = br.readLine()) != null) {
				countline++;
				if (countline == 1) {
					continue;
				} // skip the line 1, title

				data = dataline.split("\\|");

				if (data.length < 9) { // 跳行的資料放到前一筆record之中
					tempdata[8] += data[0];
				}
				
				if (data.length == 9) { // 每筆資料應該要有的正常筆數為九
					for (int i = 0; i < 9; i++) { // 把資料站時放入tempdata以便結合後續跳行的資料
						tempdata[i] = data[i];
					}
					if (tempdata.length == 9 && tempdata[0] != null) {
						
						recordline++;
						if (recordline < 10) {
							activityid = "A000" + recordline;
						} else if (recordline >= 10 && recordline < 100) {
							activityid = "A00" + recordline;
						} else if (recordline >= 100 && recordline < 1000) {
							activityid = "A0" + recordline;
						} else {
							activityid = "H" + recordline;
						}
						
						System.out.println(activityid + "," + tempdata[0] + ","
								+ tempdata[1] + "," + tempdata[2] + ","
								+ tempdata[3] + "," + tempdata[4] + ","
								+ tempdata[5] + "," + tempdata[6] + ","
								+ tempdata[7] + "," + tempdata[8]);

						ActivityVO act = new ActivityVO();
						act.setActivityid(activityid);
						act.setActivityname(tempdata[0]);
						act.setActivityregion(tempdata[1]);
						act.setActivitytype(tempdata[2]);
						act.setActivityaddress(tempdata[3]);
						act.setActivitytel(tempdata[4]);
						act.setActivityintro(tempdata[8]);

						int count1 = dao.insertfolkfestival(act);
						System.out.println("insert folkfestival " + count1
								+ " rows");
						
						
						// insert 附近美食/景點/住宿資訊
						int neighborfood = tempdata[5].split("暫無提供").length;
						int neighborhouse = tempdata[6].split("暫無提供").length;
						int neighborspot = tempdata[7].split("暫無提供").length;
						if (neighborfood > 0) {
							String[] neighborfooddata = tempdata[5].split("\\/");
							for (String s : neighborfooddata) {
								ActivityNeighborVO nei = new ActivityNeighborVO();
								System.out.println(activityid+",美食,"+s);
								nei.setActivityid(activityid);
								nei.setNeighbortype("美食");
								nei.setNeighborname(s);
								int count2 = dao.insertneighbor(nei);
								System.out.println("insert neighbor " + count2
										+ " rows");
							}
						}//if (neighborfood > 0)
						
						if (neighborhouse > 0) {
							String[] neighborhousedata = tempdata[6]
									.split("\\/");
							for (String s : neighborhousedata) {
								ActivityNeighborVO nei = new ActivityNeighborVO();
								System.out.println(activityid+",住宿,"+s);
								nei.setActivityid(activityid);
								nei.setNeighbortype("住宿");
								nei.setNeighborname(s);
								int count2 = dao.insertneighbor(nei);
								System.out.println("insert neighbor " + count2
										+ " rows");
							}
						}//if (neighborhouse > 0)
						
						if (neighborspot > 0) {
							String[] neighborspotdata = tempdata[7]
									.split("\\/");
							for (String s : neighborspotdata) {
								ActivityNeighborVO nei = new ActivityNeighborVO();
								System.out.println(activityid+",景點,"+s);
								nei.setActivityid(activityid);
								nei.setNeighbortype("景點");
								nei.setNeighborname(s);
								int count2 = dao.insertneighbor(nei);
								System.out.println("insert neighbor " + count2
										+ " rows");
							}
						}//if (neighborspot > 0)
						System.out.println("---------------------------------");
					}//if (tempdata.length == 9 && tempdata[0] != null)
				}//if (data.length == 9)

			}// while
			
			countline=0;
			String[] tempdata1 = new String[5];
			String dataline1=null;
			File readfile1 = new File("C://Users//BigData//100_project//done//tainan_activity.txt");
			InputStreamReader fr1 = new InputStreamReader(new FileInputStream(readfile1), "UTF-8");
			BufferedReader br1 = new BufferedReader(fr1);
			Set<String> duplicatedata = new HashSet<>();
			while ((dataline1 = br1.readLine()) != null) {
				
				countline++;
				//System.out.println(countline);
				if (countline == 1) {
					continue;
				} // skip the line 1, title
				data = dataline1.split("\\|");
				if (data.length < 5) { // 跳行的資料放到前一筆record之中
					tempdata1[4] += data[0];
				}
				
				if (data.length == 5) { // 每筆資料應該要有的正常筆數為九
					for (int i = 0; i < 5; i++) { // 把資料站時放入tempdata以便結合後續跳行的資料
						tempdata1[i] = data[i];
						
					}
					if (tempdata1.length == 5 && tempdata1[0] != null) { // tempdata1裡面已經有完整資料。
						//去除重覆資料
						int before = duplicatedata.size();
						duplicatedata.add(tempdata1[0]);
						int after = duplicatedata.size();
						if (before==after){
							continue;
						}
						
						recordline++;
						if (recordline < 10) {
							activityid = "A000" + recordline;
						} else if (recordline >= 10 && recordline < 100) {
							activityid = "A00" + recordline;
						} else if (recordline >= 100 && recordline < 1000) {
							activityid = "A0" + recordline;
						} else {
							activityid = "H" + recordline;
						}

						System.out.println(activityid + "," + tempdata1[0]+ "," + tempdata1[1] + "," + tempdata1[2]+ "," + tempdata1[3] + "," + tempdata1[4]);
						ActivityVO act = new ActivityVO();
						act.setActivityid(activityid);
						act.setActivityname(tempdata1[0]);
						act.setActivityregion(tempdata1[1]);
						act.setActivitytype(tempdata1[2]);
						
						act.setActivityintro(tempdata1[4]);
						
						String[] month = tempdata1[3].split("月")[0].split(",");
						int[] month1 = new int[12];
						Arrays.fill(month1,1);
						for (String m:month){
							int a = Integer.parseInt(m);
							month1[a-1]=0;
						}
						act.setActivityjan(month1[0]);
						act.setActivityfeb(month1[1]);
						act.setActivitymar(month1[2]);
						act.setActivityapr(month1[3]);
						act.setActivitymay(month1[4]);
						act.setActivityjun(month1[5]);
						act.setActivityjul(month1[6]);
						act.setActivityaug(month1[7]);
						act.setActivitysep(month1[8]);
						act.setActivityoct(month1[9]);
						act.setActivitynov(month1[10]);
						act.setActivitydec(month1[11]);
						

						int count3 = dao.insertactivity(act);
						System.out.println("insert activity "+ count3
								+ " rows");
						System.out.println("---------------------------------");
					
					}//if (tempdata1.length == 5 && tempdata1[0] != null)
				}//	if (data.length == 5)
			
			
			}//while ((dataline1 = br1.readLine())

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
		}//finally
	}//main
} // end of class EmpDAODemo