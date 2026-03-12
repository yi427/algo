class PrimeHelper {
    private let spf: [Int]
    private let primes: [Int]
    private let n: Int

    init(_ n: Int) {
        self.n = n
        var spf = Array(0...n)
        var primes: [Int] = []
        assert(n >= 2)

        for i in 2...n {
            if spf[i] == i {
                primes.append(i)
            }
            for prime in primes {
                if i * prime > n { break }
                spf[i * prime] = prime
                if i % prime == 0 { break }
            }
        }
        self.spf = spf
        self.primes = primes
    }

    func isPrime(_ x: Int) -> Bool {
        assert(x >= 2 && x <= n)
        return spf[x] == x
    }

    func factorize(_ x: Int) -> [(prime: Int, exp: Int)] {
        assert(x >= 2 && x <= n)
        var x = x
        var result: [(prime: Int, exp: Int)] = []

        while x > 1 {
            let p = spf[x]
            var exp = 0
            while x > 1 && spf[x] == p {
                x /= p
                exp += 1
            }
            result.append((p, exp))
        }

        return result
    }

    static func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            (a, b) = (b, a % b)
        }
        return a
    }

    static func lcm(_ a: Int, _ b: Int) -> Int {
        a / gcd(a, b) * b
    }
}
