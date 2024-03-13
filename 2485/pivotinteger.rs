impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let f = (((n * (n + 1)) >> 1) as f32).sqrt();
        if ((f as i32) as f32) == f {
            f as i32
        } else {
            -1
        }
    }
}
