package YB101_5_VIEW_LOAD;

public class ViewNeighborVO {
	private String viewid;//景點ID
	private String neighbortype;//附近景點類型
	private String neighborname;//附近景點名稱
	
	
	public void setViewid (String viewid) {  this.viewid = viewid;  }
	public void setNeighbortype (String neighbortype) {  this.neighbortype = neighbortype;  }
	public void setNeighborname (String neighborname) {  this.neighborname = neighborname;  }
	
	public String getViewid () {  return viewid;  }
	public String getNeighbortype () {  return neighbortype;  }
	public String getNeighborname () {  return neighborname;  }
	
	
} // end of class ViewNeighborVO