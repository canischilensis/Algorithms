def merge_lists(nums1, m, nums2, n):
    p=(m+n)-1 #Ubicacion del primer apuntador
    #n-1 y m-1 ubicacion del segundo apuntador en cada lista 
    p1=m-1
    p2=n-1
    while 0 <= p1 and 0 <= p2:
        #nums2 nos sirve
        if nums1[p1]<nums2[p2]:
            nums1[p1]=nums2[p2]
            p2 -= 1
        #nums1 nos sirve
        else:
            nums1[p]=nums1[p1]
            p1 -= 1
            p -= 1
    # Complejidad T=O(n+m)=O(n)
    # Complejidad espacial S=O(1) es constante
    if n != m:
        nums1[ : p2 + 1] = nums2[ : p2 + 1]
    
    return nums1

# Arrays de prueba 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
response = merge_lists(nums1, m, nums2, n)
print(response)

# Arrays de prueba 2
nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [-4,2,3,9]
n = 4
response = merge_lists(nums1, m, nums2, n)
print(response)