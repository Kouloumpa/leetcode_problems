class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        List<Integer> result = new ArrayList<Integer>();
        HashSet<Integer> new_array = new HashSet<Integer>(); 
        
        for (int i : nums) {
            if (!new_array.contains(i))
                new_array.add(i);
        }
        
        for(int i = 1; i<=nums.length; i++){
            if (!new_array.contains(i)) {
                result.add(i);
            }
        }
        
        return result;
    }
}