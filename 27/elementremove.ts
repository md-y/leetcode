function removeElement(nums: number[], val: number): number {
    let j = 0;
    nums.forEach((elem, i) => {
        if (elem !== val) {
            nums[j] = nums[i];
            j++;
        }
    });
    return j;
}

