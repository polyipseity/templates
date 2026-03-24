use std::fs;
use std::path::Path;

fn main() {
    // Ensure .git/hooks folder exists before tests run
    let git_hooks_dir = Path::new(".git/hooks");
    let _ = fs::create_dir_all(git_hooks_dir);
}
