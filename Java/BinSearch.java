public class BinSearch{
  public BinSearch(){}
  public void test(){
  
    System.out.println("Hello From Bin search");
  }
  // Given an array that is definitely a mountain,
  // return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
  public int peakIndexInMountainArray(int[] A) {
        int low = 0, high = A.length - 1;
        int mid;
        while (low <= high){
            mid = (high - low)/2 + low;
            if( A[mid] < A[mid + 1]){
                low = mid + 1;
            }
            else if (A[mid] < A[mid - 1]){
                high = mid - 1;
            }
            else return mid;
        }
        return -1;
        
    }
}
