use anyhow::Result;

fn main() -> Result<()>{
    let max = include_str!("./input.txt")
        .split("\n\n")
        .map(|x| {
            return x
                .split("\n")
                .flat_map(str::parse::<usize>)
                .sum::<usize>();
        })
        .max();
    
    println!("{:?}", max);
    return Ok(());

}
