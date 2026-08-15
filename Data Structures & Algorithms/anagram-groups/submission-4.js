class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = {}
        for (let item of strs) {
            const sortedItem = item.split('').sort().join();
            if (!res[sortedItem]) {
                res[sortedItem] = [];
            }
            res[sortedItem].push(item)
        }
        return Object.values(res)
    }
}
