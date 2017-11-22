class SubArray(object):
    def ParseArray(self, nums):
        #Create dict for storing KV pairs of largest product and it's members
        dict = {}
        #test for array length, if 1, return member
        if len(nums) == 1:
            x = nums[0]
            return x
        else:
            #Find largest single value
            largestList = max(nums)
            #parse values into doublets, calculate products, store as KV pairs
            for each in range(0, len(nums) - 1, 1):
                keys = str(nums[each]) + "," + str(nums[each + 1])
                product = nums[each] * nums[each + 1]
                dict[keys] = product
            #Find largest in products    
            largestProduct = max(dict, key=dict.get)
            #Test if largest single value is bigger than largest product 
            if largestList > dict[largestProduct]:
                return largestList
            else:
                return ((largestProduct, dict[largestProduct]))
