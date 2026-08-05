class Solution {
    public int[] twoSum(int[] nums, int target) {

        // HashMap stores:
        // Key = the complement we are looking for
        // Value = the index of the number that needs that complement
        Map<Integer, Integer> complements = new HashMap<>();

        // Loop through every number in the array
        for (int i = 0; i < nums.length; i++) {

            // Check if the current number is a complement
            // that we've already stored
            Integer complementIndex = complements.get(nums[i]);

            // If it's not null, we've found two numbers
            // that add up to the target
            if (complementIndex != null) {
                return new int[]{complementIndex, i};
            }

            // Store the complement that this number needs
            // Example:
            // target = 9, current number = 2
            // Store (7 -> index 0)
            complements.put(target - nums[i], i);
        }

        // Problem guarantees a solution, but return an empty array
        // just in case no pair is found
        return new int[]{};
    }
}