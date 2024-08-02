import requests
import zipfile
import os
import shutil


def download_and_extract_zip(url, destination_folder):
    try:
        local_zip_file = os.path.join(destination_folder, url.split("/")[-1])

        # Download the file
        print(f"Downloading {url}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(local_zip_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Extract the file
        print(f"Extracting {local_zip_file}...")
        with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)

        # Remove the downloaded zip file
        os.remove(local_zip_file)
        print(f"Downloaded and extracted {url}.")
    except Exception as e:
        print(f"Failed to download or extract {url}. Error: {e}")


def download_file(url, destination_folder):
    try:
        local_file = os.path.join(destination_folder, url.split("/")[-1])

        # Download the file
        print(f"Downloading {url}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(local_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded {url}.")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")


def move_nro_files_to_switch(downloads_folder):
    switch_folder = os.path.join(downloads_folder, "switch")
    os.makedirs(switch_folder, exist_ok=True)

    for file_name in os.listdir(downloads_folder):
        if file_name.endswith(".nro"):
            source_file = os.path.join(downloads_folder, file_name)
            destination_file = os.path.join(switch_folder, file_name)
            shutil.move(source_file, destination_file)
            print(f"Moved {file_name} to switch folder.")


def move_hbmenu_out_of_switch(downloads_folder):
    switch_folder = os.path.join(downloads_folder, "switch")
    hbmenu_file = os.path.join(switch_folder, "hbmenu.nro")
    destination_file = os.path.join(downloads_folder, "hbmenu.nro")

    if os.path.exists(hbmenu_file):
        shutil.move(hbmenu_file, destination_file)
        print(f"Moved hbmenu.nro out of switch folder.")


def move_hekate_ipl_to_bootloader(downloads_folder):
    bootloader_folder = os.path.join(downloads_folder, "bootloader")
    os.makedirs(bootloader_folder, exist_ok=True)

    hekate_ipl_file = os.path.join(downloads_folder, "hekate_ipl.ini")
    destination_file = os.path.join(bootloader_folder, "hekate_ipl.ini")

    if os.path.exists(hekate_ipl_file):
        shutil.move(hekate_ipl_file, destination_file)
        print(f"Moved hekate_ipl.ini to bootloader folder.")


def move_emummc_to_hosts(downloads_folder):
    atmosphere_folder = os.path.join(downloads_folder, "atmosphere")
    os.makedirs(atmosphere_folder, exist_ok=True)

    hosts_folder = os.path.join(atmosphere_folder, "hosts")
    os.makedirs(hosts_folder, exist_ok=True)

    emummc_file = os.path.join(downloads_folder, "emummc.txt")
    destination_file = os.path.join(hosts_folder, "emummc.txt")

    if os.path.exists(emummc_file):
        shutil.move(emummc_file, destination_file)
        print(f"Moved emummc.txt to atmosphere/hosts folder.")


def move_atmosphere_to_switch_files(downloads_folder):
    atmosphere_folder = os.path.join(downloads_folder, "atmosphere")



def download_all_files(downloads_folder):
    mod_folder = os.path.join(downloads_folder, "mod")
    os.makedirs(mod_folder, exist_ok=True)
    os.makedirs(os.path.join(mod_folder, "Switch-files"), exist_ok=True)

    urls = [
        "https://github.com/CTCaer/hekate/releases/download/v6.2.1/hekate_ctcaer_6.2.1_Nyx_1.6.3.zip",
        "https://switch.hacks.guide/files/emu/hekate_ipl.ini",
        "https://github.com/Atmosphere-NX/Atmosphere/releases/download/1.7.1/atmosphere-1.7.1-master-39c201e37+hbl-2.4.4+hbmenu-3.6.0.zip",
        "https://github.com/J-D-K/JKSV/releases/download/07%2F18%2F2024/JKSV.nro",
        "https://github.com/mtheall/ftpd/releases/download/v3.1.0/ftpd.nro",
        "https://github.com/exelix11/SwitchThemeInjector/releases/download/v4.7.1/NXThemesInstaller.nro",
        "https://github.com/joel16/NX-Shell/releases/download/4.01/NX-Shell.nro",
        "https://github.com/XorTroll/Goldleaf/releases/download/1.0.0/Goldleaf.nro",
        "https://switch.hacks.guide/files/emummc.txt",
        "https://github.com/fortheusers/hb-appstore/releases/download/v2.3.2/appstore.nro"
    ]

    for url in urls:
        if url.endswith(".zip"):
            download_and_extract_zip(url, mod_folder)
        else:
            download_file(url, mod_folder)

    move_nro_files_to_switch(mod_folder)
    move_hbmenu_out_of_switch(mod_folder)
    move_hekate_ipl_to_bootloader(mod_folder)
    move_emummc_to_hosts(mod_folder)
    move_atmosphere_to_switch_files(mod_folder)
    move_bootloader_to_switch-files(mod_folder)
    move_switch_to_switch-files(mod_folder)
    move_hbmenu_to_switch-files(mod_folder)
    if a < 11 :print("All downloads and extractions complete")


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

    move_nro_files_to_switch(bare_minimum_folder)
    move_hbmenu_out_of_switch(bare_minimum_folder)
    move_hekate_ipl_to_bootloader(bare_minimum_folder)
    move_emummc_to_hosts(bare_minimum_folder)
    print("Bare minimum files download and extraction complete.")


