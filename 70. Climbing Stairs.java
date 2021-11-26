class Solution {
    public int singleNonDuplicate(int[] nums) {
        int result;
        while (true) {
            int mid = nums.length / 2;
            if (!(subArray(nums, 0, mid).length % 2)) {
                nums = subArray(nums, 0, mid);
            }
            else if (!(subArray(nums, mid+1, nums.length-1).length % 2)) {
                nums = subArray(nums, mid+1, nums.length-1);
            }
            else result = mid;
            break;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = [1,1,2,3,3,4,4,8,8];
        System.out.println(singleNonDuplicate(nums));
    }
}