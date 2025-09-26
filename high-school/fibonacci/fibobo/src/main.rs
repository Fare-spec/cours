fn main() {
    println!("Hello, world!");
    let f = fibobo(30);
    println!("{f}");
}

fn fibobo(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }
    return fibobo(n - 1) + fibobo(n - 2);
}
