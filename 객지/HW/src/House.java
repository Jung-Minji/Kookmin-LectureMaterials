
public class House implements AreaInterface{
	
	private String houseAddress;
	private double area;
	
	public House() {
		this("±¹¹Î´ëÇÐ±³", 1700);
	}

	public House(String houseAddress, double houseArea) {
		this.houseAddress = houseAddress;
		this.area = houseArea;
	}
	
	


	public String getHouseAddress() {
		return houseAddress;
	}

	public void setHouseAddress(String houseAddress) {
		this.houseAddress = houseAddress;
	}



	public void setArea(double houseArea) {
		this.area = houseArea;
	}
	

	@Override
	public double getArea() {
		return area;
	}

	@Override
	public String toString() {
		return "House [houseAddress=" + houseAddress + ", houseArea=" + area + "]";
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		long temp;
		temp = Double.doubleToLongBits(area);
		result = prime * result + (int) (temp ^ (temp >>> 32));
		result = prime * result + ((houseAddress == null) ? 0 : houseAddress.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		House other = (House) obj;
		if (Double.doubleToLongBits(area) != Double.doubleToLongBits(other.area))
			return false;
		if (houseAddress == null) {
			if (other.houseAddress != null)
				return false;
		} else if (!houseAddress.equals(other.houseAddress))
			return false;
		return true;
	}
	
	
	
	
	

}