def main():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    print("Select an option to download and install:")
    print("1. Hekate_ctcaer")
    print("2. Hekate_ipl.ini")
    print("3. Atmosphere")
    print("4. JKSV.nro")
    print("5. ftpd.nro")
    print("6. NXThemesInstaller.nro")
    print("7. NX-Shell")
    print("8. Emummc.txt")
    print("9. Goldleaf.nro")
    print("10. Hb app menu.nro")
    print("11. All Recommended packages")
    print("12. Bare minimum (ONLY cfw)")

    choice = input("Enter the number you want to download: ")

    if choice == "1":
        url = "https://github.com/CTCaer/hekate/releases/download/v6.2.1/hekate_ctcaer_6.2.1_Nyx_1.6.3.zip"
        download_and_extract_zip(url, downloads_folder)
        print("Credits to the creator: https://github.com/CTCaer/")
        print("Download complete.")
    elif choice == "2":
        url = "https://switch.hacks.guide/files/emu/hekate_ipl.ini"
        download_file(url, downloads_folder)
        move_hekate_ipl_to_bootloader(downloads_folder)
        print("Download complete.")
    elif choice == "3":
        url = "https://github.com/Atmosphere-NX/Atmosphere/releases/download/1.7.1/atmosphere-1.7.1-master-39c201e37+hbl-2.4.4+hbmenu-3.6.0.zip"
        download_and_extract_zip(url, downloads_folder)
        print("Credits to the creator: https://github.com/Atmosphere-NX")
        print("Download complete.")
    elif choice == "4":
        url = "https://github.com/J-D-K/JKSV/releases/download/07%2F18%2F2024/JKSV.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator: https://github.com/J-D-K/")
        print("Download complete.")
    elif choice == "5":
        url = "https://github.com/mtheall/ftpd/releases/download/v3.1.0/ftpd.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator: https://github.com/mtheall")
        print("Download complete.")
    elif choice == "6":
        url = "https://github.com/exelix11/SwitchThemeInjector/releases/download/v4.7.1/NXThemesInstaller.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator: https://github.com/exelix11/")
        print("Download complete.")
    elif choice == "7":
        url = "https://github.com/joel16/NX-Shell/releases/download/4.01/NX-Shell.nro"
        download_file(url, downloads_folder)
        print("Credits to the creator: https://github.com/joel16")
        print("Download complete.")
    elif choice == "8":
        url = "https://switch.hacks.guide/files/emummc.txt"
        download_file(url, downloads_folder)
        move_emummc_to_hosts(downloads_folder)
        print("Download complete.")
    elif choice == "9":
        url = "https://github.com/XorTroll/Goldleaf/releases/download/1.0.0/Goldleaf.nro"
        download_file(url, downloads_folder)
        print("Download complete.")
    elif choice == "10":
        url = "https://github.com/fortheusers/hb-appstore/releases/download/v2.3.2/appstore.nro"
        download_file(url, downloads_folder)
        print("Download complete.")
    elif choice == "11":
        download_all_files(downloads_folder)
    elif choice == "12":
        download_bare_minimum(downloads_folder)
    else:
        print("Invalid choice. Exiting.")

a=0

if __name__ == "__main__":
    main()
