
func quick_pow(_ x: Double, _ n: Int) -> Double {
    // Get the abs(n)
    var base = x, power = n.magnitude

    var res: Double = 1.0
    while power > 0 {
        if power & 1 == 1 {
            res *= base
        }
        base *= base
        power >>= 1
    }
    return n < 0 ? 1.0 / res : res
}
