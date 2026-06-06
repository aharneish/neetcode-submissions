class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        result=[]
        for freq in range(len(buckets)-1,0,-1):
            result.extend(buckets[freq])
            if len(result)>=k:
                return result[:k] 