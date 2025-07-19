class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums,low,high):
            if low < high :
                mid=(low+high)//2
                merge_sort(nums,low,mid)
                merge_sort(nums,mid+1,high)
                merge(nums,low,mid,high)
        def merge(nums,low,mid,high):
            b=[]
            i=low
            j=mid+1
            while i<=mid and j<=high:
                if nums[i] <= nums[j]:
                    b.append(nums[i])
                    i+=1
                else:
                    b.append(nums[j])
                    j+=1
            if i > mid :
                while j<=high:
                    b.append(nums[j])
                    j+=1
            else:
                while i<=mid:
                    b.append(nums[i])
                    i+=1
            for k in range(len(b)):
                nums[low+k]=b[k]
        merge_sort(nums,0,len(nums)-1)
        return nums
                


                    