

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int i=0, j=0;
    int *ans=(int*)malloc(numsSize*sizeof(int));
    while (i<n){
        ans[j]=nums[i];
        ans[j+1]=nums[n+i];
        i++;
        j=j+2;
    }
    *returnSize=numsSize;
    return ans;

}