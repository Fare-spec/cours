fn download_file(url: &str, output_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let response = get(url)?;
    if !response.status().is_success()
    let mut dest = File::create(Path::new(output_path))?;
    let mut content = response;
    copy(&mut content, &mut dest)?;
    println!("📥 Downloaded: {} → {}", url, output_path);

    Ok(())
}

fn main() {
    let url = "https://drive.proton.me/urls/XZ780G6P1M#kXUbcVjBlXPJ";
    let output = "sujets.zip";

    if let Err(e) = download_file(url, output) {
        eprintln!("❌ Erreur: {}", e);
    }
}
