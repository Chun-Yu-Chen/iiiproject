package YB101_5_ACTIVIY_LOAD;

public class ActivityNeighborVO {
	private String activityid;//活動ID
	private String neighbortype;//附近景點類型
	private String neighborname;//附近景點名稱
	
	
	public void setActivityid (String activityid) {  this.activityid = activityid;  }
	public void setNeighbortype (String neighbortype) {  this.neighbortype = neighbortype;  }
	public void setNeighborname (String neighborname) {  this.neighborname = neighborname;  }
	
	public String getActivityid () {  return activityid;  }
	public String getNeighbortype () {  return neighbortype;  }
	public String getNeighborname () {  return neighborname;  }
	
	
} // end of class ActivityNeighborVO