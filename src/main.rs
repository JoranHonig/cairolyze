use clap::{Parser, Subcommand};

#[derive(Debug, Parser)] 
#[command(name = "cairolyze")]
#[command(about = "A tool to analyze cairo code and find vulnerabilities", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Debug, Subcommand)]
enum Commands {}


fn main() {
    let args = Cli::parse();
    match args.command {
        _ => ()
    }
}
