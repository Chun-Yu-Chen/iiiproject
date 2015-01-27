package com.iii.ann;

import java.io.*;
import java.sql.*;


// delete a employee data
public class InsertDemo {
	public static void main(String[] args) {
		Connection conn = null;
		File f = null;
		FileInputStream fi = null;
		InputStreamReader ir = null;
		BufferedReader br = null;
		
		System.out.println("test1");
		try {     
			String connUrl = "jdbc:mysql://10.120.28.19:3306/db01";
			conn = DriverManager.getConnection(connUrl, "root", "iii");
			
			f = new File("C:\\Users\\BigData\\python\\report\\dic_info\\Food_info\\Food_info\\Food_info_all.txt");
			fi = new FileInputStream(f);
			ir = new InputStreamReader(fi, "UTF-8");
			br = new BufferedReader(ir);
						
			int id = 0;
			String fid = "";
			String temp = "";
			System.out.println("begin");
			
			while ((temp = br.readLine()) != null){
				id += 1;
				if (id < 10){
					fid = "f000"+id;
				} else if (id < 100){
					fid = "f00"+id;
				} else if (id < 1000){
					fid = "f0"+id;
				} else {
					fid = "f"+id;
				}
				System.out.println(fid);
				
				String[] st = temp.split("\\|");
				//System.out.println(st[0]+"|"+st[1]+"|"+st[2]+"|"+st[3]+"|"+st[4]+"|"+st[5]+"|"+st[6]+"|"+st[7]+"|"+st[8]+"|"+st[9]+"|"+st[10]+"|"+st[11]+"|"+st[12]+"|"+st[13]);
				String insStmt = "INSERT INTO foodinfo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
				PreparedStatement pstmt = conn.prepareStatement(insStmt);
					pstmt.setNString(1, fid);
					pstmt.setNString(2, st[0]);
					pstmt.setNString(3, st[1]);
					pstmt.setNString(4, st[2]);
					pstmt.setNString(5, st[3]);
					pstmt.setNString(6, st[4]);
					pstmt.setNString(7, st[5]);
					pstmt.setNString(8, st[6]);
					pstmt.setNString(9, st[7]);
					pstmt.setNString(10, st[8]);
					pstmt.setNString(11, st[9]);
					pstmt.setNString(12, st[10]);
					pstmt.setNString(13, st[11]);
					pstmt.setNString(14, st[12]);
					pstmt.setNString(15, st[13]);
					pstmt.setNString(16, st[14]);
					pstmt.setNString(17, st[15]);
					pstmt.setNull(18, java.sql.Types.DECIMAL);
					pstmt.setNull(19, java.sql.Types.DECIMAL);
				
			int num = pstmt.executeUpdate();
			System.out.println("insert count = " + num);
			}  // while 結束
			System.out.println("done");
		} catch (SQLException e) {
			if (e.getErrorCode() == 2627) // ï¿½Hï¿½ï¿½ PRIMARY KEY ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
			System.out.println("PK重複");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
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
}// end of class DeleteDemo


