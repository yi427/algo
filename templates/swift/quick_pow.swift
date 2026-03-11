class QuickPow {
    static func pow(_ x: Double, _ n: Int) -> Double {
        var base = x, power = n.magnitude

        var res = 1.0
        while power > 0 {
            if power & 1 == 1 {
                res *= base
            }
            base *= base
            power >>= 1
        }
        return n < 0 ? 1.0 / res : res
    }
}
