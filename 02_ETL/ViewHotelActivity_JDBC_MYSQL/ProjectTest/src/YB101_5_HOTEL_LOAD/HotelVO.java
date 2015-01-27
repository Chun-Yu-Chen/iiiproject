package YB101_5_HOTEL_LOAD;

public class HotelVO {
	private String hotelid;//飯店 ID
	private String hotelname;//飯店名稱
	private String hotelregion;//飯店所在區域
	private String hoteltype;//飯店類型
	private String hotelurl;//飯店網址
	private String hoteladdress;//飯店地址
	private String hoteltel;//飯店電話
	private String hotelfax;//飯店傳真
	private String hotelintro;//飯店介紹
	private int hotelop;//飯店是否營運
	
	
	public void setHotelid (String hotelid) {  this.hotelid = hotelid;  }
	public void setHotelname (String hotelname) {  this.hotelname = hotelname;  }
	public void setHotelregion (String hotelregion) {  this.hotelregion = hotelregion;  }
	public void setHoteltype (String hoteltype) {  this.hoteltype = hoteltype;  }
	public void setHotelurl (String hotelurl) {  this.hotelurl = hotelurl; }
	public void setHoteladdress (String hoteladdress) {  this.hoteladdress = hoteladdress;}
	public void setHoteltel (String hoteltel) {this.hoteltel = hoteltel;}
	public void setHotelfax (String hotelfax) {this.hotelfax = hotelfax;}
	public void setHotelintro (String hotelintro) {this.hotelintro = hotelintro;}
	public void setHotelop (int hotelop) {this.hotelop = hotelop;}
	
	public String getHotelid () {  return hotelid;  }
	public String getHotelname () { return hotelname;  }
	public String getHotelregion () {  return hotelregion;  }
	public String getHoteltype () {  return  hoteltype;  }
	public String getHotelurl () {  return hotelurl; }
	public String getHoteladdress () {  return hoteladdress;}
	public String getHoteltel () { return hoteltel;}
	public String getHotelfax () {return hotelfax;}
	public String getHotelintro () {return hotelintro;}
	public int getHotelop () { return hotelop;}
	
	
} // end of class HotelVO