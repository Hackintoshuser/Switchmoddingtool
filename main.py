import requests
import zipfile
import os


def download_and_extract_zip(url, destination_folder):
    local_zip_file = os.path.join(destination_folder, url.split("/")[-1])

    # Download the file
    response = requests.get(url)
    with open(local_zip_file, 'wb') as f:
        f.write(response.content)

    # Extract the file
    with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

    # Remove the downloaded zip file
    os.remove(local_zip_file)

    print("Download and extraction complete please visit https://switch.hacks.guide/user_guide/all/sd_preparation/ to add all the files correctly.")


def download_file(url, destination_folder):
    local_file = os.path.join(destination_folder, url.split("/")[-1])

    # Download the file
    response = requests.get(url)
    with open(local_file, 'wb') as f:
        f.write(response.content)

    print("Download complete.")


def download_all_files(downloads_folder):
    all_folder = os.path.join(downloads_folder, "all")
    os.makedirs(all_folder, exist_ok=True)

    urls = [
        "https://github.com/CTCaer/hekate/releases/download/v6.2.1/hekate_ctcaer_6.2.1_Nyx_1.6.3.zip",
        "https://switch.hacks.guide/files/emu/hekate_ipl.ini",
        "https://github.com/Atmosphere-NX/Atmosphere/releases/download/1.7.1/atmosphere-1.7.1-master-39c201e37+hbl-2.4.4+hbmenu-3.6.0.zip",
        "https://github.com/J-D-K/JKSV/releases/download/07%2F18%2F2024/JKSV.nro",
        "https://github.com/mtheall/ftpd/releases/download/v3.1.0/ftpd.nro",
        "https://github.com/exelix11/SwitchThemeInjector/releases/download/v4.7.1/NXThemesInstaller.nro",
        "https://github.com/joel16/NX-Shell/releases/download/4.01/NX-Shell.nro",
        "https://github.com/XorTroll/Goldleaf/releases/download/1.0.0/Goldleaf.nro",
        "https://switch.hacks.guide/files/emummc.txt"
    ]

    for url in urls:
        if url.endswith(".zip"):
            download_and_extract_zip(url, all_folder)
        else:
            download_file(url, all_folder)


def download_bare_minimum(downloads_folder):
    bare_minimum_folder = os.path.join(downloads_folder, "bare_minimum")
    os.makedirs(bare_minimum_folder, exist_ok=True)

    urls = [
        "https://github.com/CTCaer/hekate/releases/download/v6.2.1/hekate_ctcaer_6.2.1_Nyx_1.6.3.zip",
        "https://switch.hacks.guide/files/emu/hekate_ipl.ini",
        "https://github.com/Atmosphere-NX/Atmosphere/releases/download/1.7.1/atmosphere-1.7.1-master-39c201e37+hbl-2.4.4+hbmenu-3.6.0.zip"
    ]

    for url in urls:
        if url.endswith(".zip"):
            download_and_extract_zip(url, bare_minimum_folder)
        else:
            download_file(url, bare_minimum_folder)


def main():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    print("Select an option to download and install:")
    print("1. Hekate_ctcaer")
    print("2. Hekate_ipl.ini")
    print("3. Atmosphere")
    print("4. JKSV.nro")
    print("5. fptd.nro")
    print("6. NXthemesInstaller.nro")
    print("7. Nx-Shell")
    print("8. Emummc.txt")
    print("9. Goldleaf.nro")
    print("10. All Recommended packages")
    print("11. Bare minimum (ONLY cfw)")

    choice = input("Enter the numbers you want to download: ")

    if choice == "1":
        url = "https://github.com/CTCaer/hekate/releases/download/v6.2.1/hekate_ctcaer_6.2.1_Nyx_1.6.3.zip"
        download_and_extract_zip(url, downloads_folder)
        print("Credits to the creator https://github.com/CTCaer/")
    elif choice == "2":
        url = "https://switch.hacks.guide/files/emu/hekate_ipl.ini"
        download_file(url, downloads_folder)
    elif choice == "3":
        url = "https://github.com/Atmosphere-NX/Atmosphere/releases/download/1.7.1/atmosphere-1.7.1-master-39c201e37+hbl-2.4.4+hbmenu-3.6.0.zip"
        download_file(url, downloads_folder)
        print("Credits to the creator https://github.com/Atmosphere-NX")
    elif choice == "4":
        url = "https://github.com/J-D-K/JKSV/releases/download/07%2F18%2F2024/JKSV.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator https://github.com/J-D-K/")
    elif choice == "5":
        url = "https://github.com/mtheall/ftpd/releases/download/v3.1.0/ftpd.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator https://github.com/mtheall")
    elif choice == "6":
        url = "https://github.com/exelix11/SwitchThemeInjector/releases/download/v4.7.1/NXThemesInstaller.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator https://github.com/exelix11/")
    elif choice == "7":
        url = "https://github.com/joel16/NX-Shell/releases/download/4.01/NX-Shell.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator https://github.com/joel16")
    elif choice == "8":
        url = "https://switch.hacks.guide/files/emummc.txt"
        download_file(url, downloads_folder)
    elif choice == "9":
        url = "https://github.com/XorTroll/Goldleaf/releases/download/1.0.0/Goldleaf.nro"
        download_file(url, downloads_folder)
    elif choice == "10":
        download_all_files(downloads_folder)
    elif choice == "11":
        download_bare_minimum(downloads_folder)
    else:
        print("uhm choose correctly instead of not picking an option thats there >:( exiting")


if __name__ == "__main__":
    main()
