
def merge_sorted_array(arr,start_index,mid_index, end_index):
    merged = []
    left_index, right_index = start_index, mid_index+1
    
    while(left_index<=mid_index and right_index<=end_index):
        if(arr[left_index]<arr[right_index]):
            merged.append(arr[left_index])
            left_index +=1
        else:
            merged.append(arr[right_index])
            right_index +=1
    merged += arr[left_index:mid_index+1]
    merged += arr[right_index:end_index+1]
    arr[start_index:end_index+1] = merged


def merge_sort(arr, start_index, end_index):
    if(start_index>=end_index):
        return
    mid_index = (start_index+end_index)//2
    
    merge_sort(arr,start_index,mid_index)
    merge_sort(arr, mid_index+1, end_index)
    merge_sorted_array(arr, start_index, mid_index, end_index)


arr  = [10,0,200,40]
merge_sort(arr,0, len(arr)-1)
print(arr)